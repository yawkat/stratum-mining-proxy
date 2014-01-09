import time
import calendar

last_share_time = 0
last_share_bin_count = 0
accepted_log = None
bin_size = 60

def setup(f):
    global accepted_log
    accepted_log = open(f, "a")

def accepted():
    ctime = calendar.timegm(time.gmtime())
    ctime = ctime - (ctime % bin_size)
    if not ctime is last_share_time:
        _flush_time(ctime)
    global last_share_time
    last_share_time = ctime
    global last_share_bin_count
    last_share_bin_count = last_share_bin_count + 1

def _flush_time(new):
    if last_share_time is 0:
        return
    for i in range(last_share_time, new, bin_size):
        accepted_log.write(str(i) + "\t" + str(last_share_bin_count) + "\n")
        accepted_log.flush()
        global last_share_bin_count
        last_share_bin_count = 0
    global last_share_time
    last_share_time = 0
