# APEXPointsFarmer

This script runs random SQL dummy queries from a text file on an APEX browser window to accumulate points on the "Top Users" board

## Usage

Oracle Academy Application Express has a "Top Users" leaderboard, where points are awarded for doing work on APEX. However, there are no limitations to how you receive those points. Running random SQL queries in a dummy table suffice for easy points gathering.

## Setup
You need PyAutoGui for this script to work. Install using:
```
python -m pip install pyautogui
```

Then clone this repository:
```
git clone https://github.com/StormFireFox1/APEXPointsFarmer.git
```

You will need to open your APEX on a browser window, and enter the "SQL Commands" section, where you can run all the dummy SQL queries, and maximize the browser
window to make sure all the space is used.

After setup, run the script:
```
python farmer.py
```

## Queries

The random queries run are saved in *queries.txt*. If you wish to customize the queries run at random, change the file and add one SQL query to run per line.