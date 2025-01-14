import os
import shutil
import sys

from flet import *
from flet_components.toasts_flexible import ToastsFlexible, Position

toasts_history = {}


# toast
def Toast(pg, desc):
    ToastsFlexible(
        page=pg,
        icon=icons.INFO,
        title="提示",
        desc=desc,
        auto_close=None,
        trigger=None,
        set_history=toasts_history,
        position=Position.TOP_RIGHT,
    )


def MakeDir(dirName):
    print(os.name, sys.platform)
    if sys.platform == 'darwin':
        desktop_path = os.path.expanduser('~/Desktop')
        folder_path = os.path.join(desktop_path, dirName)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.mkdir(folder_path)
        return folder_path
    return ''
