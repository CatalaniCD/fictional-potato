"""

Brute Force Algorithm
1. Enumerate all possible combinations of items. That
is to say, generate all subsets of the set of subjects.
This is called the power set.

2. Remove all of the combinations whose total units
exceeds the allowed weight.

3. From the remaining combinations choose any one
whose value is the largest.

"""

# How to enumearte all possible comibinations ? 
  
  # 1. Use of combinatorics
  # 2. Cnk or Cnr Algorithm 

"""
solve Cnr
print all possible combinations for binaries in length 3
"""
binary = [0, 1]
n = 3

# itertools solution
from itertools import product
print([x for x in product([0, 1], repeat = 3)])

# Comprehension list solution
print([ (x,y,z) for x in binary for y in binary for z in binary ])

# iterative solution
for i in range(len(binary)):
        
    for j in range(len(binary)):
        
        for k in range(len(binary)):
            
            comb = str()
            comb += str(binary[i]) + str(binary[j]) + str(binary[k])
            print(comb)

"""
Get all possible combinations for a list
"""
binary = [0, 1]

"""

all subsets for a list [0, 1] : [[], [0], [1], [1, 0]]

"""
    
def get_all_subsets(some_list):
    
    """
    
    a. Reduction Step creates in the stack
    
    - empty list for last recurstion
    
    - each element of the list for each stack step
    
    b. result list is composed by :
        
        rest_list = [1], []
        first_element = 0, 1
        
        [1] + [] == [1]
        [] + [] == []
        
        rest_list + first_element = [1].append(0), [].append(0), \
                                    [1].append([]), [].append([])
                                    
    """
    
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        print('\n=== Reduction Step ===\n')
        return [[]]
    
    if len(some_list) == len(animals):
        print('=== initial list :', animals)
        print()
        
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    
    # Strategy: Get all the subsets of rest_list;
    
    # for each of those subsets, a full subset list will contain both :
    
        # the original subset as well 
        # as a version of the subset that contains first_elt
        
    print('first element : ', first_elt)
    print('rest list : ', rest_list)
    
    for partial_subset in get_all_subsets(rest_list):
        
        # print('elements returned from the stack : ', get_all_subsets(rest_list))
        
        print(f'partial subset : {partial_subset}\nfirst element : {first_elt}\nnext_subset : {partial_subset[:] + [first_elt]}')
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
        
        print(f'added to subsets {partial_subset}, {next_subset}')
        print()
        
    print('=== Stack Register : ', len(next_subset) )
    print('\nsubsets', subsets,'\n')
    
    return subsets
                   
print(sorted(get_all_subsets(animals), key = lambda x: len(x)))


"""

=== initial list : [0, 1]

first element :  0
rest list :  [1]
first element :  1
rest list :  []

=== Reduction Step ===

partial subset : []
first element : 1
next_subset : [1]
added to subsets [], [1]

=== Stack Register :  1

subsets [[], [1]] 

partial subset : []
first element : 0
next_subset : [0]
added to subsets [], [0]

partial subset : [1]
first element : 0
next_subset : [1, 0]
added to subsets [1], [1, 0]

=== Stack Register :  2

subsets [[], [0], [1], [1, 0]] 

[[], [0], [1], [1, 0]]

"""
