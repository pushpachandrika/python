def calculate_average(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)
numbers = list(map(int,input("enter the elements seperated by space:").split()))
print(calculate_average(numbers))



def calculate_average(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)
numbers = list(map(int,input("enter the elements seperated by space:").split()))
print(calculate_average(numbers))



def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
numbers =list(map(int,input("enter array values in between spaces:").split()))
target =int(input("enter the target number:"))
index = find_index(numbers, target)

if index != -1:
    print("Index of target number: ",{index})
else:
    print("Index of target not found in the array")




    def contains_value(arr, target):
        for item in arr:
            if item == target:
                return True
        return False
    numbers = list(map(int, input("enter the elements seperated by space:").split()))
    print(numbers)
    target = int(input("enter the target:"))
    if contains_value(numbers, target):
        print(f"Element {target} exists in the array")
    else:
        print(f"Element {target} does not exist in the array")



def remove_element(arr, target):
    return [item for item in arr if item != target]
numbers = list(map(int,input("enter the elements seperated by space:").split()))
target = int(input("enter the target:"))
new_num = remove_element(numbers, target)
print("Updated array:", new_num)



def copy_array(arr):
    return arr[:]
original = list(map(int,input("enter the elements seperated by space:").split()))
copy = copy_array(original)
print("Original array:", original)
print("Copied array:", copy)



def insert_element(arr, item, position):
    arr.insert(position, item)
numbers = list(map(int,input("enter the elements seperated by space:").split()))
insert_element(numbers, 25, 5)
print("Updated array:", numbers)



def find_min_max(arr):
    if not arr:
        return None, None
    return min(arr), max(arr)
numbers = list(map(int,input("enter the elements seperated by space:").split()))
minimum, maximum = find_min_max(numbers)
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")



def reverse_array(arr):
    return arr[::-1]
numbers = list(map(int,input("enter the elements seperated by space:").split()))
reversed_numbers = reverse_array(numbers)
print("Original array:", numbers)
print("Reversed array:", reversed_numbers)


def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
numbers = list(map(int,input("enter the elements seperated by space:").split()))
duplicates = find_duplicates(numbers)
print("Duplicate values:", duplicates)

def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))
array1 = list(map(int,input("enter the elements seperated by space:").split()))
array2 = list(map(int,input("enter the elements seperated by space:").split()))
common_values = find_common_values(array1, array2)
print("Common values:", common_values)



def remove_duplicates(arr):
    return list(set(arr))
numbers = list(map(int,input("enter the elements seperated by space:").split()))
unique_numbers = remove_duplicates(numbers)
print("Array without duplicates:", unique_numbers)



def second_largest_loop(arr):
    if len(arr) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
numbers = list(map(int,input("enter the elements seperated by space:").split()))
print("Second largest number:", second_largest_loop(numbers))



def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
numbers = list(map(int,input("enter the elements seperated by space:").split()))
even, odd = count_even_odd(numbers)
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")