import signal,time
# Define signal handler function
def myHandler(signum, frame):
    print("Now, it's the time")
    exit()

# register signal.SIGALRM's handler 
signal.signal(signal.SIGINT, myHandler)
while True:
    time.sleep(1)
    print('not yet')
