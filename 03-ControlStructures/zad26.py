car_speed = float(input("Enter car speed: "))

speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!")
else:
    print("Car speed is valid.")