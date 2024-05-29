
#funcion de ordenamiento quick sort
def quick_sort(array):
    #funcion de ordenamiento quick sort con parametros de entrada array 
    #low y high para los indices de la lista
    def _quick_sort(array, low, high):
        #si el indice low es menor a high
        if low < high:
            #se obtiene el indice de particion
            pi = particion(array, low, high)
            _quick_sort(array, low, pi - 1)
            _quick_sort(array, pi + 1, high)
    #funcion de particion con parametros de entrada array, low y high
    def particion(array, low, high):
        pivot = array[high]
        i = low - 1
        #se recorre el array desde low hasta high
        for j in range(low, high):
            #si el valor en la posicion j es menor o igual al pivote
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        #se retorna el indice i + 1
        return i + 1
    #se llama a la funcion _quick_sort con los parametros array, 0 y len(array) - 1
    _quick_sort(array, 0, len(array) - 1)

#funcion principal
if __name__ == "__main__":
    arr = [0, 4, 6, 2, 5, 9, 5, 10, 8,]
    print("original:", arr)
    quick_sort(arr)
    print("ordenado:", arr)

    arr2 = [1, 2, 7, 6, 10, 4, 9, 5]
    print("original:", arr2)
    quick_sort(arr2)
    print("ordenado:", arr2)
