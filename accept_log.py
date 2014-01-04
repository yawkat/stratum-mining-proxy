import time

accepted_log = None

def setup(f):
    global accepted_log
    accepted_log = open(f, "a")

def accepted():
    accepted_log.write(time.strftime("%Y/%m/%d %H:%M:%S") + "\n")
    accepted_log.flush()
