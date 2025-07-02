import time

print("Press Enter to start the lap timer.")
input()
start_time = time.time()
last_time = start_time
lap_num = 1

print("Press Enter to record a lap or 'q' to quit.\n")

while True:
    user_input = input()
    if user_input.lower() == 'q':
        break

    lap_time = round(time.time() - last_time, 2)
    total_time = round(time.time() - start_time, 2)

    print(f"Lap {lap_num}: {lap_time} sec (Total: {total_time} sec)")
    last_time = time.time()
    lap_num += 1
