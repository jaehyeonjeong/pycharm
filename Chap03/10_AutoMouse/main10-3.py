import pyautogui
import time
import pyperclip

pyautogui.moveTo(1238,206,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 962
start_y = 138
end_x = 1852
end_y = 922
pyautogui.screenshot(r'.//SeoulWheathercast.png',
                    region=(start_x, start_y, end_x-start_x, end_y-start_y))