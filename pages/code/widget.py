from flet import *


def top_tip_widget():
    return Container(
        Text("备注：条形码、二维码在桌面CommonToolsBar、CommonToolsQr文件夹中。条码只能数字并大于12位，如不满足则只有二维码",
             size=15,
             color='white'),
        width=600,
        height=50,
    )


def start_code_widget(click=None):
    return Container(
        width=600,
        height=50,
        visible=True,
        alignment=alignment.center,
        bgcolor='0xEEFFFFFF',
        border_radius=3,
        content=Text('开始生成', color='BLACK'),
        on_click=click
    )


def loading_widget():
    return Row(
        controls=[
            Text("正在写入生成码...", size=19),
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
