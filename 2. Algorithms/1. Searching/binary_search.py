array = [11,13,15,17,29,31,40,41]
array1 = [11,13,15,17,29,31,40,41,55]
    
    
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_in_details(arr, target):
    left = 0
    right = len(arr) - 1
    
    print("Array Length:", len(arr))
    print(f"First Value of index {left}:", arr[left])
    print(f"Last Value of index {right}:", arr[right])
    print("---")
    
    while left <= right:
        mid = (left + right) // 2
        print(f"Mid Value of index {mid}:", arr[mid])

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
            print(f"Mid value smaller than {target}, checking from left index of {left} to {right}")
            print(f"Checking Mid index of {left} + {right} = {(left + right) // 2}")
            print("---")
        else:
            right = mid - 1
            print(f"Mid value larger than {target}, checking from left index of {left} to {right}")
            print(f"Checking Mid index of {left} + {right} = {(left + right) // 2}")
            print("---")

    return -1


binary_search_in_details(array1, 17)
"""
Array Length: 9
First Value of index 0: 11
Last Value of index 8: 55
---
Mid Value of index 4: 29
Mid value larger than 17, checking from left index of 0 to 3
Checking Mid index of 0 + 3 = 1
---
Mid Value of index 1: 13
Mid value smaller than 17, checking from left index of 2 to 3
Checking Mid index of 2 + 3 = 2
---
Mid Value of index 2: 15
Mid value smaller than 17, checking from left index of 3 to 3
Checking Mid index of 3 + 3 = 3
---
Mid Value of index 3: 17
"""

binary_search_in_details(array1, 15)
"""
Array Length: 9
First Value of index 0: 11
Last Value of index 8: 55
---
Mid Value of index 4: 29
Mid value larger than 15, checking from left index of 0 to 3
Checking Mid index of 0 + 3 = 1
---
Mid Value of index 1: 13
Mid value smaller than 15, checking from left index of 2 to 3
Checking Mid index of 2 + 3 = 2
---
Mid Value of index 2: 15
"""

