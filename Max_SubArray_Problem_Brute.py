print('Enter Array :')
A=input().split(' ')
A=list(map(int,A))


def Max_SubArray(A):
    maximum=A[0]
    for i in range(0,len(A)):
        curr_sum=A[i]
        prev_sum=A[i]
        for j in range(i+1,len(A)):
            curr_sum=curr_sum+A[j]
            if curr_sum >= prev_sum and curr_sum >=maximum :
                maximum=curr_sum
            prev_sum=curr_sum
    return maximum

    

print('Max sum : ')
print(Max_SubArray(A))



            