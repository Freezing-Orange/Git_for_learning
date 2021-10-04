def Sort(A):
    A=A
    length=len(A)
    if length<2:
        return A
    flag=0
    for i in range(1,length):
        if A[i-1]>A[i]:
            if flag==0:
                # find the misplaced element which A[i]>A[i+1]
                misIndex1=i-1
                flag=1
            else:
                # find the misplaced element which A[i]<A[i-1]
                misIndex2=i
                flag=2
                break
    if flag==2:
        # the misplaced elements are not near each other
        A[misIndex1],A[misIndex2]=A[misIndex2],A[misIndex1]
    elif flag==1:
        # the misplaced elements are near each other
        A[misIndex1],A[misIndex1+1]=A[misIndex1+1],A[misIndex1]
    return A

def test(val):
    for i in val:
        print(Sort(i))

val=[[1,12,23,45,989],
[1,456,64,576,789],
[14,56,78,90,123,234,789,456,567,345]
]

test(val)