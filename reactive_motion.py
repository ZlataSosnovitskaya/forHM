import math
MODEL_G=9.8
DT=0.001  

# Сначала можно написать для любого тела движущегося под углом к горизонту (Класс "Тело")

class Body:
    def __init__(self,x,y,vx,vy):
        '''
        Парметры:
        x,y - начальные координаты
        vx,vy - начальная скорость
        '''
        self.x=x
        self.y=y

        self.vx=vx
        self.vy=vy

        self.trajectory_x = [] 
        self.trajectory_y = []

    def advance(self):  # Составление траектории тела, свободно движущегося под углом к горизонту

        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

        self.x+= self.vx*DT
        self.y+= self.vy*DT -MODEL_G*(DT**2)/2
        self.vy-=MODEL_G*DT
    
class Rocket(Body):
    def __init__(self,m,dm,v,M):
        '''
        Параметры:
        x,y-координаты в плоскости
        M-масса ракеты
        dm-масса газов, выбрасываемых за время DT
        m-масса газа в ракете
        v=скорость газов относительно ракеты
        '''
        self.m=m
        self.v=v
        self.dm=dm
        super().__init__(0,0, 15, 20) # Свойства тела переносятся на ракету
        self.a=v*dm/(DT*(M+m)) #Расчитаем ускорение, создаваемое реактивной силой
        self.dm=dm

    def advance(self):
        super().advance()
        while self.m>0:
            self.x+=self.a*self.vx/math.sqrt(self.vx**2+self.vy**2)*(DT**2)/2
            self.y+=self.a*self.vy/math.sqrt(self.vx**2+self.vy**2)*(DT**2)/2

            self.m-=self.dm

            self.vx+=self.a*self.vx/math.sqrt(self.vx**2+self.vy**2)*DT
            self.vy+=self.a*self.vy/math.sqrt(self.vx**2+self.vy**2)*DT


import numpy as np
'''
Зададим начальные параметры для тела и ракеты
'''
b = Body(0, 0, 15, 20)
r = Rocket(10,5,10,10)

bodies = [b, r]

'''
Теперь построим графики движения ракеты и тела в одной системе коррдинат для удобного сравнения
'''
for t in np.arange(0, 4, DT): 
    for b in bodies: 
        b.advance() 

from matplotlib import pyplot as pp

for b in bodies: 
    pp.plot(b.trajectory_x, b.trajectory_y)
pp.show()
