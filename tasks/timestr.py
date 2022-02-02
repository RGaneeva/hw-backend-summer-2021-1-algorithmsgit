__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds):
    if(not seconds or seconds < 0 or type(seconds) != int):
        return(-1) 
    if (seconds < 60):
        return(str(seconds)+'s')
    elif(seconds >= 60 and seconds < 3600):
        return(str(seconds//60)+'m'+str(seconds%60)+'s')
    elif(seconds >= 3600 and seconds < 86400):
        return(str(seconds//60//60)+'h'+str(seconds//60%60)+'m'+str(seconds%60)+'s')
    elif(seconds >= 86400):
        hours = (seconds-86400*(seconds//86400))//3600
        return(str(seconds//86400)+'d'+str(hours)+'h'+str(seconds//60%60)+'m'+str(seconds%60)+'s')
    else:
        return(-1)




