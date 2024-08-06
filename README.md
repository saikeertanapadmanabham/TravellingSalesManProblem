
TRAVELLING SALESMAN PROJECT:
===========================
IMPLEMENTED TSP USING BELOW FOUR ALGORITHMS.

HOW TO RUN THIS
===============
When you run the code,
	1.It will display list of 40 cities with indexes
	2.since ending city is same as starting city, it will only ask for starting city index number.
	3.Taking the list of city with indexes as reference, user can type any city index as starting city index.
	

Explanation:
===========

In the above example, starting city is given as 4
We get the results of total prize collected,sequence of the cities visited,total distance travelled and total time of execution results by using following algorithms.

1.Random Algorithm
2.Greedy Algorithm
3.Exhaustive Algorithm
4.Reinforcement Learning Algorithm

Procedure:
----------
1. Initially from input text file we get cities,latitude & longitudes and prizes data in a list
2.By using Haversine formula, we get the distance between two latitude and longitudes
3.We generate distance array matrix to calculate distance from each index to renaining points.
3.By getting start data,end date and the total prize to collect, we implement above algorithms

SAMPLE OUTPUT:

Output:
=======

List of cities
0 .  Albany NY
1 .  Annapolis MD
2 .  Atlanta GA
3 .  Augusta ME
4 .  Austin TX
5 .  Baton Rouge LA
6 .  Bismarck ND
7 .  Boise ID
8 .  Boston MA
9 .  Carson City NV
10 .  Charleston WV
11 .  Cheyenne WY
12 .  Columbia SC
13 .  Columbus OH
14 .  Concord NH
15 .  Denver CO
16 .  Des Moines IA
17 .  Dover DE
18 .  Frankfort KY
19 .  Harrisburg PA
20 .  Hartford CT
21 .  Helena MT
22 .  Indianapolis IN
23 .  Jackson MS
24 .  Jefferson City MO
25 .  Lansing MI
26 .  Lincoln NE
27 .  Little Rock AR
28 .  Madison WI
29 .  Montgomery AL
30 .  Montpelier VT
31 .  Nashville TN
32 .  Oklahoma City OK
33 .  Olympia WA
34 .  Phoenix AZ
35 .  Pierre SD
36 .  Providence RI
37 .  Raleigh NC
38 .  Richmond VA
39 .  Sacramento CA
40 .  Saint Paul MN
41 .  Salem OR
42 .  Salt Lake City UT
43 .  Santa Fe NM
44 .  Springfield IL
45 .  Tallahassee FL
46 .  Topeka KS
47 .  Trenton NJ
48 .  Washington DC
Please enter start city index number : 10
Please enter end city index number : 14
Please enter the total prize to collect :123

By Running Random Algorithm we get below results
Total Prize Collected:  155.0
Sequence of cities indexes:  [10, 36, 6, 29, 34, 15, 14]
Total Distance Travelled:  9688.91593649372  KM
Total Time of execution:  0.0009695999906398356

By Running Greedy Algorithm we get the below results
Total Prize Collected:  166.0
Sequence:  [10, 41, 3, 33, 14]
Total Distance travelled:  16426.743613882885  KM
Total Time of execution:  0.0010248000035062432

By Running Exhaustive Algorithm we get the below results
Total Prize Collected:  1652.0
 22, 29, 31, 28, 44, 23, 5, 24, 27, 40, 16, 46, 14]
Total Distance Travelled:  400000  KM
Total Time of execution:  0.0009652000153437257

By Running Deep Reinforcement Learning Algorithm we get the below result
Total Prize Collected:  182.0
Sequence of visited cities indexes:  [10, 2, 1, 14]
Total distance travelled:  1762.5632344590367
Time of execution:  0.002661700011231005

