from flet_mvc import FletView
from tools.constants import Constants
from views.menu_view import *


# view
class HomeView(FletView):
    def __init__(self, controller, model):
        view = [
            Container(
                bgcolor='white',
                expand=True,
                content=Row(
                    spacing=0,
                    controls=[
                        Container(
                            width=Constants.LEFT_W,
                            margin=margin.only(top=50),
                            content=Column(
                                controls=[
                                    MenuView(on_click=controller.menu_clicked,
                                             menuContents=model.menu_content.value),
                                    Container(
                                        height=50,
                                    ),
                                ]
                            )
                        ),
                        Container(
                            expand=True,
                            content=Stack(
                                controls=model.content_widgets.value
                            )
                        ),
                    ]
                )
            )
        ]
        super().__init__(model, view, controller)
