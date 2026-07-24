# WAP that accepts: 
#   a) A message from server
#   b) A time interval in seconds. 
# Schedule the program to display the msg repeadely after specified interval

# Input: 
#   Enter Message: Jay Ganesh
#   Enter interval in seconds: 5 
#   Validate that interval is > 0

# Output:
#   Jay Ganesh

import schedule
import time

def Display(msg):
    print(msg)

def main():
    msg = input("Enter message from server: ")
    interval = int(input("Enter interval in seconds: "))

    if interval <= 0:
        print("Invalid interval")
        return

    schedule.every(interval).seconds.do(Display, msg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()