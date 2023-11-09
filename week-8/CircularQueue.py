#define length 5
class CircularQueue:
    def __init__(self, length):
        self.maxSize = length 
        self.queue = [None] * length
        self.front = -1
        self.rear = -1
        self.__nItems = 0 
   
    def enqueue(self, val):
        if self.isFull():
            print("Queue is full")
            return
        if self.isEmpty():
           self.front +=1
        self.rear = (self.rear + 1) % self.maxSize
        self.queue[self.rear] = val
        self.__nItems += 1

    def dequeue(self):
        if self.isEmpty():
            print('Queue Underflow')
            return
        front = self.queue[self.front]
        self.queue[self.front] = None # Remove item reference
        self.__nItems-=1
        if self.front == self.rear:
           self.rear = self.front = -1
        else:
            self.front = (self.front + 1) % self.maxSize
        return front

    def isEmpty(self):
        return self.front == -1
    #Or
    # def isEmpty(self): return self.__nItems == 0
    

    def isFull(self):
        return (self.rear + 1) % self.maxSize == self.front

    # OR 
    # def isFull(self):  return self.__nItems == self.maxSize
    def peek(self):                    # Return frontmost item
      return None if self.isEmpty() else self.queue[self.front]

    def __len__(self):
        return self.__nItems 
    
    def __str__(self):
        if self.isEmpty():
            return "[]"
        result = "["
        for i in range(self.maxSize):
            result += str(self.queue[i]) + "\t"
        
        return result + "]"


# for person in ['Don', 'Ken', 'Ivan', 'Raj', 'Amir', 'Adi', 'Adil']:
#    queue.enqueue(person)
#    print(queue.front,"\t", queue.rear)
if __name__=="__main__":
    queue = CircularQueue(7)
    for i in range(7):
        queue.enqueue(i*2)
    print(queue.peek())
    print('After inserting', len(queue), 
        'persons on the queue, it contains:\n', queue)
    print('Is queue full?', queue.isFull())
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue("Rahim")
    print(queue.front,"\t", queue.rear)
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue.front,"\t", queue.rear)
    print(queue)
    queue.enqueue("Raheel")
    print(queue.front,"\t", queue.rear)
    print(queue)

    print('Removing items from the queue:')
    while not queue.isEmpty():
        print(queue.dequeue(), end=' ')
        print()

