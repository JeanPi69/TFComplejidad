#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd
from datetime import datetime


# In[2]:


def dibujar(fila, columna, muros_v, muros_h):
    tablero = np.zeros((9, 9, 3))
    tablero += 0.8 
    tablero[::2, ::2] = 1  
    tablero[1::2, 1::2] = 1  
    
    fig, ax = plt.subplots()
    ax.imshow(tablero, interpolation = 'nearest')
    
    for i in range(len(fila)):
        ax.text(fila[i], columna[i], 'o', size = 25, ha = 'center', va = 'center')
    
    for x, y in enumerate(muros_v):
        if y != -1:
            ax.text(x, y, '__', size = 30, ha = 'center', va = 'center')
        
    for x, y in enumerate(muros_h):
        if y != -1:
            ax.text(y, x, ' |', size = 30, ha = 'left', va = 'center')
            
    
    ax.set(xticks = [], yticks = [])
    ax.axis('image')
    
    plt.show()


# In[3]:


def Create_muros(n):
    l_h = [None for _ in range(9)]
    l_v = [None for _ in range(9)]
    k = 0
    j = 0
    
    for i in range(n):
        sorteo = rd.randint(1, 2)
        aux = rd.randint(0, 7)
        
        if k > 7:
            sorteo = 2
        if j > 7:
            sorteo = 1
        
        if sorteo == 1:
            l_h[k] = aux
            k += 1
            l_h[k] = aux
            k += 1
            
        else:
            l_v[j] = aux
            j += 1
            l_v[j] = aux
            j += 1
    
    for i in range(9):
        if l_h[i] == None:
            l_h[i] = -1
        if l_v[i] == None:
            l_v[i] = -1
    
    return l_h, l_v


# In[4]:


g1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],]

g2 = [[0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],]

g3 = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],]

g4 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],]


# In[5]:


def camino(arr, root, x, y):
    if root[x][y] == None:
        return arr
    else:
        x, y = root[x][y]
        camino(arr, root, x, y)
        aux = [x, y]
        arr.append(aux)
        return arr
    
    return arr

def Algoritmo1(posx, posy, g):    
    n = 9

    visitado = [[False for i in range(n)] for j in range(n)]
    aux = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def valid(x, y, dx, dy, g):
        if (x >= 0) and (x < n) and (y >= 0) and (y < n) and (g[x][y] != 2) and (not visitado[x][y]):
            if dx == 1:
                if lineas_h[y] != x - 1:
                    return True
                else:
                    return False
            if dy == 1:
                if lineas_v[x] != y - 1:
                    return True
                else:
                    return False
            if dx == -1:
                if lineas_h[y] != x:
                    return True
                else:
                    return False
            if dy == -1:
                if lineas_v[x] != y:
                    return True
                else:
                    return False
        else:
            return False


    def BFS(fila, columna, g):
        aux.append((fila, columna))
        visitado[fila][columna] = True
        root = [[None for i in range(n)] for j in range(n)]
    
        while len(aux) > 0:
            x, y = aux.pop(0)
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if valid(nx, ny, dx[i], dy[i], g):
                    visitado[nx][ny] = True
                    aux.append((nx, ny))
                    root[nx][ny] = x, y
                    if g[nx][ny] == 1:
                        return root, nx, ny
    
    raiz, x, y = BFS(posx, posy, g)
    return raiz, x, y           


# In[6]:


