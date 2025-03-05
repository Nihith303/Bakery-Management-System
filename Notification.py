import datetime
import time
import random
from plyer import notification

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10
    )

def get_user_input(prompt):
    return input(prompt).strip()

def get_time_input(prompt):
    while True:
        time_input = get_user_input(prompt)
        try:
            time_obj = datetime.datetime.strptime(time_input, "%H:%M")
            return time_obj.time()
        except ValueError:
            print("Invalid time format. Please use HH:MM (e.g., 08:30).")

def main():
    work_start_time = get_time_input("Enter your office start time (HH:MM): ")
    work_end_time = get_time_input("Enter your office end time (HH:MM): ")
    lunch_time = get_time_input("Enter your lunch time (HH:MM): ")
    snack_time = get_time_input("Enter your snack time (HH:MM): ")
    bedtime = get_time_input("Enter your bedtime (HH:MM): ")
    while True:
        current_time = datetime.datetime.now().time()
        current_day = datetime.datetime.now().strftime('%A')
        current_time_without_seconds = current_time.replace(second=0, microsecond=0)

        if current_day != "Sunday":
            if current_time_without_seconds == work_start_time:
                show_notification("Work Time", "It's time to start working!")
            elif current_time_without_seconds == lunch_time:
                show_notification("Lunch Time", "It's lunchtime!")
            elif current_time_without_seconds == snack_time:
                show_notification("Snack Time", "It's time for a quick snack!")
            elif current_time_without_seconds == work_end_time:
                show_notification("Time to Go Home", "It's time to go home!")

        if current_time_without_seconds == bedtime:
            show_notification("Bed Time", "It's bedtime. Have a good night's sleep!")
        elif current_day != "Sunday" and work_start_time <= current_time_without_seconds <= work_end_time:
            motivational_quotes = [
                "Stay motivated and keep going!",
                "Success is not final, failure is not fatal: It is the courage to continue that counts.",
                "Your future is created by what you do today, not tomorrow.",
                "Don't watch the clock; do what it does. Keep going.",
                "The secret of getting ahead is getting started.",
                "You are never too old to set another goal or to dream a new dream."
            ]
            show_notification("Motivational Quote", random.choice(motivational_quotes))
        time.sleep(60)


if __name__ == "__main__":
    main()