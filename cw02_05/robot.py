import math
up_down = 0
left_right = 0
active = True

while active:
    command = input("Wprowadź kierunek N/S/W/E oraz odległość jaką ma przejść robot\n"
                    "Wciśnij ENTER, aby wyjść: ")
    if command:
        direct, distance = command[0].lower(), int(command[2:])

        match direct:
            case 'n': up_down += distance
            case 's': up_down -= distance
            case 'w': left_right += distance
            case 'e': left_right -= distance
            case other: continue
        print(f"Robot jest na pozycji ({up_down},{left_right})")
    else:
        active = False

distance_center = round(math.hypot(up_down, left_right), 1)
print(f"Odległość robota od środka wynosi: {distance_center}")