# Version & information: wolf.log ver 1.0 November 15, 2021
# Last updated: November 15, 2021
# python 3.9
# Alpwuf

# Imports
import datetime

# Config

# Set path for main log
path = None
# Set True to enable backup
backup = None
# Set backup path
backup_path = None


def log(text):
    
    # Get time
    time = datetime.datetime.now()
    log_time = f"[{time:%Y-%m-%d@%H:%M:%S}]"
    
    # Complete log
    log_write = log_time + " " + str(text) + "\n"
    
    # Open and write log
    if path is not None:
        main_path = str(path)

    else:
        main_path = ""

    main_path_fnl = main_path + "wolf.log"
    file = open(main_path_fnl, "a")
    file.write(log_write)
    file.close()

    if backup_path is not None:
        pathway = str(backup_path)

    else:
        pathway = ""
        
    # Write backup log if True
    if backup:
        path_fnl = pathway + "backup.log"
        file_bk = open(path_fnl, "a")
        file_bk.write(log_write)
        file_bk.close()


def log_io(Input, Output):
    
    # Get time
    time = datetime.datetime.now()
    log_time = f"[{time:%Y-%m-%d@%H:%M:%S}]"
    
    # Complete log
    log_write = log_time + " " + "<IN> " + Input + " " + "<OUT> " + Output + "\n"
    
    # Open and write log
    if path is not None:
        main_path = str(path)

    else:
        main_path = ""

    main_path_fnl = main_path + "wolf.log"
    file = open(main_path_fnl, "a")
    file.write(log_write)
    file.close()

    if backup_path is not None:
        pathway = str(backup_path)

    else:
        pathway = ""
        
    # Write backup log if True
    if backup:
        path_fnl = pathway + "backup.log"
        file_bk = open(path_fnl, "a")
        file_bk.write(log_write)
        file_bk.close()


def daily_log(text):
    
    # Get time
    time = datetime.datetime.now()
    log_time = f"[{time:%Y-%m-%d@%H:%M:%S}]"
    log_name = f"{time:%Y-%m-%d}.log"
    backup_name = f"{time:%Y-%m-%d}_bk.log"
    
    # Complete log
    log_write = log_time + " " + str(text) + "\n"
    
    # Open and write log
    if path is not None:
        main_path = str(path)

    else:
        main_path = ""

    main_path_fnl = main_path + log_name
    file = open(main_path_fnl, "a")
    file.write(log_write)
    file.close()

    if backup_path is not None:
        pathway = str(backup_path)

    else:
        pathway = ""
        
    if backup:
        path_fnl = pathway + backup_name
        file_bk = open(path_fnl, "a")
        file_bk.write(log_write)
        file_bk.close()


def daily_log_io(Input, Output):
    
    # Get time
    time = datetime.datetime.now()
    log_time = f"[{time:%Y-%m-%d@%H:%M:%S}]"
    log_name = f"{time:%Y-%m-%d}.log"
    backup_name = f"{time:%Y-%m-%d}_bk.log"
    
    # Complete log
    log_write = log_time + " " + "<IN> " + Input + " " + "<OUT> " + Output + "\n"
    
    # Open and write log
    if path is not None:
        main_path = str(path)

    else:
        main_path = ""

    main_path_fnl = main_path + log_name
    file = open(main_path_fnl, "a")
    file.write(log_write)
    file.close()

    if backup_path is not None:
        pathway = str(backup_path)

    else:
        pathway = ""
        
    if backup:
        path_fnl = pathway + backup_name
        file_bk = open(path_fnl, "a")
        file_bk.write(log_write)
        file_bk.close()


def monthly_log(text):
    
    # Get time
    time = datetime.datetime.now()
    log_time = f"[{time:%Y-%m-%d@%H:%M:%S}]"
    log_name = f"{time:%Y-%m}.log"
    backup_name = f"{time:%Y-%m}_bk.log"
    
    # Complete log
    log_write = log_time + " " + str(text) + "\n"
    
    # Open and write log
    if path is not None:
        main_path = str(path)

    else:
        main_path = ""

    main_path_fnl = main_path + log_name
    file = open(main_path_fnl, "a")
    file.write(log_write)
    file.close()

    if backup_path is not None:
        pathway = str(backup_path)

    else:
        pathway = ""
        
    if backup:
        path_fnl = pathway + backup_name
        file_bk = open(path_fnl, "a")
        file_bk.write(log_write)
        file_bk.close()


def monthly_log_io(Input, Output):
    
    # Get time
    time = datetime.datetime.now()
    log_time = f"[{time:%Y-%m-%d@%H:%M:%S}]"
    log_name = f"{time:%Y-%m}.log"
    backup_name = f"{time:%Y-%m}_bk.log"
    
    # Complete log
    log_write = log_time + " " + "<IN> " + Input + " " + "<OUT> " + Output + "\n"
    
    # Open and write log
    if path is not None:
        main_path = str(path)

    else:
        main_path = ""

    main_path_fnl = main_path + log_name
    file = open(main_path_fnl, "a")
    file.write(log_write)
    file.close()

    if backup_path is not None:
        pathway = str(backup_path)

    else:
        pathway = ""
        
    if backup:
        path_fnl = pathway + backup_name
        file_bk = open(path_fnl, "a")
        file_bk.write(log_write)
        file_bk.close()
