import pynput as p
from pynput import keyboard
import time




# 创建一个键盘类
key_board = p.keyboard
# 创建一个键盘控制类
key_control = key_board.Controller()


def on_press(key):
    pass


# all_key.append(key)

def on_release(key):
    try:
        if key == keyboard.Key.home:
            for index,i in enumerate(f,start = 1):
                key_control.type(f'{index}.' + i + '\n')
                key_control.press(keyboard.Key.enter)
                key_control.release(keyboard.Key.enter)
                time.sleep(times)
        elif key == keyboard.Key.esc:
            return False
    except:
        pass


if __name__ == "__main__":
    print("欢迎来到，本程序由阿狸开发。")
    msg = input("请把文件拖入此处,然后按回车:")
    times = int(input("请输入听写间隔时间（单位/秒）,然后按回车:"))
    with open(msg,encoding = 'utf-8')as file:
        f = file.read().split('\n')

        
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        print("开启成功,打开qq聊天框按home自动报听写,Esc键停止")
        listener.join()
