def remove_multiple_element():

    print("Remove multiple element from list\n")
    user_input = input("Enter list elements separeted by space: ")
    orginal_list = list(map(int, user_input.split()))

    remove_input = input("Enter elements to remove separeted by space: ")
    to_remove = list(map(int, remove_input.split()))

    updated_list = [item for item in orginal_list if item not in to_remove]
    print("Updated list: ",updated_list)

remove_multiple_element()