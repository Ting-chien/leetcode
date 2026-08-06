# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from datetime import datetime, timedelta

def is_interesting(t: datetime) -> bool:
    """
    Args:
        t: datetime

    Return: If the time `t` is interesting (only contain up to two distinct digits)
    """
    # Turn datetime to string 
    t_str = t.strftime("%H:%M:%S")

    # Count appearance of digits
    digits = t_str.replace(":", "")
    counter = set()
    for d in digits:
        counter.add(d)

    # Check if interesting
    return len(counter) <= 2

def solution(S, T):
    # Implement your solution here

    # Step 1. Turn S & T from string to time and get difference in seconds
    dt_S = datetime.strptime(S, "%H:%M:%S")
    dt_T = datetime.strptime(T, "%H:%M:%S")
    diff = (dt_T - dt_S).total_seconds()

    # Step 2. For loop the time between S & T (inclusive) by second and check if 
    # it is interesting
    curr_dt = dt_S
    ans = 0
    for _ in range(int(diff)+1):
        
        # Check if it is interesting
        if is_interesting(t=curr_dt):
            ans += 1

        # Add one second to current datetime
        curr_dt = curr_dt + timedelta(seconds=1)

    return ans