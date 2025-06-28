from time import time

running = False
start_time = 0
elapsed = 0 

def start_stop():
    global running, start_time, elapsed
    if not running:
        running = True
        start_time = time()
        return elapsed
    else:
        running = False
        elapsed += (time() - start_time)
        return elapsed

def get_time():
    global running, start_time, elapsed
    if running:
        return elapsed + (time() - start_time)
    else:
        return elapsed
    


running2 = False
start_time2 = 0
elapsed2 = 0 

def start_stop2():
    global running2, start_time2, elapsed2
    if not running2:
        running2 = True
        start_time2 = time()
        return elapsed2
    else:
        running2 = False
        elapsed2 += (time() - start_time2)
        return elapsed2

def get_time2():
    if running2:
        return elapsed2 + (time() - start_time2)
    else:
        return elapsed2
    
def get_time3():
    if running2:
        return (time() - start_time2)
