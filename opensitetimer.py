from datetime import datetime
import os
import time
import webbrowser
time1 = datetime.now().strftime('%H:%M')
at = input("What time should the alarm go off? (HH:MM)\n")
td = input("What site should open when the alarm goes off?\n")
while True:
    if at == time1:
        webbrowser.open(td)
        print("Set time reached!")
        break
    time.sleep(1)
    time1 = datetime.now().strftime('%H:%M')
