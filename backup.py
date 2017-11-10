'''
File for backing up translation memories from their shared folder
If the folder is unavailable, the script sleeps for 15 minutes
TODO: add logging and make invisible (pyw)
'''
#!/usr/bin/env python3

import datetime
import glob
import os
import pickle
import shutil
import sys
import time

TMPATH = r'\\elena\Elena\база ТМ'
STAMPFILE = 'time.stamp'
d = datetime.timedelta(days=5)

while True:
    if os.path.isdir(TMPATH):
        curdate = datetime.date.today()
        if os.path.exists(STAMPFILE):
            with open(STAMPFILE, 'rb') as stampfile:
                pastdate = pickle.load(stampfile)
        else:
            pastdate = curdate
        if (pastdate+d) >= curdate:
            sys.exit(0) # five days have not passed
        else:
            for filo in glob.glob(TMPATH+'\\*.txt'):
                shutil.copy(filo, os.path.basename(filo))
                with open('time.stamp', 'wb') as stampfile:
                    pickle.dump(curdate, stampfile)
             sys.exit(0)
    else:
        print('Sleeping 15 minutes')
        time.sleep(54000)
