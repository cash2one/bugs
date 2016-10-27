# -*- coding: utf-8 -*-

def left_sort_list(lsta,lstb):
    if len(lsta) <> len(lstb):
        return
        
    for i in range(len(lsta)):
        if i == 0:
            continue

        if lsta[i] <= lsta[i-1] and lstb[i] >= lstb[i-1]:
            if i+1 < len(lsta):
                lsta[i+1] = max(lsta[i],lsta[i+1])
                lstb[i+1] = max(lstb[i],lstb[i+1])

            del lsta[i]
            del lstb[i]
            return left_sort_list(lsta,lstb)
    pass

def right_sort_list(lsta,lstb):
    if len(lsta) <> len(lstb):
        return
        
    for i in range(len(lsta)):
        if i+1>=len(lsta):
            break

        if lsta[i] <= lsta[i+1] and lstb[i] >= lstb[i+1]:
            if i+1 < len(lsta):
                lsta[i+1] = max(lsta[i],lsta[i+1])
                lstb[i+1] = max(lstb[i],lstb[i+1])

            del lsta[i]
            del lstb[i]
            return right_sort_list(lsta,lstb)
    pass

a = [10,12,11,30,31]
b = [5,6,7,13,12]

left_sort_list(a,b)
print a
print b

right_sort_list(a,b)
print a
print b
