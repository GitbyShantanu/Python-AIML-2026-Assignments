import psutil
import os
import MarvellousMailSender as MailSender


def get_process_info():
    ProcList = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            ProcList.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return ProcList


def get_process_name_info(proc_name):
    proc_name = proc_name.strip().lower()
    procList = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])

            if (pinfo["name"].lower() == proc_name) or (proc_name in pinfo["name"].lower()): 
                procList.append(pinfo)
                break

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    return procList


def log_process(process_list, DirectoryName="."):
    if os.path.exists(DirectoryName) == False:
        return "Directory does not exists"

    if os.path.isdir(DirectoryName) == False:
        return "Directory exists, but it is not a directory" 

    fobj = open(f"{DirectoryName}/ProcInfo.log", "w")

    if len(process_list) == 0:
        fobj.write(f"No process found")
        fobj.close()
        return
    
    i = 0
    for proc in process_list:
        fobj.write(f"{i+1}. Process Name: {proc['name']}, PID: {proc['pid']}, Username: {proc['username']}\n")
        i += 1

    fobj.close()


def sendLogMail(reciever_mail, body):
    try:
        sender_email = "demo.shan24@gmail.com"
        app_password = "rjkgsuuhrlvqesmi"
        subject = "Log Mail from Python Assignment 34 Script"

        Ret, err = MailSender.send_mail(sender_email, app_password, reciever_mail, subject, body)
        if Ret == False:
            return False, err
        return True, None
    
    except Exception as e:
        return False, str(e)

def sendLogMailWithAttachment(reciever_mail, body, attachment_file_path):
    try:
        sender_email = "demo.shan24@gmail.com"
        app_password = "rjkgsuuhrlvqesmi"
        subject = "Log Mail from Python Assignment 34 Script"

        Ret, err = MailSender.send_mail_with_attachment(sender_email, app_password, reciever_mail, subject, body, attachment_file_path)
        if Ret == False:
            return False, err
        
        return True, None
    
    except Exception as e:
        return False, str(e)