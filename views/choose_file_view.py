from flet import *


class ChooseFileView(Container):

    def __init__(self, on_click=None, pathName= "选择文件"):
        super().__init__()
        self.on_click = on_click
        self.width = 200
        self.height = 230
        self.border_radius = 8
        self.on_click = self.on_click
        self.alignment = alignment.center

        src_string="./../assets/icon_no_file.png"
        if not pathName == "选择文件":
            src_string = "./../assets/icon_has_file.png"

        self.content = Column(
            [
                Image(
                    src=src_string,
                    width=200,
                    height=200,
                    fit=ImageFit.CONTAIN,
                ),
                Container(content=Text(pathName,
                                       text_align=TextAlign.CENTER,
                                       color='black',
                                       width=200,
                                       height=30,
                                       ),
                          bgcolor=colors.WHITE)

            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=0

        )
