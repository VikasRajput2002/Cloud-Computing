#!/usr/bin/python

"""mapper.py"""

import sys

def euclidean(point_a, point_b):
        
        distance = 0
        for pts1, pts2 in zip(point_a, point_b):
            distance += (pts1-pts2)**2
        
        distance = distance**0.5
        return distance




def main():

  
  cand_1 = ['5.8','4.0','1.2','0.2','Iris-setosa']
  cand_2 = ['6.1','2.8','4.0','1.3','Iris-versicolor']
  cand_3 = ['6.3','2.7','4.9','1.8','Iris-virginica']
  
  with open('iris.txt', 'r') as file: 
       data = file.readlines() 
       for line in data: 
           #line = line.strip() 
           words=line.split(",")
           #print((float(words[0]),float(words[1])))
           dist_1 = euclidean([float(words[0]),float(words[1])],[float(cand_1[0]),float(cand_1[1])])
           dist_2 = euclidean([float(words[0]),float(words[1])],[float(cand_2[0]),float(cand_2[1])])
           dist_3 = euclidean([float(words[0]),float(words[1])],[float(cand_3[0]),float(cand_3[1])])
            
           min_dist = min(dist_1,min(dist_2,dist_3))
           if min_dist == dist_1:
               print('([%s\t,%s\t,%s],\t%s)' % (words[0],words[1],'C1',1))
           elif min_dist == dist_2:
               print('([%s\t,%s\t,%s],\t%s)' % (words[0],words[1],'C2',1))
           else:
               print('([%s\t,%s\t,%s],\t%s)' % (words[0],words[1],'C3',1))




#!/usr/bin/env python

"""reducer.py"""

import sys
import re

class_1 = 'Iris-setosa'
class_2 = 'Iris-versicolor'
class_3 = 'Iris-virginica'

spel_l , spel_w , count_1 = 0.0,0.0,0
spel_l_2 , spel_w_2 , count_2 = 0.0,0.0,0
spel_l_3 , spel_w_3 , count_3 = 0.0,0.0,0


for line in sys.stdin:
    line = line.strip()
    line = re.sub('[^\w\s.]','',line)
    line = line.split()

    if line[2] == 'C1':
        spel_l  += float(line[0])
        spel_w  += float(line[1])
        count_1 += int(line[3])

    elif line[2] == 'C2':
        spel_l_2  += float(line[0])
        spel_w_2  += float(line[1])
        count_2 += int(line[3])

    else :
        spel_l_3  += float(line[0])
        spel_w_3  += float(line[1])
        count_3 += int(line[3])

             
       
##################### NEW Candidate point ###############################

spel_l , spel_w = spel_l/float(count_1) , spel_w/float(count_1)
spel_l_2 , spel_w_2 = spel_l_2/float(count_2) , spel_w_2/float(count_2)
spel_l_3 , spel_w_3 = spel_l_3/float(count_3) , spel_w_3/float(count_3)


print('[%s,%s,%s]' % (spel_l,spel_w,class_1))
print('[%s,%s,%s]' % (spel_l_2,spel_w_2,class_2))
print('[%s,%s,%s]' % (spel_l_3,spel_w_3,class_3))

