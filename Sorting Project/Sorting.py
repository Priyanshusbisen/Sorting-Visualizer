try:
    import pygame
    from pygame import *
    import time
    import random
    import tkinter
    from tkinter import *
    from Algos import Selection_sort,Insertion_sort,mergeSort,Bubble_sort
    from Quick_sort import Algo_quick_sort
    from BARS import Bars
except:
    import install_requirements
    import pygame
    from pygame import *
    import time
    import random
    import tkinter
    from tkinter import *
    from Algos import Selection_sort,Insertion_sort,mergeSort,Bubble_sort
    from Quick_sort import Algo_quick_sort
    from BARS import Bars

pygame.init()

class MainScreen:
   
    def __init__(self,width,height):
        
        self.screen_width = width
        self.screen_height = height
        self.window = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.window.fill((255,255,255))
        
        
    def create_screen(self):
        all_rects = []
        global test_list
        for i in range(len(test_list)):
            bar = Bars(i,test_list[i])
            all_rects.append(bar)
            bar.Visualize((0,0,255),self.window)
            
        pygame.display.update()

        self.process(all_rects)
    def process(self,all_rects):
        global var
        import Algos
        loop = True
        
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        loop = False
                        break
        count = 0
        quick_sort_algo = Algo_quick_sort(all_rects,0,len(all_rects)-1)
        while not Algos.sort:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
            
            
            if var.get() == 1:
                Selection_sort(all_rects,Bars(count,all_rects[count].height),self.window)
            elif var.get() == 2:
                Insertion_sort(all_rects,Bars(count,all_rects[count].height),self.window)
            elif var.get() == 3:
                Bubble_sort(all_rects,count,self.window)
            elif var.get() == 4:
                mergeSort(all_rects,count,self.window)
            elif var.get() == 5:    
                quick_sort_algo.quick_sort(all_rects,self.window)
            
            
            count+=1
            
            pygame.display.update()
            
            
            
                
        

            
class tkscreen():
    def __init__(self):
        global var
        self.tkwindow = Tk()
        var = IntVar()
    def create_tkwindow(self):
        
        self.label = Label(self.tkwindow,text = 'Choose one Algorithm')
        self.label.pack()
        self.RButton1 = Radiobutton(self.tkwindow,text = 'Selection Sort', variable = var,value = 1)
        self.RButton1.pack()
        self.RButton2 = Radiobutton(self.tkwindow,text = 'Insertion Sort', variable = var,value = 2)
        self.RButton2.pack()
        self.RButton3 = Radiobutton(self.tkwindow,text = 'Bubble Sort',variable = var,value = 3)
        self.RButton3.pack()
        self.RButton4 = Radiobutton(self.tkwindow,text = 'Merge Sort',variable = var,value = 4)
        self.RButton4.pack()
        self.RButton5 = Radiobutton(self.tkwindow,text = 'Quick Sort',variable = var,value = 5)
        self.RButton5.pack()
        self.button = Button(self.tkwindow,text = 'Submit', command = self.submit)
        self.button.pack()
        self.tkwindow.mainloop()

    def submit(self):
        screen = MainScreen(1300,600)
        screen.create_screen()
        self.tkwindow.destroy()


test_list = []   
for i in range(100):
    test_list.append(random.randint(1,600))
 
def main():
    obj = tkscreen()
    obj.create_tkwindow()
    
main()

