__all__ = (
    'is_prime',
)


def is_prime(number):
    if(not number or number <= 0 or type(number) != int):
        return(False)        
    new_num = number + 1
    for i in range(2,new_num):
        if(new_num%i == 0):
            return(True)
        else:
            return(False)
