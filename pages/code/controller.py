from time import sleep

import barcode
import qrcode
from barcode.writer import ImageWriter
from flet_core import FilePickerResultEvent
from flet_mvc import FletController, alert

from pages.write_file.widget import top_tip_widget, loading_widget, start_write_widget
from tools.utils import MakeDir
from views.choose_file_view import ChooseFileView


class CodeController(FletController):
    def handleQRFiles(self):
        save_dir = MakeDir('CommonToolsQr')
        print(save_dir)
        with open(self.model.dir_path.value, "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                img = qrcode.make(line)
                # 保存图片
                img.save(save_dir + "/" + line + ".png")

    def handleBarFiles(self):
        save_dir = MakeDir('CommonToolsBar')
        with (open(self.model.dir_path.value, "r") as f):
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                print(line)
                if line.isdecimal() and len(line) > 12:
                    bar = barcode.get('ean13', line, writer=ImageWriter())
                    bar.save(save_dir + "/" + line)

    # 选择文件按钮
    def file_on_click(self, e=None):
        self.model.get_directory_dialog.value.pick_files(
            allow_multiple=True
        )

    # 选完文件回调
    def get_directory_result(self, e: FilePickerResultEvent):
        self.model.dir_path.value = e.files[0].path if e.files[0].path else ""
        if self.model.dir_path.value == "":
            self.alert("你未选中任何文件", alert.WARNING)
        else:
            arr = self.model.dir_path.value.split('/')
            self.model.write_file_content.set_value([top_tip_widget(),
                                                     ChooseFileView(on_click=self.file_on_click, pathName=arr[-1]),
                                                     start_write_widget(click=self.start_make_code),
                                                     ])
        self.update()

    # 开始读取
    def start_make_code(self, e=None):
        if self.model.dir_path.value == "":
            self.alert("你未选中任何文件夹", alert.WARNING)
        else:
            arr = self.model.dir_path.value.split('/')
            self.model.write_file_content.set_value([top_tip_widget(),
                                                     ChooseFileView(on_click=self.file_on_click, pathName=arr[-1]),
                                                     loading_widget(),
                                                     ])
        self.update()
        self.handleBarFiles()
        self.handleQRFiles()
        sleep(3)
        self.model.dir_path.value = ""
        self.model.write_file_content.set_value([top_tip_widget(),
                                                 ChooseFileView(on_click=self.file_on_click),
                                                 start_write_widget(click=self.start_make_code),
                                                 ])
        self.update()
