integerArray = [1, 1, 2, 3, 5] # A list of 5 integers
charArray = ['a' for j in range(1000)] # 1,000 letter ’a’ characters
booleArray = [False] * 32768 # 32,768 binary False values

maxSize = 10000
myArray = [None] * maxSize
myArraySize = 0

# Implement an Array data structure as a simplified type of list. 

class Array:
   def __init__(self, initialSize):    # Constructor
      self.__a = [None] * initialSize  # The array stored as a list
      self.__nItems = 0                # No items in array initially
   def __len__(self):                  # Special def for len() func
      return self.__nItems             # Return number of items
   
   def isEmpty(self):
      return int(self.__nItems) == 0  #checks if length == 0
   
   def isFull(self):
      return int(self.__nItems) == len(self.__a)   #Length == maxSize
    
   def get(self, n):                   # Return the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
         return self.__a[n]            # only return item if in bounds
   
   def insertAtEnd(self, item):             # Insert item at end
      if not self.isFull():
        self.__a[self.__nItems] = item   # Item goes at current end
        self.__nItems += 1               # Increment number of items
      else:
         print("List is Full. Insertion not possible")

   def insertAtPosition(self, position, value):            # Set the value at index n
    if not self.isFull():
         if position >=1 and position <= self.__nItems: # Check if n is in bounds, and
            if position == self.__nItems+1:
               self.insertAtEnd(value)
            else:
                self.MakeRoom(position)
                self.__a[position-1] = value           # only set item if in bounds
                self.__nItems += 1 
    else:
       print("List is Full. Insertion not possible")
   
    
   def MakeRoom(self, position):
       i=self.__nItems
       while i >= position:
           self.__a[i] =self.__a[i-1]
           i -=1

   def find(self, item):               # Find index for item
      for j in range(self.__nItems):   # Among current items
         if self.__a[j] == item:       # If found,
            return j                   # then return index to item
      return -1                        # Not found -> return -1
   
   def search(self, item):             # Search for item
      return self.get(self.find(item)) # and return item if found

   def delete(self, item):             # Delete first occurrence
      for j in range(self.__nItems):   # of an item
         if self.__a[j] == item:       # Found item
            self.__nItems -= 1         # One fewer at end
            for k in range(j, self.__nItems):  # Move items from
               self.__a[k] = self.__a[k+1]     # right over 1
            return True                # Return success flag
      
      return False     # Made it here, so couldn't find the item   

   def traverse(self, function=print): # Traverse all items
      if not self.isEmpty():
        for j in range(self.__nItems):   # and apply a function
            function(f"Position: {j+1} value: {self.__a[j]}")
   # Task 1a & 1b
   def deleteMaxNum(self):
      curr_max=None
      for i in self.__a:
         if isinstance(i,(int,float)):
            if curr_max==None:
               curr_max=i
            elif i>curr_max:
               curr_max=i
      if curr_max is not None:
         self.delete(curr_max)
         return f"Removed {curr_max}"
      else:
         return f"No number to return"
   def removeDupes(self):
      new=[]
      for i in range(len(self.__a)):
         
         if self.__a[i] in new:
            pass
         else:
            new.append(self.__a[i])
      self.__a=new
   
      
