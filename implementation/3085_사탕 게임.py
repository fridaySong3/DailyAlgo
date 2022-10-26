# https://www.acmicpc.net/problem/1308
import sys

LAST_DATE = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LAST_DATE_LY = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_last_date(year):
    return LAST_DATE_LY if is_ly(year) else LAST_DATE

def is_ge(sy, sm, sd, ey, em, ed):
    return (sy < ey) or (sy == ey and sm < em) or (sy == ey and sm == em and sd <= ed)

def is_ly(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

sy, sm, sd = map(int, sys.stdin.readline().split())
ey, em, ed = map(int, sys.stdin.readline().split())

if is_ge(sy+1000, sm, sd, ey, em, ed):
    print("gg")
else:
    x = 0
    if sy == ey:
        if sm == em:
            x += ed - sd
        else:
            LD = get_last_date(sy)
            x += (LD[sm] - sd) + sum(LD[sm+1:em]) + ed
    else:        
        for y in range(sy + 1, ey):
            x += 366 if is_ly(y) else 365
        LD = get_last_date(sy)
        x += (LD[sm] - sd) + sum(LD[sm+1:])
        LD = get_last_date(ey)
        x += ed + sum(LD[:em])
    print("D-", x, sep="")
    