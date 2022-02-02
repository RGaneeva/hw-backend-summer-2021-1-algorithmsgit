from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text):
    if(type(text) != str):
        return(-1)
    i = 0
    temp = []
    text = text.strip()
    if(text == ''):
        biggest = None
        smallest = None
    if(text):     
        while(i < len(text)):
            if(text[i] == ' ' or text[i] == '\n' or text[i] == '\t' \
               or text[i] == '\v'):
                one_str = text[0:i]
                temp.append(one_str)
                text = text[i+1:]
            i += 1
        one_str = text
        temp.append(one_str)
        biggest = max(temp, key=len)
        smallest = min(temp, key=len)    
    cort = (smallest, biggest)
    return(cort)
