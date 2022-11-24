''' Start counting down from 10 to 0. Display every number in different line. 
    At the end print "Countdown is OVER!" '''

n = 10

print("\nStarting to countdown from 10 to 0.\n")
while n >= 0:
    # display every number in different line, put dot between numbers to look fancy :)
    print(f"{n}\n.")
    n -= 1
    if n < 0:
        print("Countdown is OVER!\n")