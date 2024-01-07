def mergeSortedArrays(arr1,arr2):
    ind1,ind2=0,0
    arr = []
    while(ind1 < len(arr1) and ind2 < len(arr2)):
        if arr1[ind1] < arr2[ind2]:
            arr.append(arr1[ind1])
            ind1+=1
        else:
            arr.append(arr2[ind2])
            ind2 += 1
    while(ind1 < len(arr1)):
        arr.append(arr1[ind1])
        ind1 +=1
    while (ind2 < len(arr2)):
        arr.append(arr2[ind2])
        ind2+=1
    return arr
if __name__ == '__main__':
    arr1,arr2=[0,3,4,31],[4,6,30]
    arr = mergeSortedArrays(arr1,arr2)
    print(arr)
