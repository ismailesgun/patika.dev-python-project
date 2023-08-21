def flatten(arr):
    """
    Input: arr -> list \n
    Output flattened_list -> list
    
    This function flattens the given list. Because the list has nested lists and non-scalar data, the function works recursively.
    """
    flattened_list = []
    for l in arr:
        if isinstance(l,list) :
            flattened_list.extend(flatten(l))  # if the current element is a nested list
        else:
            flattened_list.append(l)
            
    return flattened_list

def reverse(arr):
    """
    Input: arr -> list \n
    Output arr -> list
    
    This function reverses both the list and lists in the list
    """
    arr.sort(reverse=True) # Reverse the array
    for i in arr:
        if isinstance(i,list): # if the array has lists , it reverses the lists, too
            i.sort(reverse=True)    
    return arr
arr =  [[1, 2], [3, 4], [5, 6, 7]]
print(reverse(arr))
