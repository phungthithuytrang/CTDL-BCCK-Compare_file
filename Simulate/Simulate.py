import matplotlib.pyplot as plt
 

def Data():
    data=[[]]
    temp=[]
    name=[]
    i=0
    for line in open('sample.txt', 'r'):
        lines = [i for i in line.split()]
        if i==0:
            for j in lines:
                name.append(j)
                temp=[]
                data.append(temp)
        else:
            for j in lines:
                num=lines.index(j)
                data[num].append(float(j))
        i=i+1
 
    for dl in data:
       print("@")
       for i in dl:
           print(i)
    for z in data[1:-1]:
        plt.plot(data[0], z , label=name[data.index(z)], marker = 'o')
        plt.yticks(z)

    plt.title("Simulate")
    plt.xlabel('File size (kb)')
    plt.ylabel('Time')

    plt.legend()
    plt.show()

def finddetail(str):
    data=[[]]
    x=[]
    for line in open(str, 'r'):
        lines = [i for i in line.split()]
        x.append(lines[0])
        temp=[]
        for j in lines[1:]:
            temp.append((float)(j))
        data.append(temp)
    minL=[]
    meanL=[]
    maxL=[]
    for dl in data[1:]:
        minL.append(min(dl))
        maxL.append(max(dl))
        meanL.append(sum(dl)/len(dl))

    #plt.plot(x, minL , label="min", marker = 'o')
    #plt.plot(x, maxL , label="max", marker = 'o')
    plt.plot(x, meanL , label="mean", marker = 'o')

    #plt.yticks(minL)
    #plt.yticks(maxL)
    plt.yticks(meanL)

    plt.title("Simulate")
    plt.xlabel('File size (kb)')
    plt.ylabel('Time')

    plt.legend()
    plt.show()

def CTDL():
    read=['docBTree.txt','docAVL.txt','docBST.txt','docTrie.txt']
    compare=['sosanhBTree.txt','sosanhAVL.txt','sosanhBST.txt','sosanhTrie.txt']
    name=['BTree','AVL','BST','Trie']
    Process(read,name)
    Process(compare,name)
   
def Process(list,name):
    first=[]
    second=[]
    chart=[]
    data=[]
    for line in open(list[0], 'r'):
        lines = [i for i in line.split()]
        first.append(lines[0])
        second.append(lines[1])
        temp=[]
        for j in lines[2:]:
            temp.append((float)(j))
        data.append(temp)
    chart.append(data)

    for item in list[1:]:
        data=[]
        for line in open(item, 'r'):
            lines = [i for i in line.split()]
            temp=[]
            for j in lines[2:]:
                temp.append((float)(j))
            data.append(temp)
        chart.append(data)
    meanL=[]
    for ch in chart:
        meanN=[]
        for dl in ch:
            meanN.append(sum(dl)/len(dl))
        meanL.append(meanN)
    x=[]
    for i in first:
        x.append('P'+str(first.index(i)+1))
    index=0;
    for line in meanL:
        plt.plot(x[10:], line[10:] , label=name[index])
        index=index+1
        plt.yticks(line)

    plt.title("simulate")
    plt.xlabel('File pair')
    plt.ylabel('Time')

    plt.legend()
    plt.show()

CTDL()

#finddetail('desdata.txt')
#finddetail('sourdata.txt')







