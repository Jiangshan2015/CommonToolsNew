from flet import *


def top_tip_widget():
    return Container(
        Text("备注:生成的图片在桌面CommonToolsImages文件夹中", size=15,
             color='white'),
        width=600,
        height=30,
    )


def start_read_widget(click=None):
    return Container(
        width=600,
        height=50,
        visible=True,
        alignment=alignment.center,
        bgcolor='0xE62A2A2A',
        border_radius=3,
        content=Text('开始读取', color='white'),
        on_click=click
    )


def loading_widget():
    return Row(
        controls=[
            Text("正在读取文件...",size=19),
            Container(width=100,
                      height=100,
                      content=Lottie(
                          src=f"../assets/loading03.json",
                          repeat=True,
                          reverse=True,
                          animate=True),
                      )
        ]
    )
