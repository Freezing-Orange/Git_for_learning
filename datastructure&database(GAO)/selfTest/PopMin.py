class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class stack:
    def __init__(self):
        self.top=None
        self.length=0
    def push(self,val):
        newTop=node(val,self.top)
        self.top=newTop
        self.length+=1
    def pop(self):
        res=self.top.val
        newTop=self.top.next
        del self.top
        self.top=newTop
        self.length-=1
        return res
    def top(self):
        return self.top
    def isEmpty(self):
        return True if self.length==0 else False

def PopMin(s):
    if s.isEmpty():
        return None
    helper=stack()
    minElement=s.pop()
    helper.push(minElement)
    count=1
    while not s.isEmpty():
        temp=s.pop()
        helper.push(temp)
        if temp<minElement:
            minElement=temp
            count=1
        elif temp==minElement:
            count+=1
    while helper.isEmpty():
        temp=helper.pop()
        if temp!=minElement:
            s.push(temp)
        else:
            count-=1
            if count:
                s.push(temp)
    return minElement