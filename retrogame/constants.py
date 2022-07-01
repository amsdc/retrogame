import ctypes


user32 = ctypes.windll.user32

SCREEN_WIDTH = user32.GetSystemMetrics(78)
SCREEN_HEIGHT = user32.GetSystemMetrics(79)
FILE_PATH = r"retro_score.json"