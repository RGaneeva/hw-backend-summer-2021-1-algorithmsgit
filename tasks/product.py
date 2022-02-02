from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1, arr2):
    if(not arr1 or not arr2):
        return(-1)
    if(type(arr1) != list or type(arr2) != list):
        return(-1)
    new_arr = []
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            temp = (arr1[i], arr2[j])
            new_arr.append(temp)
    return(new_arr)
