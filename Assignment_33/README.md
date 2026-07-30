# Duplicate File Removal Automation

A command-line Python script that scans a directory for duplicate files, removes them based on MD5 checksum comparison, and emails a detailed report after every run — on a configurable schedule.

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Email Configuration](#email-configuration)
- [Command-Line Options](#command-line-options)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Log File Details](#log-file-details)
- [Important Notes](#important-notes)

---

## Overview

Duplicate files accumulate quietly — backups, re-downloads, copy-paste accidents. Over time they waste storage and make directories harder to manage. This script automates the full cleanup pipeline without any manual intervention.

On each scheduled run it recursively scans a target directory, fingerprints every file with an MD5 checksum, deletes all duplicate copies while keeping one original from each group, writes a timestamped report to disk, and emails that report as an attachment to a specified recipient.

You run it once. It handles the rest.

---

## How It Works

```
START
  |
  v
Parse and validate CLI arguments
(directory path, interval, receiver email)
  |
  v
Load sender credentials from .env
  |
  v
+-----------------------------------------------+
|         Scheduled loop  (every N minutes)      |
|                                                |
|   os.walk() --> collect all files              |
|         |                                      |
|         v                                      |
|   Compute MD5 checksum for each file           |
|         |                                      |
|         v                                      |
|   Group files by checksum                      |
|         |                                      |
|         v                                      |
|   Delete duplicates, keep first occurrence     |
|         |                                      |
|         v                                      |
|   Write timestamped .log file to Marvellous/   |
|         |                                      |
|         v                                      |
|   Send log via Gmail SMTP (SSL, port 465)      |
|         |                                      |
|         v                                      |
|   Wait N minutes, then repeat                  |
+-----------------------------------------------+
```

---

## Features

- **Recursive directory scanning** — traverses all subdirectories using `os.walk`
- **Checksum-based duplicate detection** — MD5 comparison on file content, not filename
- **Automatic deletion** — removes duplicates safely, preserves the first encountered copy
- **Timestamped log generation** — unique `.log` file per run with full scan statistics
- **Periodic scheduling** — configurable repeat interval via the `schedule` library
- **Email notification** — log report sent via Gmail SMTP SSL after every scan
- **Log file attachment** — the `.log` file is attached directly to the outgoing email
- **Input validation** — checks path existence, interval range, and email format before starting
- **Exception handling** — covers `ValueError`, `KeyboardInterrupt`, permission errors, and unexpected failures
- **Modular design** — three focused modules with clean separation of responsibilities

---

## Tech Stack

| Component | Tool |
|---|---|
| Language | Python 3.6+ |
| Duplicate detection | `hashlib` (MD5) |
| Scheduling | `schedule` |
| Email delivery | `smtplib` + `email.message.EmailMessage` |
| Credential management | `python-dotenv` |
| File system traversal | `os.walk` |
| Email validation | `re` (regex) |

---

## Project Structure

```
DuplicateFileRemovalAutomation/
|
+-- DuplicateFileRemoval.py     <- Entry point: argument parsing, validation, scheduler
+-- FileUtils.py                <- Core logic: scan, checksum, delete, log, email trigger
+-- MarvellousMailSender.py     <- Email utility: Gmail SMTP with log attachment
+-- .env                        <- Sender credentials (never commit this to Git)
+-- .gitignore
|
+-- Marvellous/                 <- Auto-created at runtime; stores all log files
    +-- DuplicateRemovalLog_DD_MM_YYYY_HH_MM_SS.log
    +-- DuplicateRemovalErrorLog_DD_MM_YYYY_HH_MM_SS.log
```

**DuplicateFileRemoval.py** — Main entry point. Loads `.env`, validates all three CLI arguments, retrieves sender credentials from environment variables, and sets up the scheduled job. Also triggers one immediate scan on startup so you don't wait for the first interval to pass.

**FileUtils.py** — The core of the system. Contains `FindDuplicates` (recursive scan and checksum grouping), `CalculateCheckSum` (buffered MD5 via `hashlib`), `SafelyDeleteFile` (pre-deletion checks followed by `os.remove`), `WriteLogReport` (structured log writing and email trigger), and `DeleteDuplicates` which orchestrates the full pipeline on every scheduled call.

**MarvellousMailSender.py** — A focused email utility. Builds an `EmailMessage` with the log content as the body and the `.log` file as an attachment, then connects to `smtp.gmail.com:465` over SSL and sends using the App Password.

**Marvellous/** — Created automatically on first run. Acts as the audit trail for every scan. Errors that occur during deletion or email delivery are written to a separate error log file, so the main scan log stays clean.

---

## Requirements

**Python version:** 3.6 or higher

**Install dependencies:**

```bash
pip install schedule python-dotenv
```

Standard library modules used (no installation needed): `smtplib`, `hashlib`, `os`, `sys`, `re`, `time`, `datetime`, `email`

**Other requirements:**

- Active internet connection for Gmail SMTP
- A Gmail account with 2-Step Verification enabled
- A Google App Password (16 characters) — the regular Gmail password will not work over SMTP

---

## Email Configuration

Credentials are stored in a `.env` file in the project root. This keeps them out of source code and out of version control.

**Step 1 — Create the `.env` file:**

```dotenv
SENDER_EMAIL="your.email@gmail.com"
SENDER_APP_PASSWORD="xxxx xxxx xxxx xxxx"
```

**Step 2 — Generate a Google App Password:**

Google blocks direct SMTP logins with the standard account password. You need a dedicated App Password instead.

1. Go to [myaccount.google.com](https://myaccount.google.com) and open **Security**
2. Enable **2-Step Verification** if it is not already active
3. Search for **App passwords** in the search bar
4. Select app: **Mail**, device: **Windows Computer**, then click **Generate**
5. Copy the 16-character password and paste it as `SENDER_APP_PASSWORD` in `.env`

Add `.env` to `.gitignore` immediately. Never push credentials to a public repository.

---

## Command-Line Options

**Normal execution requires exactly three arguments:**

| Argument | Type | Description |
|---|---|---|
| `DirectoryPath` | string | Absolute path to the directory to scan |
| `IntervalInMinutes` | integer | How often to repeat the scan (must be greater than 0) |
| `ReceiverEmailId` | string | Email address where the report will be sent |

**Info flags (pass one argument):**

```bash
# Brief description of the script
python DuplicateFileRemoval.py --help
python DuplicateFileRemoval.py --h

# Full syntax with example
python DuplicateFileRemoval.py --usage
python DuplicateFileRemoval.py --u
```

---

## Usage

**Syntax:**

```bash
python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmailId>
```

**Example:**

```bash
python DuplicateFileRemoval.py "E:/Data/Demo" 50 "marvellousinfosystem@gmail.com"
```

This command scans `E:/Data/Demo` immediately, deletes all duplicates while keeping one original per group, writes a log to `Marvellous/`, emails the report to the specified address, and then repeats the same process every 50 minutes.

To stop the script at any time, press `Ctrl + C`. It will print the stop timestamp and exit cleanly.

---

## Sample Output

Terminal output during a normal run:

```
----------------------------------------------------------------------
Duplicate File Removal Automation Script
----------------------------------------------------------------------
Process started at: Thu Jul 25 14:30:00 2025
Scheduling the duplicate file removal task...

[Email Success] Report sent successfully to marvellousinfosystem@gmail.com

^C
Stopping the scheduler. Exiting program...
Process stopped at: Thu Jul 25 16:10:42 2025
----------------------------------------------------------------------
Thank you For using Duplicate File Removal Automation
----------------------------------------------------------------------
```

Sample log file (`DuplicateRemovalLog_25_07_2025_14_30_00.log`):

```
Scan started at: Thu Jul 25 14:30:00 2025
Scan completed at: Thu Jul 25 14:30:03 2025
----------------------------------------------------------------------
Scanning and Deletion Report
----------------------------------------------------------------------
Directory Scanned: E:/Data/Demo
Total Files Scanned: 120
Total Duplicate files Found: 8
Total duplicate Files Deleted: 5
Complete paths of all deleted files:
  - E:/Data/Demo/reports/summary_copy.pdf
  - E:/Data/Demo/images/photo_backup.jpg
CheckSum values of duplicate files:
  - d41d8cd98f00b204e9800998ecf8427e
  - 9e107d9d372bb6826bd81d3542a419d8
Time Taken: 2.8431 seconds
----------------------------------------------------------------------
Email report sent successfully to marvellousinfosystem@gmail.com
```

---

## Log File Details

All logs are written to the `Marvellous/` directory, which is created automatically on the first run.

**Naming format:**

```
DuplicateRemovalLog_DD_MM_YYYY_HH_MM_SS.log
DuplicateRemovalErrorLog_DD_MM_YYYY_HH_MM_SS.log
```

**Scan log contains:**

- Scan start and end timestamps
- Directory path scanned
- Total files scanned
- Number of duplicate groups found and files deleted
- Full absolute paths of every deleted file
- MD5 checksums of all duplicate groups
- Total scan duration in seconds (4 decimal places)
- Email delivery confirmation

**Error log contains:**

- Permission denied errors at the file level
- Email send failures with timestamps
- File-not-found or invalid path errors encountered during deletion

---

## Important Notes

Read this section before pointing the script at any directory that contains data you care about.

**Deletion is permanent.** The script uses `os.remove()`, which does not send files to the Recycle Bin. Once deleted, they are gone.

**Test on a sample directory first.** Create a small folder with known duplicate files and run the script there before using it on real data.

**Never hard-code credentials.** Store them in `.env` and add that file to `.gitignore` before making the repository public.

**The first copy found is preserved.** The script keeps whichever copy `os.walk` encounters first for a given checksum. All subsequent matches are deleted. The traversal order depends on the file system.

**Duplicates are defined by content, not name.** Two files with the same name but different content are not duplicates. Only files with an identical MD5 hash are flagged.

**The interval must be a positive integer.** Passing zero or a negative number will cause the script to exit immediately with an error.

---

*Built with Python 3 using `hashlib`, `smtplib`, `schedule`, and `python-dotenv`.*
