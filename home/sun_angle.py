def sun_angle(time):
    minutes_per_hour = 60
    sunrise = 6 * minutes_per_hour
    sunset = 18 * minutes_per_hour
    sunset_angle = 180  
    sun_period = sunset - sunrise

    hours, minutes = map(int, time.split(':'))
    current_time = hours * minutes_per_hour + minutes

    if sunrise <= current_time <= sunset:
        rate = (current_time - sunrise) / sun_period
        return round(sunset_angle * rate, 2)
    
    return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
