print('Enter the all numbers at once but seperated by a space :\n ')
Array=input().split(' ')
def Insertion_Sort(Array):
    for i in range(0,len(Array)-1):
        for j in range(i+1,len(Array)):
            key=Array[i]
            if key>=Array[j]:
                Array[i]=Array[j]
                Array[j]=key
    return Array
            
print('Sorted Array :')
print(Insertion_Sort(Array))




