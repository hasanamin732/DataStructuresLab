class LQueue:
    def __init__(self, length): #Constructor
        self.maxSize = length #size of array
        self.queue = [None] * length #queue stored as a list
        self.front = 0     
        self.rear = -1  #Empty queue has front -1
        self.__nItems = 0 #Initially no items in the queue
    
    def isEmpty(self):
         return self.front == self.rear + 1 or self.__nItems == 0
    
    def isFull(self):
        return self.rear == self.maxSize - 1 
    #or self.__nItems == self.maxSize

    def insert(self, value): #Enqueue
        if self.isFull():
            print("queue overflow")
            return
        self.rear += 1
        self.queue[self.rear] = value
        self.__nItems +=1
        print("inserted Item ", value, " in the queue. ")
    
    def remove(self):  # dequeue
        if self.isEmpty():
            print("Queue underflow")
            return

        print("Deleting element from the queue...")

        # Save the element to be removed
        front = self.queue[self.front]

        # Shift all elements ahead by one place
        for i in range(self.front, self.rear):
            self.queue[i] = self.queue[i + 1]

        # Set the last element to None and update rear
        self.queue[self.rear] = None
        self.rear -= 1

        self.__nItems -= 1
        return front

    
    def peek(self):                    # Return frontmost item
      return None if self.isEmpty() else self.queue[self.front]

    def __len__(self):
        return self.__nItems 
    
    def __str__(self):
        if self.isEmpty():
            return "[]"
        result = "["
        for i in range(self.front, self.rear+1):
            if len(result) > 1: # Except next to left bracket,
                result += ", " # separate items with comma
            result += str(self.queue[i]) # Add string form of item
            
        return result + "]"
if __name__=="__main__":
    qObj = LQueue(10)

    for i in range(qObj.maxSize):
        qObj.insert(i*2+1)

    print('After inserting', len(qObj), 
        'elements in the queue, it contains:\n', qObj)
    print('Is queue full?', qObj.isFull())
    print("Element deleted from the queue is:" , qObj.remove())
    print("Element deleted from the queue is:" , qObj.remove())
    print("Element deleted from the queue is:" , qObj.remove())
    print(qObj)
    print("Queue Size is:", qObj.maxSize)
    print("Number of Elements currently in Queue = ", len(qObj))
    print('Is queue full?', qObj.isFull())

    qObj.remove()
    print(qObj)


