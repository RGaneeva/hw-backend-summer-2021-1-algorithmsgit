from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1, arr2):
    if(not arr1 or not arr2):
        return(-1)
    if(type(arr1) != list or type(arr2) != list):
        return(-1)
    new_arr = []
    if (len(arr1) > len(arr2)):
        len_min = len(arr2)
    else:
        len_min = len(arr1)
    for i in range(0, len_min):
        temp = (arr1[i], arr2[i])
        new_arr.append(temp)
    return (new_arr)
