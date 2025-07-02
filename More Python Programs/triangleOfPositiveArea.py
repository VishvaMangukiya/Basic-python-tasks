def is_valid_triangle(angle1, angle2, angle3):
    return (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3 == 180)

angles = list(map(int, input("Enter three angles separated by spaces: ").split()))
if len(angles) != 3:
    print("Please enter exactly three angles")
else:
    if is_valid_triangle(angles[0], angles[1], angles[2]):
        print("Yes, these angles can form a valid triangle with positive area")
    else:
        print("No, these angles cannot form a valid triangle with positive area")