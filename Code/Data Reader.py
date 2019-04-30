def create_list(doc):
    file = open(doc, 'r')
    file1 = {}
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

    print(file1)


create_list('ProcessedDatasetNew.csv')
