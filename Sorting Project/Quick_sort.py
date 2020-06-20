import time
from BARS import Bars

class Algo_quick_sort():

    
    def __init__(self,arr,low,high):
        size = high - low + 1
        self.stack = [0]*size
        self.top = -1
        self.top+=1
        self.stack[self.top] =  low
        self.top += 1
        self.stack[self.top] = high
        self.qsort = False

    def quick_sort(self,arr,window):
        
        
        
        if self.top >= 0:
            H = self.stack[self.top]
            self.top = self.top-1
            L = self.stack[self.top]
            self.top = self.top - 1
                        
            p = self.partition(arr,L,H,window)
                
            if p-1 > L:
                self.top = self.top + 1
                self.stack[self.top] = L
                self.top = self.top + 1
                self.stack[self.top] = p-1
                
                
            if p+1 < H: 
                self.top = self.top + 1
                self.stack[self.top] = p+1
                self.top = self.top + 1
                self.stack[self.top] = H
        if self.top == -1:
            for i in range(len(arr)):
                time.sleep(.02)
                arr[i].Visualize((0,255,0),window)
                
            self.qsort = True
            
                    
    def partition(self,arr,low,high,window):
        i = low
        j = high
        pivot = arr[low].height
        arr[i].Visualize((255,255,0),window)
        arr[j].Visualize((255,69,0),window)
        
        while i < j:
            arr[low].Visualize((0,128,0),window)
            
            while arr[i].height <= pivot and i<high:
                arr[i].Visualize((0,0,255),window)
                i+=1
                
                arr[i].Visualize((255,255,0),window)
                time.sleep(.02)
            while arr[j].height > pivot and j > low:
                arr[j].Visualize((0,0,255),window)
                j-=1
                
                arr[j].Visualize((255,69,0),window)
                time.sleep(.02)
                
            if i < j:
                arr[i].Visualize((255,255,255),window)
                arr[j].Visualize((255,255,255),window)
                bar1 = Bars(i,arr[j].height)
                bar2 = Bars(j,arr[i].height)
                arr[i] = bar1
                arr[j] = bar2
                arr[i].Visualize((0,0,255),window)
                arr[j].Visualize((0,0,255),window)

        arr[low].Visualize((255,255,255),window)
        arr[j].Visualize((255,255,255),window)
        bar1 = Bars(low,arr[j].height)
        bar2 = Bars(j,arr[low].height)
        arr[low] = bar1
        arr[j] = bar2
        arr[low].Visualize((0,0,255),window)
        arr[j].Visualize((0,0,255),window)
        return j
    
