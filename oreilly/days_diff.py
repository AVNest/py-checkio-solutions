from datetime import date

def days_diff(dt1, dt2):
    diff = date(*dt1) - date(*dt2)
    return abs(diff.days)

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
print('Good')
