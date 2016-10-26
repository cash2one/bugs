# -*- coding: utf-8 -*-

def left_sort_list(lsta,lstb):   
    for i in range(len(lsta)):
        if i == 0:
            continue
        
        if lsta[i] <= lsta[i-1] and lstb[i] >= lstb[i-1]:
            # if i+1 < len(lsta):
                # lstb[i+1] = lstb[i]
                             
            del lsta[i]
            del lstb[i]
            return left_sort_list(lsta,lstb)
    pass

def right_sort_list(lsta,lstb):
    lsta.reverse()
    lstb.reverse()    
    left_sort_list(lsta,lstb)
    lsta.reverse()
    lstb.reverse()   
    pass
    
a = [10,12,20,30,31]
b = [5,7,11,13,12]
left_sort_list(a,b)
print a
print b

right_sort_list(a,b)
print a
print b
