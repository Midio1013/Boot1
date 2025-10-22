from pyautogui import *

sleep(3)
moveTo(480,890,0.3)
i1=screenshot(region=(480,890,90,90))
i1.save("Icon.bmp")
moveTo(130,890,0.3)
i1=screenshot(region=(130,890,90,90))
i1.save("MDP.bmp")
moveTo(260,160,0.3)
i1=screenshot(region=(260,160,90,90))
i1.save("PP.bmp")
hotkey("win","1")