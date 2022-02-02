__all__ = (
    'even_odd',
)


def even_odd(arr):
    sum_chet = 0
    sum_nechet = 0
    res = 0
    i = 0
    if(not arr or type(arr) != list):
        return(0)
    while(i < len(arr)):
        if(arr[i]%2 == 0):
            sum_chet += arr[i]
        if(arr[i]%2 != 0 ):
            sum_nechet += arr[i]
        if(sum_nechet == 0):
            return(0)
        i += 1
    res = float(sum_chet / sum_nechet)
    return(res)
