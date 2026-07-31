# Please follow these rules while designing automation script as: 
# 1. Accept input through command line or thorugh file
# 2. Display any message in log file instead of console.
# 3. For seperate task define seperate function. 
# 4. For rubustness handle every expected exception
# 5. Perform validations before taking any action
# 6. Create user defined modules to store the functionality. 

# Q1. Design automation script which accepts Directory name, email id from user and create log file in that directory that displays info of running processes as its name, PID, username. 
# Usage : ProcInfo.py Demo abc@gmail.com

import ProcUtil
import os
import sys
import re


def main():
    if len(sys.argv) != 3:
        print("Error: Please provide Directory name and Email ID as command-line arguments.")
        print("Usage: python Assignment34_4.py <DirectoryName> <EmailId>")
        return

    try:    
        DirectoryName = sys.argv[1]
        EmailId = sys.argv[2]

        if not os.path.exists(DirectoryName):
            os.mkdir(DirectoryName)
        elif not os.path.isdir(DirectoryName):
            print(f"Error: '{DirectoryName}' exists, but it is not a directory.")
            return

        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.fullmatch(pattern, EmailId) is None:
            print(f"Error: Invalid Email ID '{EmailId}'. Please provide a valid email address.")
            return

        ProcList = ProcUtil.get_process_info()

        err = ProcUtil.log_process(ProcList, DirectoryName)
        if err:
            print(f"Error logging process information: {err}")
            return
        print("Processes logged successfully.")

        log_file_path = os.path.join(DirectoryName, "ProcInfoLogs.log")
        body = "Please find the process log attached.\n\n"
        body += "Regards,\nShantanu D"

        mail_sent, error = ProcUtil.sendLogMailWithAttachment(EmailId, body, log_file_path)
        if mail_sent:
            print(f"Process log successfully sent to {EmailId}")
        else:
            print(f"Failed to send email to {EmailId}: {error}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()