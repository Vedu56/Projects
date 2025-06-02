import random

def creating_list(user_lower, user_upper, count):
    
    list_numbers = []

    for i in range(count):

        list_items = random.randint(user_lower, user_upper)
        list_numbers.append(list_items)

    return list_numbers

def sorting_list(arr):

    for i in range(1, len(arr)):
        g = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > g:

            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = g

    return arr

user_lower = int(input("Enter the lower bound: "))
user_upper = int(input("Enter the upper bound: "))

user_Choice = int(input("Enter how many item you want to add to the list: "))

unsorted_list = creating_list(user_lower, user_upper, user_Choice)
print(f"Unsorted list: {unsorted_list}")

sorted_list = sorting_list(unsorted_list)
print(f"Sorted list: {sorted_list}")


    

   


