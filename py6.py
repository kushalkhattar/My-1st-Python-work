speed_limit = 80

vehicle_speed = float(input("Enter vehicle speed (km/h): "))

if vehicle_speed > speed_limit:
    print(f"Vehicle exceeds speed limit! Speed: {vehicle_speed} km/h, Limit: {speed_limit} km/h")
else:
    print(f"Vehicle is within speed limit. Speed: {vehicle_speed} km/h, Limit: {speed_limit} km/h")
