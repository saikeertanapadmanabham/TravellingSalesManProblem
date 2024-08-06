from itertools import permutations
import math
import time
from math import radians, cos, sin, asin, sqrt
import timeit
from sys import maxsize


def extractDataFromFile():
    cities = []
    LongLats = []
    prizes = []
    with open("states.txt") as file:
        for line in file:
            citi = line.split(',')
            rest=citi[1].split() 
            cities.append(citi[0]+' '+rest[0])
            prizes.append(float(rest[3]))
            temp=[]
            temp.append(float(rest[1]))
            temp.append(float(rest[2]))
            LongLats.append(temp)
            #data = citi[1].split()
            #temp = []
            #cities.append(citi[0]  + citi[1])
            #print(citi[2])
            #prizes.append(float(citi[5]))
            #temp.append(float(citi[3]))
            #temp.append(float(citi[4]))
            #LongLats.append(temp)
        
        #print(cities) 
        #print(LongLats)
        #
        # 
        # print(prizes)    
    return cities, LongLats, prizes
cities, LongLats, prizes = extractDataFromFile()

print("List of cities")
for i,j in enumerate(cities):
    print(i,". ",j)

def distance(d1,d2):
    a=d1
    b=d2
    return haversine(a[0],a[1],b[0],b[1])

def haversine(lon1, lat1, lon2, lat2):
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c

def distBetweenCities(info):
    Distance =[]
    for i,j in enumerate(info):
        temp=[]
        for m,n in enumerate(info):
            if(i==m):
                temp.append(0);
            else:
                val=distance(info[i],info[m])
                temp.append(val);
        Distance.append(temp)
    #print(Distance)
    return Distance
distance_array=distBetweenCities(LongLats)
#print(distance_array[2][3])


start_index = input("Please enter start city index number : ")
end_index= input("Please enter end city index number : ")
Total_prize=input("Please enter the total prize to collect :")

import random
import timeit
def RandomAlgorithm(start_in,end_in,tot_prize):
    total = 0
    TotDist=0
    count=0
    total=total-prizes[start_in]-prizes[end_in]
    visited = []
    currCity = start_in
    order = []
    order.append(start_in)
    num = len(prizes)
    visited.append(start_in)
    while total<tot_prize:
        index = random.randint(0,num-1)
        if index not in visited:
            TotDist = TotDist + distance_array[currCity][index]
            currCity = index
            visited.append(currCity)
            total = total + prizes[index]
            order.append(currCity)
        count=count+1
    
    order.append(end_in)
    print("Total Prize Collected: ", total)
    print("Sequence of cities indexes: ", order)
    print("Total Distance Travelled: ", TotDist ," KM ")

print("\nBy Running Random Algorithm we get below results")  
start = timeit.default_timer()   
RandomAlgorithm(int(start_index),int(end_index),int(Total_prize))
stop = timeit.default_timer()
print('Total Time of execution: ', stop - start) 

import timeit
def GreedyAlgorithm(start_in,end_in,total_prize):
    total = 0
    Totdist = 0
    count=0
    total=total-prizes[start_in]-prizes[end_in]
    visited = []
    currCity = start_in
    sequence = []
    sequence.append(start_in)
    while total<total_prize:
        #print("hello")
        val2 = 0
        index = 0
        for i,d in enumerate(LongLats):
            if i in visited  or i == start or i == currCity:
                continue
            val1 = (distance_array[i][currCity])
            if val1 > val2:
                val2 = val1
                index = i
        Totdist = Totdist + distance_array[currCity][index]
        currCity = index
        visited.append(currCity)
        total = total + prizes[index]
        sequence.append(currCity)
        count=count+1
    
    sequence.append(end_in)
    
    et = time.time()
    print("Total Prize Collected: ", total)
    print("Sequence: ", sequence)
    print("Total Distance travelled: ", Totdist, " KM ")


print("\nBy Running Greedy Algorithm we get the below results")
start = timeit.default_timer()
GreedyAlgorithm(int(start_index),int(end_index),int(Total_prize))
stop = timeit.default_timer()
print('Total Time of execution: ', stop - start) 




def ExhaustiveAlgorithm(start_in,end_in,prize_collect):
    visited=[]
    totDist=0
    total=0
    total=total-prizes[start_in]-prizes[end_in]    
    count=0
    visited.append(start_in)
    order=[]
    order.append(start_in)
    while count<=10:
        for i in range(len(cities)):
            if i not in visited:
                #print( " i = ", i )
                visited.append(i)
                start_in=i
                temp=0
                temp1=0
                for m,n in enumerate(distance_array):
                    #print("m= ",m, " n = ", n)
                    if(i!=m ):
                        
                        temp=n.index(min(n))  
                        n[temp]=100000
                        #print(min(n))
                        temp1=n.index(min(n))
                        start_in=temp1
                        totDist+=distance_array[start_in][temp1]
                        #print(prizes[start_in])
                        total+=int(prizes[start_in])
                        visited.append(temp1)
                        order.append(temp1)
                        #print("n= ",n, "temp = ",temp1)
                        count+=1
                        if(total>=prize_collect):
                            break;
                        
                    
    order.append(end_in)
    print("Total Prize Collected: ", total)
    print("Sequence of cities indexes: ", order)
    print("Total Distance Travelled: ", totDist ," KM ")                
        
    
