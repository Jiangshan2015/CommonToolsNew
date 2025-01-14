from flet import *

from tools.constants import Constants

# contents = [
#     {"icon": "icon_read.png", "title": "读文件"},
#     {"icon": "icon_write.png", "title": "写文件"},
#     {"icon": "icon_code.png", "title": "条码器"},
#     {"icon": "icon_plan.png", "title": "Todo"},
#     # {"icon": "icon_cloud.png", "title": "暂时无"},
#     {"icon": "icon_help.png", "title": "使用帮助"}
# ]


def MenuRailContent(index: int, on_click=None, chooseIndex=0,contents=[]):
    cell_icon = str(contents[index]['icon']),
    cell_title = str(contents[index]['title']),
    content_color = "0xFFEAE8E8" if chooseIndex == index else "white"

    def content_click(e):
        on_click(index),

    return Container(
        height=40,
        margin=margin.only(top=5,bottom=5),
        padding=padding.only(left=20),
        on_click=content_click,
        width=Constants.LEFT_W,
        bgcolor=content_color,
        content=Row(
            [
                Image(
                    src=f"../assets/{cell_icon[0]}",
                    width=15,
                    height=15,
                    fit=ImageFit.CONTAIN,
                ),
                Text(cell_title[0]),
            ],
        )
    )
