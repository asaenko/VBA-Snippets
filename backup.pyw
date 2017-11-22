'''
File for backing up translation memories from their shared folder
If the folder is unavailable, the script sleeps for 15 minutes
TODO: add logging and make invisible (pyw)
'''
#!/usr/bin/env python3

import datetime
import glob
import logging
import os
import pickle
import shutil
import sys
import time


TMPATH = r'\\elena\Elena\база ТМ' # path to TM files
STAMPFILE = 'time.stamp'
d = datetime.timedelta(days=5) # backup each five days

# logging setup
logger = logging.getLogger('backup')
hdlr = logging.FileHandler('backup.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

# get date
curdate = datetime.date.today()

# processing time stamp file
if os.path.exists(STAMPFILE):
    with open(STAMPFILE, 'rb') as stampfile:
        pastdate = pickle.load(stampfile) # read date from file
else:
    pastdate = curdate
    with open('time.stamp', 'wb') as stampfile:
        pickle.dump(pastdate, stampfile)

# checking if five days have passed since last backup and acting
if (pastdate+d) >= curdate:
    logger.info("Five days have not elapsed")
    sys.exit(0)
else:
    with open('backup.log', 'w'):
        pass # clear the log
        
    while True:
        if os.path.isdir(TMPATH): # if network path exists
            # let the bloody typewriter boot or it may choke
            time.sleep(900)
            # copy txt files
            for filo in glob.glob(TMPATH+'\\*.txt'):
                shutil.copy(filo, os.path.basename(filo))
                logger.info("Copied {}".format(filo))
            # save current date
            with open('time.stamp', 'wb') as stampfile:
                pickle.dump(curdate, stampfile)
            sys.exit(0)
        else:
            logger.info("Sleeping 15 minutes")
            time.sleep(900)
