class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

def ShortestSubArray(head):
    nums=dict()
    temp=head
    if not temp:
        return 0
    index=0
    degree=0
    while temp:
        num=temp.val
        if num in nums.keys():
            nums[num]=[nums[num][0],index,nums[num][2]+1]
            degree=max(degree,nums[num][2])
        else:
            nums[num]=[index,index,1]
            if degree==0:
                degree=1
        index+=1
    res=index
    for num in nums.keys():
        if nums[num][2]==degree:
            res=min(res,nums[num][1]-nums[num][0]+1)
    return res