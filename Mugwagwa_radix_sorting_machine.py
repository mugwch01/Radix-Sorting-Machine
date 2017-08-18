#My name is Charles Mugwagwa. I'm writing an algorithm that simulates a radix punch card sorting machine.

import random
import queue     #queue.py contains the class Queue

class RadixMachine:
    def __init__(self):
        self.mainBin = queue.Queue()
        self.binList = []
        self.zeroBin = queue.Queue()
        self.oneBin = queue.Queue()
        self.twoBin = queue.Queue()
        self.threeBin = queue.Queue()
        self.fourBin = queue.Queue()
        self.fiveBin = queue.Queue()
        self.sixBin = queue.Queue()
        self.sevenBin = queue.Queue()
        self.eightBin = queue.Queue()
        self.nineBin = queue.Queue()
        self.binList.append(self.zeroBin)
        self.binList.append(self.oneBin)
        self.binList.append(self.twoBin)
        self.binList.append(self.threeBin)
        self.binList.append(self.fourBin)
        self.binList.append(self.fiveBin)
        self.binList.append(self.sixBin)
        self.binList.append(self.sevenBin)
        self.binList.append(self.eightBin)
        self.binList.append(self.nineBin) #all bins contained in self.binList        
               
    def load(self, adeck):   #adeck>>type='list'+ mainBin>>type='Queue'.    
        for x in adeck:           
            self.mainBin.enqueue((x)) #Loading mainBin and converting to strings              
        
    def go(self):
        outeroptions=['o','t','h']
        for variable in outeroptions: #3 processe       
            while not self.mainBin.isEmpty():
                item = self.mainBin.dequeue()
                onesDigit = item%10
                tensDigit = (item//10)%10
                hundredsDigit = item//100                
                if variable == 'o':
                    operation = onesDigit
                elif variable == 't':
                    operation = tensDigit
                else:
                    operation = hundredsDigit                    
                              
                if operation == 0:
                    self.zeroBin.enqueue(item)
                elif operation == 1:
                    self.oneBin.enqueue(item)
                elif operation == 2:
                    self.twoBin.enqueue(item)
                elif operation == 3:
                    self.threeBin.enqueue(item)
                elif operation == 4:
                    self.fourBin.enqueue(item)
                elif operation == 5:
                    self.fiveBin.enqueue(item)
                elif operation == 6:
                    self.sixBin.enqueue(item)
                elif operation == 7:
                    self.sevenBin.enqueue(item)
                elif operation == 8:
                    self.eightBin.enqueue(item)
                elif operation == 9:
                    self.nineBin.enqueue(item)           
            while not self.zeroBin.isEmpty():   #Putting everything back to mainBin
                self.mainBin.enqueue(self.zeroBin.dequeue())
            while not self.oneBin.isEmpty():
                self.mainBin.enqueue(self.oneBin.dequeue())
            while not self.twoBin.isEmpty(): 
                self.mainBin.enqueue(self.twoBin.dequeue())
            while not self.threeBin.isEmpty():  
                self.mainBin.enqueue(self.threeBin.dequeue())
            while not self.fourBin.isEmpty(): 
                self.mainBin.enqueue(self.fourBin.dequeue())
            while not self.fiveBin.isEmpty():
                self.mainBin.enqueue(self.fiveBin.dequeue())
            while not self.sixBin.isEmpty():  
                self.mainBin.enqueue(self.sixBin.dequeue())
            while not self.sevenBin.isEmpty():
                self.mainBin.enqueue(self.sevenBin.dequeue())
            while not self.eightBin.isEmpty(): 
                self.mainBin.enqueue(self.eightBin.dequeue())
            while not self.nineBin.isEmpty():  
                self.mainBin.enqueue(self.nineBin.dequeue())                  
                
    def unload(self):
        self.sorteddeck = []       
        while not self.mainBin.isEmpty():                   
            self.sorteddeck.append(self.mainBin.dequeue())  
            self.mainBin.isEmpty() 
        return self.sorteddeck    #This must return a list<iterable>             
            
def main(howmany):
    rm = RadixMachine()     
    deck = []     #deck is a list     
    for i in range(howmany):
        temp = random.randrange(1000)
        deck.append(temp)    
    rm.load(deck) #takes list as parameter    
    rm.go()    
    sorteddeck = rm.unload()  #sorteddeck is a list<iterable>    
    for item in sorteddeck:
        print(item)   
main(50)
