from LQueue import LQueue

class Waiting:
    def __init__(self,MaxSize):
        self.maxsize=MaxSize
        self.queue=LQueue(self.maxsize)
        self.record={}
    def RegisterPatient(self,name):
        if self.queue.isEmpty():
            id=1
            
        else:
            id=self.queue.peek()+len(self.queue)
        self.queue.insert(id)
        self.record[id]=name
        return id
    def ServePatient(self):
        ServedPatient=self.queue.remove()
        self.record.pop(ServedPatient)
        return self.queue.peek(),self.record[self.queue.peek()] #returning the id and name of next patient in the queue
    def CancelAll(self):
        while not self.queue.isEmpty():
            self.queue.remove()
    def CanDoctorGoHome(self):
        return self.queue.isEmpty()
    
    def ShowAllPatients(self):
        sortedDict=dict(sorted(self.record.items(), key=lambda x:x[1]))
        return sortedDict
    
if __name__=="__main__":
    room= Waiting(5)
    room.RegisterPatient("Sara")
    room.RegisterPatient("HasanAmin")
    room.RegisterPatient("Ali")
    room.RegisterPatient("Ahmed")
    print(room.ShowAllPatients())
    room.ServePatient()
    print(room.ShowAllPatients())
    print(room.CanDoctorGoHome())
    print(room.CancelAll())
    print(room.CanDoctorGoHome())
    # Working Fine