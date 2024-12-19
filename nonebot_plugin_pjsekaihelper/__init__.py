import json
import time
import datetime
from pickle import EMPTY_LIST

from nonebot import require
from pathlib import Path

from nonebot.params import ArgPlainText

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store
from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot import get_driver
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Event, MessageEvent, PrivateMessageEvent, MessageSegment


SUPERUSERS = get_driver().config.superusers
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_pjsekaihelper",
    description="世界计划插件，拥有组建车队等功能，持续开发中",
    usage="发送 pjsk help 查看帮助",
    type="application",
    supported_adapters={"~onebot.v11"},
    homepage="https://github.com/Ant1816/nonebot-plugin-pjsekaihelper",
    extra={
            "author": "Ant1",
            "version": "1.0.18",
            "priority": 10,
    },
)

room_data = []
plugin_data_dir: Path = store.get_plugin_data_dir()
ROOM_LIST_FILE: Path = store.get_plugin_data_file("room_list.json")

if not ROOM_LIST_FILE.exists():  # 判断文件存在
    ROOM_LIST_FILE.write_text('[]', encoding='utf-8')


def load_all_room():
    global room_data
    try:
        with open(ROOM_LIST_FILE, 'r', encoding='utf-8') as file:
            room_data = json.load(file)
    except FileNotFoundError:
        room_data = []
    if room_data:
        for room in room_data:
            last = datetime.datetime.strptime(room["CreatedTime"], "%Y-%m-%d %H:%M:%S")
            now = datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
            duration = now - last
            if duration.days > 0 or duration.seconds > 1800:
                room_data.remove(room)
                with open(ROOM_LIST_FILE, 'w', encoding='utf-8') as file:
                    json.dump(room_data, file, ensure_ascii=False, indent=2)
    return room_data


help_ = on_command("pjsk help", priority=10, block=True)
roomcreate = on_command("建车队", aliases={"组队", "组车队"}, priority=10, block=True)
roomnum = on_command("车队号", aliases={"房间号", "车号", "有烤吗", "有烤嘛", "ycm"}, priority=10, block=True)
roomdelete = on_command("删车队", aliases={"删队", "删除车队"}, priority=10, block=True)
roomreset = on_command("重置车队列表", priority=10, block=True, permission=SUPERUSER)


@help_.handle()
async def handle_help_message(bot: Bot, event: GroupMessageEvent):
    message = (
        "Project Sekai helper 世界计划小助手帮助\n"
        "！！！检测到车队创建时间超过半小时会自动删除哦！！！\n"
        "建车队/组队/组车队 <房间号> <服务器(日/台/韩/国际/中)>\n"
        "删除车队/删队/删车队 <房间号>\n"
        "车队号/房间号/车号/有烤吗/有烤嘛/ycm\n"
        "重置车队列表(仅限SUPERUSER)\n"
    )
    await help_.send(message)


@roomcreate.handle()
async def handle_create_room(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    new_room_data = load_all_room()
    args_list = args.extract_plain_text().split()

    if len(args_list) == 2:
        room_number = args_list[0]
        ServerInfo = args_list[1]
    else:
        room_number = ''
        ServerInfo = ''
        args = args.extract_plain_text()
        for i in args:
            if i.isdigit():
                room_number += i
            else:
                ServerInfo += i

    if room_number.isdecimal() and ServerInfo in ["日", "台", "韩", "国际", "中"]:
        new_room = {
            "RoomNumber": room_number,
            "Server": ServerInfo,
            "CreatedBy": event.get_user_id(),
            "CreatedTime": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        new_room_data.append(new_room)
    elif room_number.isdecimal():
        await roomcreate.finish(f"""房间创建失败 请检查输入的服务器 "{ServerInfo}" 是否正确""")
    elif ServerInfo in ["日", "台", "韩", "国际", "中"]:
        await roomcreate.finish(f"""房间创建失败 请检查输入的房间号 {room_number} 是否正确""")
    else:
        await roomcreate.finish("房间创建失败 请检查参数是否正确：<房间号> <服务器>")

    with open(ROOM_LIST_FILE, 'w', encoding='utf-8') as file:
        json.dump(new_room_data, file, ensure_ascii=False, indent=2)
    await roomcreate.send("房间创建成功")


@roomnum.handle()
async def handle_room_list(bot: Bot, event: GroupMessageEvent):
    roomlist = load_all_room()
    message_list = []
    if not roomlist:
        await roomnum.send("当前暂无房间 请新建一个吧")
    else:
        message = "房间列表: \n"
        symbol = "\n"
        for data in roomlist:
            processed_data = f"\n房间号：{data['RoomNumber']}\n服务器：{data['Server']}\n创建者：{data['CreatedBy']}\n创建时间：{data['CreatedTime']}"
            message_list.append(processed_data)
        message += symbol.join(message_list)
        await roomnum.send(message)


@roomdelete.handle()
async def handle_room_delete(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    new_room_data = load_all_room()
    room_number = args.extract_plain_text()
    group_id = event.group_id
    user_id = event.get_user_id()

    member = await bot.get_group_member_info(group_id=group_id, user_id=user_id)
    if member['role'] not in ['owner', 'admin'] and user_id not in SUPERUSERS:
        await roomdelete.finish("您没有权限执行此操作")

    for room in new_room_data:
        if room['RoomNumber'] == room_number:
            new_room_data.remove(room)

    with open(ROOM_LIST_FILE, 'w', encoding='utf-8') as file:
        json.dump(new_room_data, file, ensure_ascii=False, indent=2)
    await roomdelete.finish(f"删除房间{room_number}成功")


@roomreset.handle()
async def handle_room_reset(bot: Bot, event: GroupMessageEvent):
    global room_data
    with open(ROOM_LIST_FILE, 'w', encoding='utf-8') as file:
        json.dump([], file, ensure_ascii=False, indent=2)
    room_data = []
    await roomreset.finish("重置成功")
