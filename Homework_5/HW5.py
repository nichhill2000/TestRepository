#HW 5
#Due Date: 12/13/2019, 11:59PM 
########################################
#
# Name: Nicholas Hill
# Collaboration Statement:
#
########################################

# ---Copy your Queue code from lab 8 and your Stack code from HW3 here (you can remove their comments)  
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        # Checks to see if the count of the list is zero, returns true if it is, false if not
        if self.count == 0:
            return True
        return False


    def enqueue(self, x):
        # Create node object from given value
        newNode = Node(x)
        
        # if first item to be added to queue, creates both head and tail
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.count = self.count + 1
            return
        # tail is moved inside the queue one and newNode is made new tail, number of items updated
        temp = self.tail
        temp.next = newNode
        self.tail = newNode
        self.count = self.count + 1
        return


    def dequeue(self):
        #Returns queue is empty if no items to dequeue
        if self.count == 0:
            return 'Queue is empty'
        #self.head is deleted and updated, count is updated
        temp = self.head
        self.head = self.head.next
        self.count = self.count - 1
        # if last item is removed from queue, tail is deleted as well
        if self.count == 0:
            self.tail = None
        #returns value of deleted head
        return temp.value


    def __len__(self):
        #Returns length of queue, stored as count
        return self.count
        

    def reverse(self):
        #base case, when list is completely grabbed, returns nothing
        if self.isEmpty():
            return
        #items from queue stored in new nodes in reverse order from recursion, returned in that reverse order
        else:
            tempValue = self.dequeue()
            temp = Node(tempValue)
            self.reverse()
            self.enqueue(temp.value)

class Stack:

    def __init__(self):
        self.top = None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    #Function that sees if count is zero, returns true or false depending
    def isEmpty(self):
        if self.count == 0:
            return True
        return False
        
    #Allows class to use the len function
    def __len__(self): 
        return self.count
        
    #Adds a new element to stack, and pushs other elements down; becomes new top 
    def push(self,value):
        newNode = Node(value)

        if self.isEmpty():
            self.top = newNode
            self.count = self.count + 1
            return
        
        newNode.next = self.top
        self.top = newNode
        self.count = self.count + 1
        return

    #Removes top element from stack, and moves elements under it up, former next value becomes new top
    def pop(self):
        if self.top == None:
            return None

        temp = self.top
        self.top = self.top.next
        self.count = self.count - 1
        return temp.value
        
    
    #Allows user to see top value of stack
    def peek(self):
        return self.top.value
        


#----- HW5 Graph code     
class Graph:

    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start): 
        
        #Create Queue and output visited list, initialize the starting node into queue and visited
        bfsQueue = Queue()
        visited = []

        bfsQueue.enqueue(start)
        visited.append(start)

        #Loop while queue isn't empty, dequeue starting node into variable
        while bfsQueue.isEmpty() == False:
            bfsNode = bfsQueue.dequeue()

            #Grabs list which is tied to key of dict
            bfsList = self.vertList[bfsNode]

            #Sorts list if it isn't empty using a different function (See end)
            if len(bfsList) > 0:
                self.sortList(bfsList)

            #loop through the list, enqueing and adding elements to visited list if they aren't already visited
            for i in range(len(bfsList)):
                #If graph is weighted, grabs first element (Which will be the node name)
                if isinstance(bfsList[i], tuple):
                    if bfsList[i][0] not in visited:
                        bfsQueue.enqueue(bfsList[i][0])
                        visited.append(bfsList[i][0])
                else:
                    if bfsList[i] not in visited:
                        bfsQueue.enqueue(bfsList[i])
                        visited.append(bfsList[i])

        return visited
                
        

    def dfs(self, start):

        #Creates stack and output list, adds starting element to stack
        dfsStack = Stack()
        visited = []

        dfsStack.push(start)

        #Loop while stack isn't empty
        while dfsStack.isEmpty() == False:

            #Pops stack for node
            dfsNode = dfsStack.pop()

            #Searches if node has been processed already
            if dfsNode not in visited:
                visited.append(dfsNode)

                #Grabs list of next points, sorts list if list isn't empty
                dfsList = self.vertList[dfsNode]

                if len(dfsList) > 0:
                    self.sortList(dfsList)

                #Reverses list so it's added to stack properly
                dfsList.reverse()

                #Checks if nodes in next list has already been visited, if not, added to stack
                for i in range(len(dfsList)):
                    #If graph is weighted, grabs first value from tuple
                    if isinstance(dfsList[i], tuple):
                        if dfsList[i][0] not in visited:
                            dfsStack.push(dfsList[i][0])
                    else:
                        if dfsList[i] not in visited:    
                            dfsStack.push(dfsList[i])
                    
        
        return visited
    
    #Function to sort list
    def sortList(self, unsortedList):

        #if instance is a tuple, sorts accouring to fist value in tuple(name of node)
        if isinstance(unsortedList[0], (tuple,list)):
            unsortedList.sort(key=lambda i: i[0])
            return unsortedList
        #Otherwise, sorts by alphabetical order
        elif isinstance(unsortedList[0], str):
            unsortedList.sort()
            return unsortedList
        return


