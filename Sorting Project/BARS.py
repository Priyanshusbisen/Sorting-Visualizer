import pygame
class Bars():
    def __init__(self,index,height):
        
        self.index = index 
        self.height = height
        self.rect = pygame.Rect(self.index*10+150,600-self.height,8,self.height)
        #self.rect = pygame.Rect(self.index*1,600-self.height,1,self.height)

    def Visualize(self,color,window):
        
        pygame.draw.rect(window,color,self.rect)
        pygame.display.update()        

    def move(self,new_pos,window):
        self.Visualize((255,255,255),window)
        self.rect.move_ip((new_pos,0))

        pygame.display.update()
