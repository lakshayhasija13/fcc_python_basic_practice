distance_mi = 6
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if distance_mi == False or distance_mi == 0 or distance_mi == 0.0:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if not is_raining and has_bike:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)


# END
