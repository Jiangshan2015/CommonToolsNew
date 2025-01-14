from flet import *


def top_tip_widget():
    return Container(
        Text("备注:如未找到对应图片，序号栏将设置绿色！", size=15,
             color='white'),
        width=600,
        height=30,
    )


def start_write_widget(click=None):
    return Container(
        width=600,
        height=50,
        visible=True,
        alignment=alignment.center,
        bgcolor='0xE62A2A2A',
        border_radius=3,
        content=Text('开始写入', color='white'),
        on_click=click
    )


def loading_widget():
    return Row(
        controls=[
            Text("正在写入文件...",size=19),
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