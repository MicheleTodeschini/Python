import time

def count(end, start=0):   #    DEFAULT ARGUMENT CAN ONLY STAY AFTER NON-DEFAULT ARGUMENT
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print('DONE!')

count(10, 5)