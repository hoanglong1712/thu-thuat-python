# %%
import signal

def xu_ly_signal(signum, frame):
    raise Exception("Hết giờ!")

signal.signal(signal.SIGALRM, xu_ly_signal)
signal.alarm(10) # 10 giây

def ham():
    while True:
        pass
    pass

try:
    ham()
except Exception as ex:
    print(ex)




