"""
Created on Wed May 12 14:52:55 2021

@author: q

GOAL : Solve Ex_5

If the values in one sample reveal no information about 
those of the other sample, then the samples are independent.


The independent t-test, also called the two sample t-test, 
independent-samples t-test or student's t-test, 
is an inferential statistical test that determines 
whether there is a statistically significant difference 
between the means in two unrelated groups.

source: https://statistics.laerd.com/statistical-guides/independent-t-test-statistical-guide.php

The Independent Samples t Test compares the means of two 
independent groups in order to determine whether there is 
statistical evidence that the associated population means 
are significantly different. The Independent Samples t Test 
is a parametric test.

The null hypothesis (H0) and alternative hypothesis (H1) of the 
Independent Samples t Test can be expressed in two different but 
equivalent ways:

H0: µ1 = µ2 ("the two population means are equal")
H1: µ1 ≠ µ2 ("the two population means are not equal")

OR

H0: µ1 - µ2 = 0 ("the difference between the two population 
                 means is equal to 0")
H1: µ1 - µ2 ≠ 0 ("the difference between the two population 
                 means is not 0")

where µ1 and µ2 are the population means for group 1 and group 2, 
respectively. Notice that the second set of hypotheses can be 
derived from the first set by simply subtracting µ2 from both 
sides of the equation.


source : https://libguides.library.kent.edu/spss/independentttest


Show Answer:

Looking at the data in h1, you can see that the samples from 0 to 250 
are higher than the examples between 250 and 500. 
In the hr2 data, the examples occur with a frequency of 125, so 
taking the first 250 and then the next 250 will give almost the same 
average but the standard deviation will be different. 


"""

# eval and change working directory
import os
if os.getcwd() != '/home/q/MIT_6002/Last_Round':
    os.chdir('/home/q/MIT_6002/Last_Round')

import numpy as np
import random
import matplotlib.pyplot as plt

def loadFile(file = 'hr1.txt'):
    inFile = open(file)
    hr = []
    for line in inFile:
        if line != '' and len(line) != 1:
            hr.append(float(line))
            
    return hr

hr1 = loadFile(file = 'hr1.txt')
hr2 = loadFile(file = 'hr2.txt')

plt.plot(hr1)
plt.show()

plt.plot(hr2)
plt.show()

def t_test(s1, s2):
    
    """
    Eval 99.5 confidence level of sample independence
    
    Conclusion : both datasets belong to human hearts
    
    """
    popm1 = np.trunc(np.mean(hr1))
    popm2 = np.trunc(np.mean(hr2))
    mean1 = np.trunc(np.mean(s1))
    sd1 = np.trunc(np.std(s1))
    mean2 = np.trunc(np.mean(s2))
    sd2 = np.trunc(np.std(s2))
    print(f'1 >>> {(1.96 * sd1) - mean1} <- mean : {mean1} -> {(1.96 * sd1) + mean1} ; sd : {sd1} ; pop mean : {popm1}')
    print(f'2 >>> {(1.96 * sd2) - mean2} <- mean : {mean2} -> {(1.96 * sd2) + mean2} ; sd : {sd2} : pop mean : {popm2}')
    pass


# Using random sample
sample1 = random.sample(hr1, 250)
sample2 = random.sample(hr2, 250)

t_test(sample1, sample2)

plt.hist(np.array(sample1))
plt.title('250 Sample on hr1')
plt.show()

plt.hist(np.array(sample2))
plt.title('250 Sample on hr2')
plt.show()

# using random choice

choice1 = [ random.choice(hr1) for n in range(250) ]
choice2 = [ random.choice(hr2) for n in range(250) ]

t_test(choice1, choice2)

plt.hist(np.array(choice1))
plt.title('250 choice on hr1')
plt.show()

plt.hist(np.array(choice2))
plt.title('250 choice on hr2')
plt.show()

# using first 500

t_test(hr1[:500], hr2[:500])

plt.hist(hr1[:500])
plt.title('500 slice on hr1')
plt.show()

plt.hist(hr2[:500])
plt.title('500 slice on hr2')
plt.show()
