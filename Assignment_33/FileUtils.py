import time
from datetime import datetime
import os
import hashlib
import MarvellousMailSender as MailSender

def SendLogMail(SenderEmailId, SenderAppPassword, RecieverEmailId, content, logFilePath, errLogFileName):
    """
    Sends an email with the log report as an attachment using MarvellousMailSender.

    Note: This function assumes MarvellousMailSender.send_mail exists and takes
    (sender_email, app_password, receiver_email, subject, body, attachment_path).
    The 'content' parameter is used as the email body, and 'logFilePath' as the attachment.
    Errors encountered during email sending are logged to error log file if provided.
    """

    subject = "Duplicate Files Removal Report"
    try:
        MailSender.send_mail_with_attachment(SenderEmailId, SenderAppPassword, RecieverEmailId, subject, content, logFilePath)
        return True, None

    except Exception as e:
        error_message = f"Error in sending mail: {e}"
        with open(errLogFileName, "a") as efobj:
            efobj.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {error_message}\n")
        print(f"\n[Email Error] Failed to send report: {e}")
        return False, error_message


def CalculateCheckSum(Filename):
    fobj = None
    try:
        fobj = open(Filename, "rb")
        hobj = hashlib.md5()
        buffer = fobj.read(1024)

        while len(buffer) > 0:
            hobj.update(buffer)
            buffer = fobj.read(1024)
        return hobj.hexdigest()

    except Exception:
        return None
    finally:
        if fobj:
            fobj.close()


def FindDuplicates(DirectoryName): 
    if os.path.exists(DirectoryName) == False:
        errMsg = "Error: Provided path does not exist."
        return None, 0, errMsg

    if os.path.isdir(DirectoryName) == False:
        errMsg = "Error: Provided path is not a valid directory."
        return None, 0, errMsg

    if os.access(DirectoryName, os.R_OK) == False:
        errMsg = "Error: Permission denied for the provided directory."
        return None, 0, errMsg

    totalFileCnt = 0
    Duplicates = dict()

    for Foldername, Subfolder, Filename in os.walk(DirectoryName):
        for fname in Filename:
            totalFileCnt += 1
            fname = os.path.join(Foldername, fname)   
            CheckSum = CalculateCheckSum(fname)

            if CheckSum:
                if CheckSum in Duplicates:
                    Duplicates[CheckSum].append(fname)
                else:
                    Duplicates[CheckSum] = [fname]

    return Duplicates, totalFileCnt, None


def SafelyDeleteFile(filePath, errLogFileName):
    error_to_log = None
    if not os.path.exists(filePath):
        error_to_log = f"Error: File to be deleted '{filePath}' no longer exists.\n"

    elif not os.path.isfile(filePath):
        error_to_log = f"Error: Path '{filePath}' is not a file and cannot be deleted.\n"

    elif not os.access(filePath, os.W_OK):
        error_to_log = f"Error: Permission denied. Cannot delete file '{filePath}'.\n"

    if error_to_log:
        with open(errLogFileName, "a") as efobj:
            efobj.write(error_to_log)
        return False

    try:
        os.remove(filePath)
        return True
    except Exception as e:
        with open(errLogFileName, "a") as efobj:
            efobj.write(f"An unexpected error occurred while deleting file {filePath}: {e}\n")
        return False


def WriteLogReport(lfobj, DirectoryName, TotalFilesCount, Result, deletedCnt, deletedFilesList, DuplicateDict, totaltime, reciver_email_id, sender_email_id, sender_app_password, errLogFileName):
    lfobj.write("-" * 70 + "\n")
    lfobj.write("Scanning and Deletion Report\n")
    lfobj.write("-" * 70 + "\n")
    
    lfobj.write(f"Directory Scanned: {DirectoryName}\n")
    lfobj.write(f"Total Files Scanned: {TotalFilesCount}\n")
    lfobj.write(f"Total Duplicate files Found: {len(Result)}\n")
    lfobj.write(f"Total duplicate Files Deleted: {deletedCnt}\n")

    duplicateChecksums = []
    for checksum, files in DuplicateDict.items():
        if len(files) > 1:
            duplicateChecksums.append(checksum)

    lfobj.write("Complete paths of all deleted files:\n")
    if deletedFilesList:
        for path in deletedFilesList:
            lfobj.write(f"  - {path}\n")
    else:
        lfobj.write("  (No files were deleted in this run)\n")

    lfobj.write("CheckSum values of duplicate files:\n")
    if duplicateChecksums:
        for checksum in duplicateChecksums:
            lfobj.write(f"  - {checksum}\n")
    else:
        lfobj.write("  (No duplicate checksums found)\n")

    lfobj.write(f"Time Taken: {totaltime:.4f} seconds\n")    
    lfobj.write("-" * 70 + "\n")

    log_file_path = lfobj.name # Get the path of the log file

    # Flush the buffer to ensure all content is written to the file before reading.
    lfobj.flush()
    with open(log_file_path, 'r') as f:
        email_body_content = f.read()

    success, message = SendLogMail(sender_email_id, sender_app_password, reciver_email_id, email_body_content, log_file_path, errLogFileName)
    if success:
        print(f"\n[Email Success] Report sent successfully to {reciver_email_id}")
        lfobj.write(f"Email report sent successfully to {reciver_email_id}\n")


def DeleteDuplicates(DirectoryName, Interval, RecieverEmailId, SenderEmailId, SenderAppPassword):
    start_time = time.perf_counter()
    DuplicateDict, TotalFilesCount, errMsg = FindDuplicates(DirectoryName)

    logDir = "Marvellous"
    if os.path.exists(logDir) == False:
        os.makedirs(logDir)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    logFileName = os.path.join(logDir, f"DuplicateRemovalLog_{timestamp}.log")
    errLogFileName = os.path.join(logDir, f"DuplicateRemovalErrorLog_{timestamp}.log")

    if errMsg:
        efobj = open(errLogFileName, "w")
        efobj.write(errMsg + "\n")
        efobj.close()
        return

    lfobj = open(logFileName, "w")

    lfobj.write(f"Scan started at: {time.ctime()}\n")

    Result = list(filter((lambda x: len(x) > 1), DuplicateDict.values()))
    
    deletedFilesList = []
    deletedCnt = 0
    count = 0

    for value in Result:
        for subvalue in value:
            count += 1
            if count > 1:
                if SafelyDeleteFile(subvalue, errLogFileName):
                    deletedFilesList.append(subvalue)
                    deletedCnt += 1

        count = 0

    end_time = time.perf_counter()
    totaltime = end_time - start_time

    lfobj.write(f"Scan completed at: {time.ctime()}\n")

    WriteLogReport(lfobj, DirectoryName, TotalFilesCount, Result, deletedCnt, deletedFilesList, DuplicateDict, totaltime, RecieverEmailId, SenderEmailId, SenderAppPassword, errLogFileName)

    lfobj.close()
