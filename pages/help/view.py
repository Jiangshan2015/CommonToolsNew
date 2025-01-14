from flet import *
from flet_mvc import FletView

from tools.constants import Constants


# view
class HelpView(FletView):
    def __init__(self, controller, model):
        view = [
            Container(
                width=Constants.PAGE_W,
                offset=transform.Offset(0, 0),
                image_src=f"../assets/bg_05.png",
                image_fit=ImageFit.COVER,
                content=Container(
                    padding=Padding(15, 20, 15, 10),
                    content=Column(
                        [
                            Text(
                                "使用帮助",
                                size=25,
                                color=colors.WHITE,
                                weight=FontWeight.W_100,
                            ),
                            Container(
                                width=Constants.PAGE_W - 30,
                                padding=padding.only(top=10),
                                height=Constants.SCREEN_H - 110,
                                content=Column(
                                    controls=model.help_column.value
                                )
                            ),
                        ],
                    )
                )
            )
        ]
        super().__init__(model, view, controller)
