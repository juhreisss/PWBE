import time 

h = 0
m = 0
s = 0

while True:
    print(f"{h:02}:{m:02}:{s:02}", end='\r')
    time.sleep(1)
    s += 1
    if s == 60:
        s = 0 
        m += 1 
        if m == 60:
            m = 0 
            h += 1 
            if h == 24: 
                h = 0
