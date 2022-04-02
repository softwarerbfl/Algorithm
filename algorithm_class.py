a=[10,1,3,4,5,7,2,9,6,11,8]
def difference_max(array):
    leng=len(array)
    for i in range(0,leng-1):
        for j in range(i,leng):
            if array[i]>array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    return array[:leng//2], array[leng//2:]
print(difference_max(a))