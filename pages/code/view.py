from flet import *
from flet_mvc import FletView
from tools.constants import Constants


# view
class CodeView(FletView):
    def __init__(self, controller, model):
        view = [
            Container(
                width=Constants.PAGE_W,
                offset=transform.Offset(0, 0),
                image_src=f"../assets/bg_04.png",
                image_fit=ImageFit.COVER,
                content=Container(
                    padding=Padding(15, 20, 15, 10),
                    content=Column(
                        [
                            Text(
                                "批量生成码",
                                size=25,
                                color=colors.WHITE,
                                weight=FontWeight.W_100,
                            ),
                            Container(
                                width=Constants.PAGE_W - 30,
                                padding=padding.only(top=5, left=5),
                                height=Constants.SCREEN_H - 110,
                                border_radius=5,
                                content=Column(
                                    ref=model.write_file_content,
                                    wrap=True,
                                    spacing=30,
                                    run_spacing=10,
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    horizontal_alignment=CrossAxisAlignment.CENTER
                                )
                            ),
                        ],
                    )
                )
            )
        ]
        super().__init__(model, view, controller)
