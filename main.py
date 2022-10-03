import source.merge_sort_four as mg
import source.avl_tree.avl as avl
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer


avl_sort_n = []
avl_sort_time = []

merge_data_time = []
merge_data_n = []

merge_four_data_time = []
merge_four_data_n = []


#Создание списка
#for i in range(0,50000,1250):
for i in range(0,5000,125):
    print(i);
    #Создание списка для сортировки
    sorting_list = []
    
    #Заполнение списка
    for j in range(i):
        sorting_list.append(random.randint(-10000000,10000000))

    #Создание AVL-дерева
    avl_a = avl.avl_tree()
    rt = None

    #Таймер НАЧАЛО
    start_timer = timer()
    for i in range(i):
        avl_a.insert(sorting_list[i],rt)
    #Сама сортировка на АВЛ
    avl_sorted_list = avl_a.sort_list_by_avl(rt)
    avl_sort_time.append(timer()-start_timer)
    avl_sort_n.append(i)


    #Сортировка слиянием 4
    start_timer = timer()
    merge_sorted_list = mg.merge_sort_k(sorting_list,4)
    merge_four_data_time.append(timer()-start_timer)
    merge_four_data_n.append(i)

    #обычная сортировка слиянием
    start_timer = timer()
    merge_sorted_list = mg.merge_sort(sorting_list)
    merge_data_time.append(timer()-start_timer)
    merge_data_n.append(i)


#print(avl_sort_time,'t',avl_sort_n,'n')
plt.plot(merge_four_data_n,merge_four_data_time,'r*')
plt.plot(merge_data_n,merge_data_time,'g*')
plt.plot(avl_sort_n,avl_sort_time,'b*')
plt.ylabel('some numbers')
plt.show()
