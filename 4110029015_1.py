def bubble_sort(arr:list):
    # Done this function
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp    
    return arr
arr = [10,20,3,7,9,53]
print(bubble_sort(arr))
# Time complexity : O(n²)