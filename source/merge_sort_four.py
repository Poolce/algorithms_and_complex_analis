def _merge(first, second):
    res =[]
    i=0
    j=0
    while i < len(first) and j < len(second):
        if first[i]<second[j]:
            res.append(first[i])
            i+=1
        else:
            res.append(second[j])
            j+=1
    while i< len(first):
        res.append(first[i])
        i+=1
    while j<len(second):
        res.append(second[j])
        j+=1
    return res

def _bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if(array[i]>array[j]):
                a = array[i]
                array[i]=array[j]
                array[j] = a
    return array



def merge_sort(array):
    if(len(array)>4):
        first = array[0:len(array)//2]

        second = array[len(array)//2:len(array)]
        first = merge_sort(first)
        second = merge_sort(second)

        res = _merge(first,second)
        return res
    else:
        return _bubble_sort(array)