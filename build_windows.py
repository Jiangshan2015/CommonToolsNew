import PyInstaller.__main__
import os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'main.py',  # 你的主程序文件
    '--name=CommonTools',  # 应用名称
    '--windowed',  # 无控制台窗口
    '--onefile',  # 打包成单个文件
    '--icon=assets/icon.ico',  # 应用图标（如果有的话）
    '--add-data=assets;assets',  # 添加资源文件夹（如果有的话）
    '--clean',  # 清理临时文件
    '--noconfirm',  # 不确认覆盖
    f'--distpath={os.path.join(current_dir, "dist")}',  # 输出目录
    '--add-binary=flet;flet',  # 添加flet依赖
])