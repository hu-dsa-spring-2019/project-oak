All source codes should be submitted within this folder.
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
##print(len(file1))
##for i in file1:
##    print((list(file1.values())))

##for i in file1:
##    point=file1.get(i)
##    print('Point Number# '+str(i))
##    for j in point:
##        print(j)

askUser=input('Do want to register a new location OR retrive the number of van for a location? Type "register" for the first option and "Best Van" for the second one: ')         
if askUser=='Best Van':        
    loc=input('Where do you live?').replace(' ','-')+'-Karachi'
else:
    loc=''
vans=[]

#Returns the time in formatted Order

def timer(time):
    f=time-int(time)
    if f>0.59:
        time=int(time+1.00)
        f=f-0.60
        time+=f
    return time

#Generates The list of vans

vans=[]

def findAllVans(loc):
    for i in file1:
        g=file1.get(i)
        for k in g:
            dist=k
            if loc in k:
                t=round(((((float(k[2]))/30)*60)/100),2)
                time=round((float(k[4])+t),2)
                hold=timer(time)
                res=[str(i),hold,k[3]]
##              print('van: '+str(res[0])+', Estimated time of drop off: '+str(res[1])+' p.m, Order: '+res[2])
                vans.append(res)
            
##print(vans)
def bubble_sort(array):
    index = len(array) - 1
    while index >= 0:
        for j in range(index):
            if array[j][1] > array[j+1][1]:
                array[j], array[j+1] = array[j+1], array[j]
            if array[j][1] == array[j+1][1]:
                if array[j][2] > array[j+1][2]:
                    array[j], array[j+1] = array[j+1], array[j]          
        index -= 1
    return array

def chooseBest(vans):
    if len(vans)==1:
        print('Van: '+str(vans[0][0])+', Estimated time of drop off: '+str(round(vans[0][1],2))+' p.m, Order: '+vans[0][2])
    else:
        bubble_sort(vans)
        for i in vans:
            print('Van: ' + str(i[0]) + ', Estimated time of drop off: ' + str(round(i[1], 2)) + ' p.m, Order: ' + i[2])
        
findAllVans(loc)
chooseBest(vans)

#This is the Google API code that helps us to retrive distances between locations

import urllib.request, json
import googlemaps


    
#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCZG2zTi7wFQ4Z-jeTpImkPuMXWQEa6Fyw'


def dist(origin,destination):
    #Building the URL for the request

    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request

    #Sends the request and reads the response.
    response = urllib.request.urlopen(request).read()

    #Loads response as JSON
    directions = json.loads(response)
    return (directions["routes"][0]["legs"][0]["distance"]["value"])
    


#User Input
add=(input('Your Address? ').replace(' ','+'))+'+Karachi'
uni='habib+university'

#This sorting algorithim helps to sort the van list based on the new added van and the updated distances

def bubble_sort2(array):
    index = len(array) - 1
    while index >= 0:
        for j in range(index):
            if float(array[j][2]) < float(array[j+1][2]):
                array[j], array[j+1] = array[j+1], array[j]
        index -= 1
    return array

#This function assigns the updated vans list with their new drop off order
def align(a):
    count=len(a)
    for i in range(len(a)):
        a[i][3]=count
        count-=1
    return a

#Finds the best van based on the location

def findVan(add):
    key=file1.keys()
    for i in key:
        point=file1.get(i)
        for j in point:
            a=dist(add,j[0])
            if a<2000:
                    return i

##        van=int(input('We could not find a suitable van for you, please choose manually: '))
##        return van
    
        

    

#Main function that registers the new location       
def addingAnode(address):
    van=findVan(add)  
    distance=round(((dist(add,uni))/1000),1)
    uniDist=distance
    for i in file1[van]:
        f=i[0].replace('-','+')
        distance1=round(((dist(add,f))/1000),1)
        if distance<distance1:
            continue
        else:
            pos='0'
            distance=round((distance1+(float(i[2]))),1)
            address=address.replace('+',' ')
        dataInput=[address,uniDist,distance,pos,file1[van][1][4]]
    file1[van].append(dataInput)
    bubble_sort2(file1[van])
    print(align(file1[van]))


    

        

addingAnode(add)


DeletingNodes
addressD=input('Do you want to delete any location? ')
vanD=int(input('From which van? '))


def deletingNodes(addressD,vanD):
    for i in file1[vanD]:
        if i[0]==addressD:
            file1[vanD].remove(i)
    bubble_sort2(file1[vanD])
    align(file1[vanD])            
    print(file1[vanD])

deletingNodes(addressD,vanD)
