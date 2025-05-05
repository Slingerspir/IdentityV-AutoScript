import pyautogui
import cv2
import os

def capture_template(template_name):
    print('准备截取模板：请将游戏窗口置于前台')
    input('定位目标区域后按回车开始5秒倒计时...')
    
    for i in range(5,0,-1):
        print(f'倒计时{i}秒...')
        time.sleep(1)
    
    x1, y1 = pyautogui.position()
    print(f'已记录左上角坐标：({x1},{y1})')
    
    print('请移动鼠标到区域右下角并保持3秒')
    time.sleep(3)
    x2, y2 = pyautogui.position()
    
    img = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))
    if not os.path.exists('assets'):
        os.makedirs('assets')
    img.save(f'assets/{template_name}.png')
    print(f'模板已保存至：assets/{template_name}.png')