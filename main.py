import source.merge_sort_four as mg
import source.avl_tree.avl as avl
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer


avl_sort_n = []
avl_sort_time = []

merge_data_time = []
merge_data_n = []

#Создание списка
for i in range(0,1000,2):

    avl_a = avl.avl_tree()
    rt = None
    sorting_list_by_merge = []
    

    for j in range(i):
        rand = random.randint(-10000000,10000000)
        rt = avl_a.insert(rand,rt)
        sorting_list_by_merge.append(rand)


    print(i)
    #Сама сортировка на АВЛ
    start_timer = timer()
    avl_sorted_list = avl_a.sort_list_by_avl(rt)
    avl_sort_time.append(timer()-start_timer)
    avl_sort_n.append(i)


    #Сортировка слиянием
    start_timer = timer()
    merge_sorted_list = mg.merge_sort(sorting_list_by_merge)
    merge_data_time.append(timer()-start_timer)
    merge_data_n.append(i)

print(avl_sort_time,'t',avl_sort_n,'n')
plt.plot(merge_data_n,merge_data_time,'ro')
plt.plot(avl_sort_n,avl_sort_time,'b*')
plt.ylabel('some numbers')
plt.show()
