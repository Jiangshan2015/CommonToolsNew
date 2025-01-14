from flet import *
from flet_mvc import FletView
from tools.constants import Constants


# view
class TodoView(FletView):
    def __init__(self, controller, model):
        view = [
            Container(
                width=Constants.PAGE_W,
                offset=transform.Offset(0, 0),
                image_src=f"../assets/bg_02.png",
                image_fit=ImageFit.COVER,
                content=Container(
                    padding=Padding(15, 20, 15, 10),
                    content=Column(
                        [
                            Text(
                                "任务",
                                size=25,
                                color=colors.WHITE,
                                weight=FontWeight.W_100,
                            ),
                            Container(
                                ref=model.todo_time_picker_overlay,
                            ),
                            Container(
                                alignment=alignment.center,
                                content=SegmentedButton(
                                    style=ButtonStyle(bgcolor=colors.WHITE38, overlay_color='white'),
                                    on_change=model.handle_change,
                                    allow_multiple_selection=False,
                                    selected_icon=Icon(icons.TIMER),
                                    selected={"1"},
                                    segments=[
                                        Segment(
                                            value="1",
                                            label=Text("今天"),
                                            icon=Icon(icons.LOOKS_ONE),
                                        ),
                                        Segment(
                                            value="2",
                                            label=Text("明天"),
                                            icon=Icon(icons.LOOKS_TWO),
                                        ),
                                        Segment(
                                            value="3",
                                            label=Text("每天"),
                                            icon=Icon(icons.LOOKS_3),
                                        ),
                                    ],
                                ),
                            ),
                            Container(height=Constants.BODY_H,
                                      content=Column(
                                          [
                                              Container(
                                                  height=Constants.BODY_H - 70,
                                                  width=Constants.PAGE_W - 30,
                                                  content=Column(
                                                      ref=model.task_contents,
                                                      height=Constants.BODY_H - 70,
                                                      scroll=ScrollMode.ALWAYS,
                                                      horizontal_alignment=CrossAxisAlignment.CENTER
                                                  )
                                              ),
                                              Container(
                                                  width=Constants.PAGE_W - 30,
                                                  alignment=alignment.bottom_center,
                                                  padding=padding.only(top=5, left=5),
                                                  height=60,
                                                  border_radius=5,
                                                  content=Column(
                                                      ref=model.todo_content,
                                                      horizontal_alignment=CrossAxisAlignment.CENTER
                                                  )
                                              ),
                                          ],
                                          alignment=MainAxisAlignment.SPACE_BETWEEN,
                                      ),
                            ),
                        ],
                    )
                )
            )
        ]
        super().__init__(model, view, controller)
