def QuickSort(list, start=0, last=None):
    # PIVOT = ultimo da lista
    if last == None:
        last = len(list)-1
    if start < last:
        pivot = divide_array(list, start, last)
        QuickSort(list, start, pivot-1)  # esquerda
        QuickSort(list, pivot+1, last)  # direita


def divide_array(list, start=0, last=None):
    if last == None:
        last = len(list)-1
    pivot = list[last]
    indice = start
    for analisyng in range(start, last):
        if list[analisyng] <= pivot:
            list[analisyng], list[indice] = list[indice], list[analisyng]
            indice += 1
    list[indice], list[last] = list[last], list[indice]
    return indice
