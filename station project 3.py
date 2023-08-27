import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds // 3600:02}:{(seconds // 60) % 60:02}:{seconds % 60:02}")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def parse_time_input(time_input):
    try:
        hours, minutes, seconds = map(int, time_input.split(":"))
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        return None

user_input = input("Enter the countdown time in the format hours:minutes:seconds:\n")
total_seconds = parse_time_input(user_input)

if total_seconds is not None:
    countdown_timer(total_seconds)
else:
    print("Invalid input. Please enter a valid time in the format hours:minutes:seconds.")
