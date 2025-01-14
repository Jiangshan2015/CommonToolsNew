import os
import openpyxl
from flet_core import FilePickerResultEvent
from flet_mvc import FletController, alert
from openpyxl_image_loader import SheetImageLoader

from pages.read_file.widget import top_tip_widget, loading_widget, start_read_widget
from tools.utils import MakeDir
from views.choose_file_view import ChooseFileView
from time import sleep


# Controller
class ReadFileController(FletController):
    # 选择文件按钮
    def file_on_click(self, e=None):
        self.model.get_directory_dialog.value.get_directory_path()

    # 选完文件回调
    def get_directory_result(self, e: FilePickerResultEvent):
        self.model.dir_path.value = e.path if e.path else ""
        if self.model.dir_path.value == "":
            self.alert("你未选中任何文件夹", alert.WARNING)
        else:
            arr = self.model.dir_path.value.split('/')
            self.model.read_file_content.set_value([top_tip_widget(),
                                                    ChooseFileView(on_click=self.file_on_click, pathName=arr[-1]),
                                                    start_read_widget(click=self.start_read),
                                                    ])
        self.update()

    # 开始读取
    def start_read(self, e=None):
        if self.model.dir_path.value == "":
            self.alert("你未选中任何文件夹", alert.WARNING)
        else:
            arr = self.model.dir_path.value.split('/')
            self.model.read_file_content.set_value([top_tip_widget(),
                                                    ChooseFileView(on_click=self.file_on_click, pathName=arr[-1]),
                                                    loading_widget(),
                                                    ])
        self.update()
        self.handleFiles()
        sleep(3)
        self.model.dir_path.value = ""
        self.model.read_file_content.set_value([top_tip_widget(),
                                                ChooseFileView(on_click=self.file_on_click),
                                                start_read_widget(click=self.start_read),
                                                ])
        self.update()

    def handleFiles(self):
        if self.model.dir_path.value == "":
            return
        save_dir = MakeDir('CommonToolsImages')
        file_paths = []
        for root, dirs, files in os.walk(self.model.dir_path.value):
            file_paths = [os.path.join(root, file) for file in files]
        for file_path in file_paths:
            if file_path.endswith('.xlsx'):
                print(file_path)
                workbook = openpyxl.load_workbook(file_path)
                for sheetName in workbook.sheetnames:
                    ws = workbook[sheetName]
                    image_loader = SheetImageLoader(ws)
                    num = ws.max_row
                    for i in range(2, num + 1):  # 从第2行开始，总行数要+1
                        try:
                            name = ws['A' + str(i)].value  # B列的文件名
                            image = image_loader.get('B' + str(i))  # C列的图片
                            image = image.convert('RGB')
                            image_name = save_dir + '/' + name + ".jpg"
                            image.save(image_name)  # 以Ai为名，存图片Ci
                        # 排除没有图片，或图片超出单元格的情况
                        except ValueError:
                            print("这一行没有图片：", i)

        print("结束了")
