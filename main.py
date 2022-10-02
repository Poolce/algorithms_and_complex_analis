from heapq import merge
import source.merge_sort_four as mg
import source.avl_tree.avl as avl
import random

#Создание списка
for i in range(100,10000,100):
    
    avl_a = avl.avl_tree()
    rt = None

    sorting_list_by_merge = []
    for j in range(i):
        rand = random.randint(100,1000)
        rt = avl_a.insert(rand,rt)
        sorting_list_by_merge.append(rand)


    print(i/100)
    #Сама сортировка на АВЛ
    #avl_sorted_list = avl_a.sort_list_by_avl(rt)

    #Сортировка слиянием
    merge_sorted_list = mg.merge_sort(sorting_list_by_merge)
