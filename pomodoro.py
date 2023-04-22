from time import sleep
from win11toast import toast
from os import system

def cls():
    system('cls')

def progress_bar(minutes):
    for j in range(1, minutes+1):
        for i in range(1, 61):
            sleep(0.925)
            if i > 50:
                space = "0"
            else:
                space = ""
            cls()
            print(f"Time left: {minutes-j}:{space}{60-i}")

try:
    focus = int(input("Enter focus time in minutes: "))
    break_variant = int(input("After how many focus sessions do you want to take a long break? (0 for no long breaks): "))
    break_long = int(input("Enter long break time in minutes: "))
    break_short = int(input("Enter short break time in minutes: "))
    cls()
except:
    print("Wrong input!\nSettings will be set to default values.")
    focus = 25
    break_variant = 2
    break_long = 15
    break_short = 5
    sleep(3)
    cls()

reps = 0

def empty(*arg):
    pass

def main():
    global reps
    try:
        while True:
            toast("Pomodoro", "Focus!", on_dismissed=empty)
            progress_bar(focus)
            reps += 1

            if break_variant == reps:
                toast("Pomodoro", "Long Break!", on_dismissed=empty)
                progress_bar(break_long)
                reps = 0
            else:
                toast("Pomodoro", "Short Break!", on_dismissed=empty)
                progress_bar(break_short)
    except KeyboardInterrupt:
        print("Pomodoro reset.")
        input("Press enter to continue...")
        cls()
        main()

if __name__ == "__main__":
    main()
    