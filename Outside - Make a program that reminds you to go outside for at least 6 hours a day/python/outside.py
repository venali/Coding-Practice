import time
from datetime import datetime, timedelta

def remind_to_go_outside():
    total_hours = 0
    target_hours = 6
    last_reminder_time = datetime.now()
    
    print("Reminder system initialized. Don't forget to go outside for at least 6 hours a day!")

    while total_hours < target_hours:
        current_time = datetime.now()
        
        # Check if an hour has passed since the last reminder
        if current_time - last_reminder_time >= timedelta(hours=1):
            total_hours += 1
            last_reminder_time = current_time
            print(f"Reminder #{total_hours}: Time to go outside! Total time outside: {total_hours} hour(s)")
        
        # Wait for a minute before checking again
        time.sleep(60)

    print(f"Congrats! You've been outside for {target_hours} hours today. Well done!")

if __name__ == "__main__":
    remind_to_go_outside()