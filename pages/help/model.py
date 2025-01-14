from flet_mvc import data, FletModel
from flet import *


# Model

class HelpModel(FletModel):
    @data
    def help_data(self):
        return [
            "1、程序异常崩溃闪退，重启电脑解决",
            "2、Excel的格式一定要正确,以.xlsx结尾的",
            "3、程序运行时，不要手动打开excel，如打开请关闭",
            "4、若拷贝CommonToolsImages文件夹到桌面，则可省略读取文件",
            "5、桌面生成的CommonToolsImages文件夹不要删除",
            "6、如果程序卡在动画，可能报错了，检查excel是否正常打开",
            "7、定期清理电脑垃圾，不行就换",
            "8、部分windows系统上有兼容性问题",
            "9、Todo新建任务后，重启程序才能执行",
        ]

    @data
    def help_column(self):
        items = []
        for i in range(0, len(self.help_data.value)):
            items.append(
                Text(self.help_data.value[i], color='white'),
            )
        return items
