def flatten(arr):
    """
    Input: arr -> list \n
    Output flattened_list -> list
    
    This function flattens the given list. Because the list has nested lists and non-scalar data, the function works recursively.
    """
    flattened_list = []
    for l in arr:
        print(f"listenin şu an dönen elemanı: {l}")
        if isinstance(l,list) :
            flattened_list.extend(flatten(l))
        else:
            flattened_list.append(l)
            
        
        print(f"Listenin şu ana kadar düzleşmiş hali: {flattened_list}")
    return flattened_list

def reverse(arr):
    """
    Input: arr -> list \n
    Output arr -> list
    
    This function reverses both the list and lists in the list
    """
    arr.sort(reverse=True)
    for i in arr:
        if isinstance(i,list):
            i.sort(reverse=True)    
    return arr
arr =  [[1, 2], [3, 4], [5, 6, 7]]
print(reverse(arr))