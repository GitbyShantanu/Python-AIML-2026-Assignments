# Create a function named DisplayMessage(message). 
# Schedule fn using schedule.every(5).seconds.do(DisplayMessage, message)
# The message should be accepted from user. 

import time 
import schedule

def DisplayMessage(message):
    print(message)


def main():
    msg = input("Enter the message: ")

    schedule.every(5).seconds.do(DisplayMessage, msg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

    