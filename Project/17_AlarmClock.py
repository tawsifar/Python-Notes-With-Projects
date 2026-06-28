import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    sound_file = "C:\\Users\\T4WSIF\\Desktop\\PyNotes\\Tutorials\\demomusic.mp3"  # make sure this file is in the same folder as the script
    is_running = True

    while is_running:
        # get current time as a string in HH:MM:SS format to match what the user typed
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        # compare current time string to alarm time string
        # when they match exactly, trigger the alarm
        if current_time == alarm_time:
            print("WAKE UP! 😴")

            # pygame.mixer handles audio playback
            # init() must be called before any mixer functions
            pygame.mixer.init()

            # load() prepares the audio file but doesnt play it yet
            pygame.mixer.music.load(sound_file)

            # play() starts the audio, default plays once
            # play(-1) would loop forever
            pygame.mixer.music.play()

            # get_busy() returns True while audio is still playing
            # this loop keeps the program alive until the song finishes
            # without this, the script would exit and cut the audio off
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False  # stop the main loop after alarm finishes

        time.sleep(1)  # check once per second so it doesnt burn CPU in a tight loop


# typo fix: original had _name_ (single underscores), needs __name__ (double)
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)