
# W = 13
# i  pi  wi pi/wi
# 1 $20  2   10
# 2 $30  5   6
# 3 $35  7   5
# 4 $12  3   4
# 5 $3   1   3

# n = 5 #items given
# W = 13 # capacity of knapsack
# p = [0, 20, 30, 35, 12, 3] # profit of each item (starts with item 0 = $0)
# w = [0, 2, 5, 7, 3, 1] # weight of each item
# p_per_weight = [0, 10, 6, 5, 4, 3] #price per weight
# items are ordered by price per weight
 
import numpy as np

#n = 50
#p = np.random.randint(1,501,50)
#w = np.random.randint(1,21,50)
#p_per_weight = np.divide(p, w)



n = 10
p = [40, 30, 50, 10, 12, 60, 30, 24, 55, 45]
w = [2, 50, 10, 5, 6, 30, 6, 4, 5, 9]
p_per_weight = np.divide(p, w)
W = 32



class Priority_Queue:
    def __init__(self):
        self.pqueue = []
        self.length = 0
    
    def insert(self, node):
        for i in self.pqueue:
            get_bound(i)
        i = 0
        while i < len(self.pqueue):
            if self.pqueue[i].bound > node.bound:
                break
            i+=1
        self.pqueue.insert(i,node)
        self.length += 1

    def print_pqueue(self):
        for i in list(range(len(self.pqueue))):
            print ("pqueue",i, "=", self.pqueue[i].bound)
                    
    def remove(self):
        try:
            result = self.pqueue.pop()
            self.length -= 1
        except: 
            print("Priority queue is empty, cannot pop from empty list.")
        else:
            return result
        
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
        self.items = []
        
            
def get_bound(node):
    if node.weight >= W:
        return 0
    else:
        result = node.profit
        j = node.level + 1
        totweight = node.weight
        while j <= n-1 and totweight + w[j] <= W:
            totweight = totweight + w[j]
            result = result + p[j]
            j+=1
        k = j
        if k<=n-1:
            result = result + (W - totweight) * p_per_weight[k]
        return result


nodes_generated = 0
pq = Priority_Queue()

v = Node(-1, 0, 0, 0) # v initialized to be the root with level = 0, profit = $0, weight = 0
nodes_generated+=1
maxprofit = 0 # maxprofit initialized to $0
v.bound = get_bound(v)
#print("v.bound = ", v.bound)


pq.insert(v)

while pq.length != 0:
    
    v = pq.remove() #remove node with best bound
#    print("\nNode removed from pq.")
#    print("Priority Queue: ") 
#    pq.print_pqueue()
    
#    print("\nmaxprofit = ", maxprofit)
#    print("Parent Node: ")
#    print("v.level = ", v.level, "v.profit = ", v.profit, "v.weight = ", v.weight, "v.bound = ", v.bound, "v.items = ", v.items)

    if v.bound > maxprofit:
        #set u to the child that includes the next item
        u = Node(0, 0, 0, 0)
        nodes_generated+=1
        u.level = v.level + 1
        u.profit = v.profit + p[u.level]
        u.weight = v.weight + w[u.level]
        #take v's list and add u's list
        u.items = v.items.copy()
        u.items.append(u.level) # adds next item

        if u.weight <= W and u.profit > maxprofit: 
            #update maxprofit
            maxprofit = u.profit
#            print("\nmaxprofit updated = ", maxprofit)
            bestitems = u.items
#            print("bestitems = ", bestitems)
        u.bound = get_bound(u)
#        print("u.bound = ", u.bound)
        if u.bound > maxprofit:
            pq.insert(u)
         
        #set u to the child that does not include the next item
        u2 = Node(u.level, v.profit, v.weight, v.bound)
        nodes_generated+=1
        u2.bound = get_bound(u2)
        u2.items = v.items.copy()

        if u2.bound > maxprofit:
            pq.insert(u2)

        

print("\nEND maxprofit = ", maxprofit, "nodes generated = ", nodes_generated)
print("bestitems = ", bestitems)