print("\nBy Running Exhaustive Algorithm we get the below results")
start = timeit.default_timer()
ExhaustiveAlgorithm(int(start_index),int(end_index),int(Total_prize))
stop = timeit.default_timer()
print('Total Time of execution: ', stop - start) 

def ReinforcementLearning(start, end, prize_collect):
	#Q tables and Reward tables
    Q_table = []
    n = len(prizes)
    Reward_table = []
    TotalDistanceSum = 0
    for i in range(n):
        for j in range(n):
            TotalDistanceSum = TotalDistanceSum + distance_array[i][j]
    for i in range(n):
        arr = []
        arr2 = []
        for j in range(n):
            val = (n*n)/(n*TotalDistanceSum)
            arr.append(val)
            arr2.append(0)
        Q_table.append(arr)
        Reward_table.append(arr2)
    learning_rate = 0.1
    discount = 0.3
    alpha = 1.1
    beta = 1.1
    w = 10
    QProb = 5
    visited = []
    SequenceOfVisitedCities = []
    DistTotal = []
    NodesCurrentCities = []
    tot_prizes = []
    best_agent = 0
    AgentsNumber = 10
    for n in range(AgentsNumber):
        visited.append([])
        SequenceOfVisitedCities.append([start])
        DistTotal.append(0)
        NodesCurrentCities.append(start)
        tot_prizes.append(0)  
    #Run algorithm for 50 iterations
    for it in range(50):
        for i in range(n):
            for m in range(AgentsNumber):
                if tot_prizes[m] > prize_collect:
                    continue
                    
                currCity = NodesCurrentCities[m]
                q = random.randint(0,10)
                index = 0
                if q < QProb:
                    index = 0
                    max_t = 0
                    for c in range(n):
                        if c not in visited[m] and c != currCity and c != start and c != end:
                            ratio = pow(Q_table[c][currCity],alpha)/pow(distance_array[c][currCity],beta)
                            if ratio > max_t:
                                max_t = ratio
                                index = c
                else:
                    sum_probs = 0
                    probs = []
                    probs_indices =[]
                    for c in range(n):
                        if c not in visited[m] and c != currCity and c != start and c != end:
                            ratio = pow(Q_table[c][currCity],alpha)/pow(distance_array[c][currCity],beta)
                            probs.append(ratio)
                            probs_indices.append(c)
                            sum_probs = sum_probs + ratio
                    for i,p in enumerate(probs):
                        probs[i] = p/sum_probs
                        
                    index = random.choices(population=probs_indices, weights=probs,k=1)[0]
                
                
                visited[m].append(currCity)   
                SequenceOfVisitedCities[m].append(index)
                NodesCurrentCities[m] = index
                tot_prizes[m] = tot_prizes[m] + prizes[index]
                DistTotal[m] = DistTotal[m] + distance_array[index][currCity]
                val = (1-learning_rate)*Q_table[index][currCity]
                max_t = 0
                for c in range(n):
                    if c not in visited[m] and c != index and c != start and c != end:
                            if Q_table[c][index] > max_t:
                                max_t = Q_table[c][index]
                val = val + learning_rate*discount*max_t
                Q_table[currCity][index] = val
        max_t = 0
        index = 0
        for m in range(AgentsNumber):
            ratio = tot_prizes[m]/DistTotal[m]
            if ratio > max_t:
                max_t = ratio
                index = m
        prev = start
        best_agent = index
        for p in SequenceOfVisitedCities[index]:
            Reward_table[start][p] = tot_prizes[index]/DistTotal[index]
            val = Q_table[start][p]*(1-learning_rate)
            max_t = 0
            for i in range(n):
                if i != p:
                    if Q_table[p][i] > max_t:
                        max_t = Q_table[p][i]
            val = val + learning_rate*(Reward_table[start][p] + max_t)
            Q_table[start][p] = val
            start = p
        for n in range(AgentsNumber):
            visited.append([])
            SequenceOfVisitedCities.append([start])
            DistTotal.append(0)
            NodesCurrentCities.append(start)
            tot_prizes.append(0)
    
    SequenceOfVisitedCities[best_agent].append(end)
    DistTotal[best_agent] = DistTotal[best_agent] + distance_array[NodesCurrentCities[best_agent]][end]
    print("Total Prize Collected: ", tot_prizes[best_agent])
    print("Sequence of visited cities indexes: ", SequenceOfVisitedCities[best_agent])
    print("Total distance travelled: ", DistTotal[best_agent])
    

print("\nBy Running Deep Reinforcement Learning Algorithm we get the below result")
start = timeit.default_timer()
ReinforcementLearning(int(start_index),int(end_index),int(Total_prize))         
stop = timeit.default_timer()
print('Time of execution: ', stop - start) 