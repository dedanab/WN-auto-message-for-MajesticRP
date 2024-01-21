import datetime, configparser, pyautogui, pyperclip, time
config = configparser.ConfigParser()
config.read("settings.cfg", encoding="utf-8")

times = []
texts = []
for c in range(1, 25):
    advertisementtime = 'advertisementtime' + str(c)
    advertisementtime = config.get(f"advertisement{c}", f"time_{c}", raw=True)
    times.append(advertisementtime)
    advertisementtext = 'advertisementtext' + str(c)
    advertisementtext = config.get(f"advertisement{c}", f"text_advertisement{c}", raw=True)
    text = 'text' + str(c)
    text = eval(advertisementtext).translate(str.maketrans({'"':None}))
    texts.append(text)

while True:
    for i in range(24):
        date = datetime.datetime.today()
        gettime = date.strftime("%H:%M:%S")
        if gettime == times[i]:
            if (texts[i]) == '':
                pass
            else:
                pyautogui.press('t')
                time.sleep(2)
                pyperclip.copy(texts[i])
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press('enter')
                timescreen = date.strftime('[%d.%m.%Y] [%H.%M.%S]')
                time.sleep(3)
                pyautogui.screenshot(f'screenshot/{timescreen}.png')
                print(f'[{gettime}] Текст отправлен, скрин сохранён.')