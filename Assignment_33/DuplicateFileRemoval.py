
import time
import sys
import os
import schedule
import FileUtils
import re
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    Border = "-"*70
    
    print(Border)
    print("Duplicate File Removal Automation Script")
    print(Border)

    if (len(sys.argv) == 2):    
        arg = sys.argv[1].lower()
        if arg == "--help" or arg == "--h":
            print("This automation script scans a directory, identifies duplicate files using checksums,\ndeletes duplicate files, create a log file, and sends log file through email.\n")
            print("For better usage please check --u or --usage flag")

        elif arg == "--usage" or arg == "--u":
            print("Usage: ")
            print("     python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <RecieverEmailId>\n")
            print("Note: Directory name should be absoulte path\n")
            print("Example:")
            print(f"     python {sys.argv[0]} E:/Data/Demo 50 demo@gmail.com")

        else:
            print("Error: Invalid option.")
            print("Please use --h or --u for help or usage")

    # Actual Logic begins here
    elif (len(sys.argv) == 4):
        try:
            DirectoryPath = sys.argv[1]
            
            Interval = int(sys.argv[2])
            if Interval <= 0:
                print("Error: Interval must be a positive integer greater than 0.")
                return

            EmailId = sys.argv[3]

            DirectoryPath = os.path.abspath(DirectoryPath)
            if os.path.isabs(DirectoryPath) == False:
                print("Error: Please provide an absolute path for the directory.")
                return
            
            if os.path.exists(DirectoryPath) == False:
                print("Error: The provided directory does not exist.")
                return

            # Email validation
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if re.fullmatch(pattern, EmailId) == None:
                print("Error: Invalid email address format. Please provide a valid email address.")
                return
            
            # Retrieve sender credentials from environment
            sender_email = os.getenv("SENDER_EMAIL")
            sender_app_password = os.getenv("SENDER_APP_PASSWORD")

            if not sender_email or not sender_app_password:
                print("Error: SENDER_EMAIL and SENDER_APP_PASSWORD must be set in the environment file (.env).")
                return

            print(f"Process started at: {time.ctime()}")
            print("Scheduling the duplicate file removal task...")            
            schedule.every(Interval).minutes.do(FileUtils.DeleteDuplicates, DirectoryPath, Interval, EmailId, sender_email, sender_app_password)

            # Perform one immediate scan upon starting
            FileUtils.DeleteDuplicates(DirectoryPath, Interval, EmailId, sender_email, sender_app_password)

            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("Error: Interval must be an integer representing minutes.")
        except KeyboardInterrupt:
            print("\nStopping the scheduler. Exiting program...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print(f"Process stopped at: {time.ctime()}")

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for help or usage")

    print(Border)
    print("Thank you For using Duplicate File Removal Automation")
    print(Border)

if __name__ == "__main__":
    main()

# --h, --u add done
# command line args done
# Log: scan report, errors done
# Schedule done
# module done
# email done