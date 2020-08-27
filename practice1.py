#!/usr/bin/env python3
milk = [1,2,1]
apple = [100,1,200]
N = 3
P = 2
P -= 1
sumapples = 0
for i in range(N-1):
   if P == 0:
   	milk[i] = 0
   elif P >= 1:
   	if apple[i] >= apple[i+1]:
   	    sumapples += apple[i]
   	    P -= 1
print(sumapples + apple[N-1])
