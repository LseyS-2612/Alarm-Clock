import time
from playsound import playsound
#playsound("mixkit-classic-alarm-995.mp3")

CLEAR ="\033[2J"
CLEAR_AND_RETURN ="\033[H"

def alarm(seconds):
    time_elapsed =0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1

        time_left = seconds - time_elapsed
        minutes_left = time_left//60
        seconds_left = time_left%60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("mixkit-classic-alarm-995.mp3")

minutes = int(input("How many minutes for alarm clock:\n"))
sec = int(input("How many seconds for alarm clock:\n"))
alarm((minutes*60)+sec)