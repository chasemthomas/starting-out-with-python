###############################################################################
# Starting out with Python, 4th Edition
# By Tony Gads
# Chapter 4 Programming Exercise 1, p. 203
##########
# A bug collector collects bugs every day for five days.
# Write a program that keeps a running total of the number of bugs collected
# during the five days.
# The loop should ask for the number of bugs collected for each day,
# and when the loop is finished, the program should display the total
# number of bugs collected.
###############################################################################

# integer variable to hold the running total
bug_total = 0
# for each day the bug collector works...
for day in range(5):
    repeat = True
    # Use a while-loop to handle input errors
    while(repeat):
        try:
            #ask how many bugs they caught, and save it to a variable
            userInput = int(input('\nNumber of bugs caught today: '))
            # verify number is not negative. Break loop if positive
            if userInput < 0:
                print("\nError. Please enter a positive number.")
            else:
                # If user entry valid add to total and break loop
                bug_total += userInput
                repeat = False
        # if user didn't enter a interger, display error and loop again
        except:
            print("\nError. Please enter a positive number.")

# print the total number of bugs caught after 5 days
print('\nYou caught ' + str(bug_total) + ' bugs.\n')
