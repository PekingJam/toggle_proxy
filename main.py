from pystray import *
from PIL import Image
import winreg
import webbrowser

# 图标路径
blue_icon_path = "blue.png"
white_icon_path = "white.png"


# 获取代理状态
def get_proxy_status():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                             0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, "ProxyEnable")
        winreg.CloseKey(key)
        return bool(value)
    except Exception as e:
        print(f"Error reading proxy status: {e}")
        return False


# 切换代理状态
def toggle_proxy_status():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
                             0, winreg.KEY_SET_VALUE)
        current_status = get_proxy_status()
        new_status = not current_status
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, int(new_status))
        winreg.CloseKey(key)
        if new_status is not None:
            if new_status:
                path = blue_icon_path
                icon.notify("  开启系统代理成功✅", " ")
            else:
                path = white_icon_path
                icon.notify("  关闭系统代理成功✅", " ")
            print(path)
            new_image = Image.open(path)  # 替换为另一个图标的路径
            icon.icon = new_image
            icon.update_menu()
            icon.title = title_name()
    except Exception as e:
        print(f"Error toggling proxy status: {e}")
        return None


# 创建系统托盘图标
def create_tray_icon(icon_path):
    image = Image.open(icon_path)
    menu = (Menu(MenuItem('网页面板', webui), MenuItem('切换代理', toggle_proxy_status),
                 MenuItem('退出', on_exit), ))
    icon = Icon("proxy_icon", image, title_name(), menu=menu)
    return icon


def title_name():
    if get_proxy_status():
        return "系统代理已开启"
    else:
        return "系统代理已关闭"


def webui():
    webbrowser.open("http://127.0.0.1:9090/ui/#/proxies")


# 退出程序
def on_exit(con):
    con.stop()


# 启动系统托盘应用
if __name__ == "__main__":
    proxy_status = get_proxy_status()
    icon_path = blue_icon_path if proxy_status else white_icon_path
    icon = create_tray_icon(icon_path)
    icon.run()
