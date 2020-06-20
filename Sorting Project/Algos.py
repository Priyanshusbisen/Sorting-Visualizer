import pygame
from BARS import Bars
import time

sort = False

def Selection_sort(all_rects,bar,window):
    global sort
    
    
    print(sort)
    min_pos = bar.index
    for i in range(bar.index,len(all_rects)):
        all_rects[i].Visualize((255,0,0),window)
        
        all_rects[i].Visualize((0,0,255),window)
        if all_rects[i].height < all_rects[min_pos].height:
            min_pos = i
    
    all_rects[bar.index].index, all_rects[min_pos].index = min_pos, bar.index
    
    all_rects[bar.index], all_rects[min_pos] = all_rects[min_pos], all_rects[bar.index]
    all_rects[bar.index].move((bar.index-min_pos)*10,window)
    all_rects[min_pos].move((min_pos-bar.index)*10,window)
    if all_rects[bar.index].index == all_rects[min_pos].index:
        all_rects[bar.index].Visualize((0,255,0),window)
    else:    
        all_rects[bar.index].Visualize((0,255,0),window)
        all_rects[min_pos].Visualize((0,0,255),window)
    if bar.index == len(all_rects)-1:
        sort = True

      
        


def Insertion_sort(all_rects,bar,window):
    global sort
    
    pos = bar.index
    if bar.index == len(all_rects)-1:
        sort = True
        print('Sorted',sort)
    
        
    while pos > 0 and all_rects[pos].height < all_rects[pos-1].height:
        all_rects[pos].index, all_rects[pos-1].index = all_rects[pos-1].index, all_rects[pos].index
        all_rects[pos], all_rects[pos-1] = all_rects[pos-1], all_rects[pos]
        all_rects[pos-1].move(-10,window)
        all_rects[pos].move(10,window)
        all_rects[pos-1].Visualize((0,0,255),window)
        all_rects[pos].Visualize((0,255,0),window)
        pygame.display.update()
        pos = pos -1
        

def mergeSort(all_rects,count,window):  
    global sort  
    current_size = 2**count
      
    # Outer loop for traversing Each  
    # sub array of current_size  
    
          
    left = 0
        # Inner loop for merge call  
        # in a sub array  
        # Each complete Iteration sorts  
        # the iterating sub array  
    while left < len(all_rects)-1:  
              
            # mid index = left index of  
            # sub array + current sub  
            # array size - 1  
        mid = min((left + current_size - 1),(len(all_rects)-1)) 
              
            # (False result,True result)  
            # [Condition] Can use current_size  
            # if 2 * current_size < len(a)-1  
            # else len(a)-1  
        right = ((2 * current_size + left - 1,  
                    len(all_rects) - 1)[2 * current_size  
                        + left - 1 > len(all_rects)-1])  
                              
            # Merge call for each sub array  
        merge(all_rects, left, mid, right,window)  
        left = left + current_size*2

    if current_size >= len(all_rects)//2:
        for i in range(len(all_rects)):
            all_rects[i].Visualize((0,255,0),window)
            time.sleep(.02)
        sort = True
    
  
# Merge Function  
def merge(all_rects, l, m, r,window):  
    n1 = m - l + 1
    n2 = r - m  
    L = all_rects[l:m+1]   
    R = all_rects[m+1:r+1]  
      
  
    i, j, k = 0, 0, l  
    while i < n1 and j < n2:  
        if L[i].height > R[j].height:
            
            all_rects[k].Visualize((255,255,255),window)
            bar = Bars(k,R[j].height)
            bar.Visualize((0,255,0),window)
            time.sleep(.02)
            bar.Visualize((0,0,255),window)
            all_rects[k] = bar
            j += 1
            
            
        else:  
            all_rects[k].Visualize((255,255,255),window)
            
            bar = Bars(k,L[i].height)
        
            bar.Visualize((0,255,0),window)
            time.sleep(.02)
            bar.Visualize((0,0,255),window)
            
            all_rects[k] = bar
            

            i += 1

        k += 1
  
    while i < n1:  
        all_rects[k].Visualize((255,255,255),window)
        bar = Bars(k,L[i].height)

        bar.Visualize((0,255,0),window)
        time.sleep(.02)
        bar.Visualize((0,0,255),window)

        all_rects[k] = bar
        

        i += 1
        k += 1
  
    while j < n2:  
        all_rects[k].Visualize((255,255,255),window)
        
        bar = Bars(k,R[j].height)
        
        bar.Visualize((0,255,0),window)
        time.sleep(.02)
        bar.Visualize((0,0,255),window)

        all_rects[k] = bar

        j += 1
        k += 1

def Bubble_sort(arr,count,window):
    global sort
    i = 0
    while i < len(arr)-count-1:
        if arr[i].height > arr[i+1].height:
                
            arr[i].move(10,window)
            arr[i+1].move(-10,window)
            arr[i].Visualize((0,0,255),window)
            arr[i+1].Visualize((0,0,255),window)
            arr[i],arr[i+1] = arr[i+1],arr[i]
        
        i+=1
    arr[len(arr)-count-1].Visualize((0,255,0),window)
    if count == len(arr)-2:
        sort = True
        print('sorted')








                
