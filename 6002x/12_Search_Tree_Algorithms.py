
"""
Create a Search Tree Algorithm for binary, ternary 
and generalize the algorithm for n elements, n levels in the tree
"""

def tree(elements = [], levels = 3):
    
    l = len(elements)
    tree = []
    # number of items is l ** n
    for i in range(l ** levels):
        
        # use length of list
        c = ''
        for j in range(levels):
            
            c += elements[i // (l ** j) % l]
            
        tree.append(c)
        
    return tree
        
print(tree('0123', 3))


# create binary tree  
binary = '01'
n = 3
# number of items is len(binary) ** n
for i in range(len(binary) ** n):
    
    # use binary system [0, 1]
    c = ''
    for j in range(n):
        
        c += binary[i // (2 ** j) % 2]
    
    print(c)

# create a ternary tree
n = 3
ternary = '012'

# number of items is 3 ** n
for i in range(len(ternary) ** n):
    
    # use ternary system [0, 1, 2] not [0, 1]
    c = ''
    for j in range(n):
        
        c += ternary[i // (3 ** j) % 3]
        
    print(c)

    
    
 
