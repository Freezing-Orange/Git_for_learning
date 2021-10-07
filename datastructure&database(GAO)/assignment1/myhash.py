class myhash:
    def __init__(self,pValue=7,hki=lambda x,i:x+i,*basicValue):
        self.valList=[None]*pValue
        self.pValue=pValue
        self.hki=hki
        self.dataCount=0
        self.add(*basicValue)

    def add(self, *keyValue):
        for x in keyValue:
            if self.dataCount==self.pValue:
                print('from key "'+str(x)+'" cannot be added because there is no more space')
                break
            for i in range(0,self.pValue):
                index=(self.hki(x,i))%self.pValue
                if self.valList[index]==None:
                    self.valList[index]=x
                    self.dataCount+=1
                    break
                
    def searchIndex(self,keyValue):
        for i in range(0,self.pValue):
            index=self.hki(keyValue,i)%self.pValue
            if self.valList[index]==keyValue:
                return index
        print('key "'+str(keyValue)+'" has not been found')
        return None

    def showHashTable(self):
        underline = '\033[4m'
        end = '\033[0m'
        print(underline+"|index|",end="")
        for i in range(self.pValue):
            print("{:^5d}".format(i),end="|")
        print(end)
        print("| key |",end="")
        for i in range(self.pValue):
            if self.valList[i]:
                print("{:^5d}".format(self.valList[i]),end="|")
            else:
                print("     |",end="")
        print()

    def compareWithHash(self,hashTable):
        length=len(hashTable)
        if self.pValue!=length:
            print("False, different length")
            return False
        flag=True
        for i in range(length):
            if self.valList[i] and hashTable[i]:
                if self.valList[i]!=hashTable[i]:
                    if flag:
                        print("False")
                    print("Key in index "+str(i)+" is different")
                    flag=False
            elif not self.valList[i] and not hashTable[i]:
                continue
            else:
                if flag:
                    print("False")
                print("Key in index "+str(i)+" is different")
                flag=False
        if flag:
            print("True")
            return True
        else:
            return False

def problem6Hash():
    print("Problem 6")
    goalTable=[9,18,None,12,3,14,4,21,None]
    print("(A)")
    p6HashA=myhash(9,lambda x,i:x+i,9,12,14,3,4,21,18)
    p6HashA.showHashTable()
    p6HashA.compareWithHash(goalTable)
    print("(B)")
    p6HashB=myhash(9,lambda x,i:x+i,9, 14, 4, 18, 12, 3, 21)
    p6HashB.showHashTable()
    p6HashB.compareWithHash(goalTable)
    print("(C)")
    p6HashC=myhash(9,lambda x,i:x+i,12, 14, 3, 9, 4, 18, 21)
    p6HashC.showHashTable()
    p6HashC.compareWithHash(goalTable)
    print("(D)")
    p6HashD=myhash(9,lambda x,i:x+i,12, 3, 14, 18, 4, 9, 21)
    p6HashD.showHashTable()
    p6HashD.compareWithHash(goalTable)
    print("(E)")
    p6HashE=myhash(9,lambda x,i:x+i,12, 9, 18, 3, 14, 21, 4)
    p6HashE.showHashTable()
    p6HashE.compareWithHash(goalTable)
    

def problem8Hash():
    print("Problem 8")
    p8Hash=myhash(11,lambda x,i:x%11+i+i*i,12,44,13,88,23,94,11,39,20)
    p8Hash.showHashTable()


def quizHash():
    print("quizHash")
    qHash=myhash(7,lambda x,i:x%7+i+i*i,88,97,39,158)
    qHash.showHashTable()

class chainNode():
    def __init__(self,value=None,next=None) -> None:
        self.val=value
        self.next=next

class hashChain():
    def __init__(self):
        self.head=chainNode()
        self.rear=self.head
    def headadd(self,val):
        if self.head==self.rear:
            temp=chainNode(val)
            self.head.next=temp
            self.rear=temp
        else:
            temp=chainNode(val,self.head.next)
            self.head.next=temp
    def rearadd(self,val):
        if self.head==self.rear:
            temp=chainNode(val)
            self.head.next=temp
            self.rear=temp
        else:
            temp=chainNode(val)
            self.rear.next=temp
            self.rear=temp        
    def showChain(self):
        if self.head==self.rear:
            return ""
        temp=self.head.next
        if temp:
            res=str(temp.val)
            temp=temp.next
        while temp:
            res+="->"+str(temp.val)
            temp=temp.next
        return res
class myChainHash():
    def __init__(self,pValue,hk=lambda k:k,mode="head",*basicValue) -> None:
        self.pValue=pValue
        self.hk=hk
        self.mode=1 if mode=="head" else 2
        self.valList=[hashChain() for _ in range(pValue)]
        self.add(*basicValue)

    def add(self,*keyValue):
        for k in keyValue:
            index=self.hk(k)%self.pValue
            if self.mode==1:
                self.valList[index].headadd(k)
            else:
                self.valList[index].rearadd(k)
    
    def showHashTable(self):
        underline = '\033[4m'
        end = '\033[0m'
        print(underline+"index|{:^20s}".format("key")+end)
        for i in range(self.pValue):
            print(underline,end="")
            print("{:^5d}".format(i),end="|")
            print("{:^20s}".format(self.valList[i].showChain())+end)


def problem7Hash():
    print("Problem 7")
    print("Insert into the head position")
    p7HashHead=myChainHash(11,lambda k:2*k+5,"head",12,44,13,88,23,94,11,39,20,16)
    p7HashHead.showHashTable()
    print()
    print("Insert into the rear position")
    p7HashRear=myChainHash(11,lambda k:2*k+5,"rear",12,44,13,88,23,94,11,39,20,16)
    p7HashRear.showHashTable()

problem6Hash()
print("\n")
problem7Hash()
print("\n")
problem8Hash()
print("\n")
quizHash()