# Oracle Academy Points Farmer
#
# Farms points for Oracle Academy Application Express by spamming SELECT DUAL SQL Queries.
#
# @StormFireFox1, 2018, MIT License

import pyautogui as gui
import random as rng
import time

print("APEXPointsFarmer v1.0 -- @StormFireFox1")
gui.FAILSAFE = True # Make sure entire thing can be stopped easily by moving the nouse in the top corner

# We need to get the queries from our text file. We assume each query is one per line, so let's go with that.
queryFile = open("queries.txt", "r")

# List that contains all the queries we're gonna run randomly, to make sure we trip any sort of spam prevention. Expand list in queries.txt.
# Give some time to the user to arrange windows around as well.
queries = queryFile.readlines()
print('Query file opened! Move to APEX "SQL Commands" section, script starts in 5 seconds...')
time.sleep(5)
print('Script running! Press Ctrl-C to cancel.')

# First off, we assume we have the browser window open. We select the textbox for "SQL Commands", make sure the whole thing works. Most screens I'll use this on have
# around 1080p, so let's just take a few hundred pixels down from the center of the screen.
gui.moveTo(960, 300, duration=0.1)
gui.click()

# Make sure we add variable for previous index to check code so we do not type same query twice, which won't register with points
previousIndex = rng.randint(0, len(queries - 1))

# Now we run a "while loop", and run a random query every time
while (True):
    randomIndex = rng.randint(0, len(queries) - 1)
    if (randomIndex == previousIndex):
        continue
    previousIndex = randomIndex
    gui.typewrite(queries[randomIndex], interval=0.01) # type query
    time.sleep(0.1)
    gui.hotkey('ctrl', 'enter') # run query
    time.sleep(5)
    gui.hotkey('ctrl', 'a') # delete previous query by selecting all of it
    time.sleep(0.1)
    gui.press('backspace')
# No need to exit loop, either we cancel with KeyboardInterrupt, or we Failsafe out of the program