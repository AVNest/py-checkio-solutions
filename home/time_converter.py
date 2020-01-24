def time_converter(time):
    noon = 12
    hours, minutes = map(int, time.split(':'))
    
    postfix = 'p.m.' if hours >= noon else 'a.m.'
    converted_hours = hours
    if hours == 0:
        converted_hours = noon
    elif hours > noon:
        converted_hours = hours - noon
    
    return f'{converted_hours}:{minutes:02d} {postfix}'


assert time_converter('12:30') == '12:30 p.m.'
assert time_converter('09:00') == '9:00 a.m.'
assert time_converter('23:15') == '11:15 p.m.'
assert time_converter('00:00') == '12:00 a.m.'


