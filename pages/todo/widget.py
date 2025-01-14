from flet import *


def todo_bottom_btn(value_changed=None, click=None):
    return Container(
        width=600,
        height=50,
        visible=True,
        alignment=alignment.center,
        bgcolor='0xE62A2A2A',
        border_radius=3,
        content=Row(controls=[
            TextField(
                height=50,
                width=480,
                color="white",
                hint_text="输入任务",
                hint_style=TextStyle(color='white', size=15),
                border_color="transparent",
                on_change=value_changed
            ),
            TextButton("添加任务",
                       icon="chair_outlined",
                       on_click=click,
                       style=ButtonStyle(color="white")
                       ),
        ]),
    )


def task_cell(task_item, click=None, dataValue=0):
    type_time = ""
    if 'type_day' in task_item:
        if task_item["type_day"] == "1":
            type_time = "今天"
        elif task_item["type_day"] == "2":
            type_time = "明天"
        else:
            type_time = "每天"
    return Container(
        width=600,
        height=50,
        visible=True,
        alignment=alignment.center,
        bgcolor=colors.WHITE,
        border_radius=5,
        content=Row(controls=[
            TextButton(
                icon_color=colors.BLUE,
                icon="circle_outlined",
                on_click=click,
                style=ButtonStyle(color="white"),
                data=dataValue,  # 注意这里
            ),
            Column(
                controls=[
                    Container(
                        padding=Padding(0, 3, 0, 0),
                        content=Text(
                            width=480,
                            size=15,
                            disabled=True,
                            value=task_item["task"],
                        ),
                    ),
                    Container(
                        content=Row(
                            controls=[
                                Text(
                                    "任务",
                                    height=20,
                                    width=40,
                                    color=colors.GREY_600,
                                    size=13,
                                    disabled=True,
                                ),
                                Icon(name=icons.SHOPPING_BAG_OUTLINED, color=colors.GREY_600, size=15),
                                Text(type_time, size=13, color=colors.BLUE_300, ),
                                Text(task_item["time"], size=13, color=colors.GREY_600, )
                            ],
                            alignment=MainAxisAlignment.START,
                            spacing=5,
                        )
                    )
                ]
                , spacing=5
            )

        ]),
    )
