# WAP that schedules the following messages: 
# Monday at 9:00 AM: Start your weekly goals
# Wednesday at 5:00 PM: Review your weekly progress
# Friday at 6:00 PM: Weekly work completed. 

import schedule
import time 

MondayMsg = lambda: print("Start your weekly goals")
WednesdayMsg = lambda: print("Review your weekly progress")
FridayMsg = lambda: print("Weekly work completed.")

def main():
    schedule.every().monday.at("09:00").do(MondayMsg)
    schedule.every().wednesday.at("17:00").do(WednesdayMsg)
    schedule.every().friday.at("18:00").do(FridayMsg) 

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
