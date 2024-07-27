for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            if seconds == 2:
                break
            print(hours, ':', minutes, ':', seconds)