def Start(activacion):
    cont, cont2, cont3, cont4 = 0, 0, 0, 0
    arr = []
    arr2 = []
    arr3 = []
    arr4 = []
    arr_x = []
    arr_y = []
    
    if activacion[0] == 1:
        root1, x1, y1 = Algoritmo1(0, 4, g1)
        arr = camino(arr, root1, x1, y1)
        aux = [x1, y1]
        arr.append(aux)
        
    if activacion[1] == 1:
        root2, x2, y2 = Algoritmo1(8, 4, g4)
        arr2 = camino(arr2, root2, x2, y2)
        aux2 = [x2, y2]
        arr2.append(aux2)
        
    if activacion[2] == 1:
        root3, x3, y3 = Algoritmo1(4, 8, g3)
        arr3 = camino(arr3, root3, x3, y3)
        aux3 = [x3, y3]
        arr3.append(aux3)   
        
    if activacion[3] == 1:
        root4, x4, y4 = Algoritmo1(4, 0, g2)
        arr4 = camino(arr4, root4, x4, y4)
        aux4 = [x4, y4]
        arr4.append(aux4)  
    
    while cont < len(arr) or cont2 < len(arr2) or cont3 < len(arr3) or cont4 < len(arr4):
        arr_x = []
        arr_y = []
        
        if cont < len(arr):
            x1 = arr[cont][0]
            y1 = arr[cont][1]
            arr_x.append(x1)
            arr_y.append(y1)
            cont += 1
        
        if len(arr2) > 0:
            if cont2 > 0:
                arr_y.append(y2)
                arr_x.append(x2)
            if cont3 > 0:
                arr_y.append(y3)
                arr_x.append(x3)
            if cont4 > 0:
                arr_y.append(y4)
                arr_x.append(x4)

            dibujar(arr_y, arr_x, lineas_h, lineas_v)    

            if cont2 > 0:
                arr_y.pop()
                arr_x.pop()
            if cont3 > 0:
                arr_y.pop()
                arr_x.pop()
            if cont4 > 0:
                arr_y.pop()
                arr_x.pop()
    
        if cont2 < len(arr2):
            x2 = arr2[cont2][0]
            y2 = arr2[cont2][1]
            arr_x.append(x2)
            arr_y.append(y2)
            cont2 += 1 
        
        if len(arr3) > 0:
            if cont3 > 0:
                arr_y.append(y3)
                arr_x.append(x3)
            if cont4 > 0:
                arr_y.append(y4)
                arr_x.append(x4)

            dibujar(arr_y, arr_x, lineas_h, lineas_v)    

            if cont3 > 0:
                arr_y.pop()
                arr_x.pop()
            if cont4 > 0:
                arr_y.pop()
                arr_x.pop()
        
        if cont3 < len(arr3):
            x3 = arr3[cont3][0]
            y3 = arr3[cont3][1]
            arr_x.append(x3)
            arr_y.append(y3)
            cont3 += 1
        
        if len(arr4) > 0:
            if cont4 > 0:
                arr_y.append(y4)
                arr_x.append(x4)

            dibujar(arr_y, arr_x, lineas_h, lineas_v)    

            if cont4 > 0:
                arr_y.pop()
                arr_x.pop()
            
        if cont4 < len(arr4):
            x4 = arr4[cont4][0]
            y4 = arr4[cont4][1]
            arr_x.append(x4)
            arr_y.append(y4)
            cont4 += 1 
        
        dibujar(arr_y, arr_x, lineas_h, lineas_v)
        
        if cont == len(arr) and len(arr) != 0:
            print("Ganador bot top")
            break
        if cont2 == len(arr2) and len(arr2) != 0:
            print("Ganador bot bottom")
            break
        if cont3 == len(arr3) and len(arr3) != 0:
            print("Ganador bot right")
            break
        if cont4 == len(arr4) and len(arr4) != 0:
            print("Ganador bot left")
            break


# In[7]:


print("Numero de barreras que quieres del 1 al 8:")
n_barreras = int(input())

lineas_h, lineas_v = Create_muros(n_barreras)
dibujar([], [], lineas_h, lineas_v)
  
print("Elige cuantos jugadores quieres del 1 al 4:")
n = int(input())

if n == 1:
    activate = [1, 0, 0, 0]
elif n == 2:
    activate = [1, 1, 0, 0]
elif n == 3:
    activate = [1, 1, 1, 0]
else:
    activate = [1, 1, 1, 1]
    
Start(activate) 


# In[ ]:




