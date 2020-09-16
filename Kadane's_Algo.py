print('Enter array : ')
A=input().split(' ')
A=list(map(int,A))
def Kadanes(A):
    curr_sum=A[0]
    maximum=A[0]
    for i in range(1,len(A)):
        curr_sum=max(curr_sum + A[i],A[i])
        maximum=max(maximum,curr_sum)
    return maximum

print('Max sum is :')
print(Kadanes(A))

       
        


        


