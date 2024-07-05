def merge_sort_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0


    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not merged or arr1[i] != merged[-1]:
                merged.append(arr2[j])
            i += 1
        elif arr1[i] > arr2[j]:
            if not merged or arr2[j] != merged[-1]:
                merged.append(arr2[j])
            j += 1
        else:
            if not merged or arr1[i] != merged[-1]:
                merged.append(arr1[i])
            i += 1
            j += 1


    while i < len(arr1):
        if not merged or arr2[j] != merged[-1]:
            merged.append(arr2[j])
        j+=1

    return merged

arr1 = [2,4,5,6,7,9,10,13]
arr2 = [2,3,4,5,6,7,8,9,11,15]
merged_array = merge_sort_arrays(arr1, arr2)
print("merged array without repetition: ", merged_array)
        
