import subprocess
import os
from ctypes  import *

screen_width = windll.user32.GetSystemMetrics(0)
screen_height = windll.user32.GetSystemMetrics(1)

path = input("Введите путь к файлу конфига Underlords (cfg): ")
config_file = os.path.join(path, "video.txt")

with open(config_file, 'r+') as f:
  lines = f.readlines()
  lines[8] = f'	"setting.defaultres"		"{screen_width}"\n'
  lines[9] = f'	"setting.defaultresheight"		"{screen_height}"\n'
  f.seek(0)
  f.writelines(lines)
  f.truncate()


steam_exe_path = input("Введите путь к папке Steam: ")

subprocess.call([steam_exe_path + '\\steam.exe'])