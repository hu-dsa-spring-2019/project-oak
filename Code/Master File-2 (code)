file1 = {}
#print(len(file1)) ###edit###
def create_list(doc):
    file = open(doc, 'r')
    c = 0
    for x in file:
        if c is 0:
            c += 1
            pass
        else:
            a = x[1:-2].split()
            b = a[0]
            d = int(b)
            if d not in file1:
                file1[d] = []
                file1[d].append(a[1:])
            else:
                file1[d].append(a[1:])
                # elif i > 0 and len(x.split()) - i > 4:
                #     if file1[b] is []:
                #         file1[b].append(a[i])
                #     else:
                #         # if file1[b][0] != a[0]:
                #         #     file1[b]
                #         file1[b]=[a[i]]
                #         print(file1[b])
                # elif type(a[i]) == int:
                #     print(a[i])
                #     file1[b][0].append(a[i])



create_list('ProcessedDatasetNew.csv')


##DeletingNodes
def align2(a):
    count=len(a)
    for i in range(len(a)):
        a[i][3]=count
        count-=1
    return a
def bubble_sort2(array):
    index = len(array) - 1
    while index >= 0:
        for j in range(index):
            if float(array[j][2]) < float(array[j+1][2]):
                array[j], array[j+1] = array[j+1], array[j]
        index -= 1
    return array

addressD=input('Which location do you want to delete? ').replace(' ','-')+'-Karachi'
vanD=int(input('From which van? '))


def deletingNodes(addressD,vanD):
    print("Before deletion: "+str(file1[vanD]))
    for i in file1[vanD]:
        if i[0]==addressD:
            file1[vanD].remove(i)
    bubble_sort2(file1[vanD])
    align2(file1[vanD])            
    print('After deletion: '+str(file1[vanD]))

deletingNodes(addressD,vanD)
        
