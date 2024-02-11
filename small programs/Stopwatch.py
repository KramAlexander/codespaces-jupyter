# import and global variables
import time
start_action = ""
end_action = None

# function for start_input
def start_input():
    global start_action
    start_action = input("Enter 'Start' to start the timer:\n")

# function for end_input
def end_input():
    global end_action
    end_action = input("Enter 'Stop' to stop the timer:\n")

# function for start_timer
def start_timer():
    start_time = time.time()
    return start_time

# function for end_timer
def end_timer():
    end_time = time.time()
    return end_time

# asking user to enter Start or start
while start_action != "Start" and start_action != "start": 
    start_input()

# starting timer
start_time = start_timer()

# asking user to enter Stop or stop
while end_action != "Stop" and end_action != "stop":
    end_input()

# ending timer
end_time = end_timer()

# calculating duration and printing it
duration = end_time - start_time
print(f"Duration: {int(duration)} seconds")