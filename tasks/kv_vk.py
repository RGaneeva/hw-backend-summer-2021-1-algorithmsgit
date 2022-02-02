from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(diction):
    d_res = {}
    key = []
    var = []
    if(not diction or type(diction) != dict):
        return(-1)
    temp = diction.copy()
    for i in temp.keys():
        key.append(temp[i])
    var = list(temp.keys())
    
    d_res = dict(zip(key, var))
    return(d_res)


def flip_kv_vk_safe(diction):
    d_res = {}
    key = []
    var = []
    var_temp = []
    if(not diction or type(diction) != dict):
        return(-1)
    temp = diction.copy()
    for i in temp.keys():
        key.append(temp[i])
    var = list(temp.keys())
    d_res = dict.fromkeys(key, var)
    
    return(d_res)
