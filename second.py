def binary_search_upper_bound(arr, x):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] >= x:
            upper_bound = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    
    return (iterations, upper_bound)

 
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5]
value_to_find = 2.0

result = binary_search_upper_bound(sorted_array, value_to_find)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")   
