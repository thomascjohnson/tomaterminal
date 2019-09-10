#!/usr/local/bin/python3
import time
import sys
import argparse
from numpy import floor

description_string = """Tomaterminal is a terminal program based on the Pomodoro
 (Italian for Tomato) method of working. In the Pomodoro method, you take a timer
 ((frequently tomato shaped) historically used in kitchens) and you set a 25 minute
 timer for work. After 25 mintues are completed, you set a 5 minute timer for break.
 Tomaterminal emulates this exact behavior, alerting you after 25 minutes have
 elapsed, then after your 5 minute break has elapsed."""

parser = argparse.ArgumentParser(description=description_string)
parser.add_argument('-t', '--task_time', type=int, help='Task Interval (minutes)', required=False)
parser.add_argument('-b', '--break_time', type=int, help='Break Interval (minutes)', required=False)
args = parser.parse_args()

# Time Definitions
seconds_minute = 60
minutes_hour = 60
hours_day = 24

intervals = 60

# Task Definitions
task_time = 25
break_time = 5

# Override task/break time if command line arguments passed
if args.task_time is not None:
    task_time = args.task_time
if args.break_time is not None:
    break_time = args.break_time

# UI Definitions
progress_bar_length = 80


def alert():
    print('\a')


def progress(count, total, suffix=''):
    filled_len = int(round(progress_bar_length * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (progress_bar_length - filled_len)
    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

def pomodoro(task_minutes: int, nintervals: int, message: str):
    progress(0, task_minutes, f"{message}: 00:00")
    for i in range(0, task_minutes):
        for j in range(0, nintervals):
            time.sleep(seconds_minute / intervals)
            t = i + j / intervals
            minutes = int(floor(t))
            seconds = int(60 * (t - minutes))
            suffix = f"{message}: {minutes:02d}:{seconds:02d}"
            progress(t, task_minutes, suffix)
    alert()

# Initial Entry into Program; Clear Screen
print(chr(27) + "[2J")
while True:
    # Task Loop
    pomodoro(task_time, intervals, "Time Elapsed")
    # Break Loop
    pomodoro(break_time, intervals, "Break Time Elapsed")
