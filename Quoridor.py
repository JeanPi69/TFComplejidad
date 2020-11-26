#!/usr/bin/env python
# coding: utf-8

# In[267]:


import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd


# In[268]:


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

pos_muros = []


# In[269]:


def dibujar(fila, columna, pos_muros):
    tablero = np.zeros((17, 17, 3))
    tablero += 0.5 
    tablero[::2, ::2] = 1  
    tablero[1::2] = 0.5  
    
    for i in range(17):
        for j in range(17):
            if i % 2 != 0 and j % 2 != 0:
                tablero[i][j] = 0.2
    
    for i in range(len(pos_muros)):   
        if pos_muros[i][2] == 2:
            tablero[pos_muros[i][0] * 2 - 1][pos_muros[i][1] * 2] = 0
        if pos_muros[i][2] == 4:
            tablero[pos_muros[i][0] * 2 + 1][pos_muros[i][1] * 2] = 0
        if pos_muros[i][2] == 1:
            tablero[pos_muros[i][0] * 2][pos_muros[i][1] * 2 - 1] = 0
        if pos_muros[i][2] == 3:
            tablero[pos_muros[i][0] * 2][pos_muros[i][1] * 2 + 1] = 0
    
    fig, ax = plt.subplots()
    ax.imshow(tablero, interpolation = 'nearest')
    
    for i in range(len(fila)):
        ax.text(columna[i] * 2, fila[i] * 2, 'o', size = 18, ha = 'center', va = 'center', color = 'red')
        
    ax.set(xticks = [], yticks = [])
    ax.axis('image')
    
    plt.show()


# In[270]:


def Conexo(pos_x, pos_y, g):
    n = 9

    visitado = [[False for i in range(n)] for j in range(n)]
    aux = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def valid(x, y, dx, dy, g):
        if (x >= 0) and (x < n) and (y >= 0) and (y < n) and (g[x][y] != 2) and (not visitado[x][y]):
            for i in range(len(pos_muros)):
                if dx == 1 and pos_muros[i][2] == 2:
                    if pos_muros[i][0] == x and pos_muros[i][1] == y:
                        return False
                if dx == -1 and pos_muros[i][2] == 4:
                    if pos_muros[i][0] == x and pos_muros[i][1] == y:
                        return False
                if dy == 1 and pos_muros[i][2] == 1:
                    if pos_muros[i][0] == x and pos_muros[i][1] == y:
                        return False
                if dy == -1 and pos_muros[i][2] == 3:
                    if pos_muros[i][0] == x and pos_muros[i][1] == y:
                        return False
                if dx == -1 and pos_muros[i][2] == 2:
                    if pos_muros[i][0] == x + 1 and pos_muros[i][1] == y:
                        return False
                if dx == 1 and pos_muros[i][2] == 4:
                    if pos_muros[i][0] == x - 1 and pos_muros[i][1] == y:
                        return False
                if dy == -1 and pos_muros[i][2] == 1:
                    if pos_muros[i][0] == x and pos_muros[i][1] == y + 1:
                        return False
                if dy == 1 and pos_muros[i][2] == 3:
                    if pos_muros[i][0] == x and pos_muros[i][1] == y - 1:
                        return False
            return True
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

    cont = 0
    
    for i in range(n):
        for j in range(n):
            if not visitado[i][j]:
                BFS(pos_x, pos_y, g)
                cont += 1
    
    if cont == 1:
        return True
    else:
        return False


# In[271]:


def Algoritmo1(posX, posY, TipoG):
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

    def solve(posx, posy, g):    
        n = 9

        visitado = [[False for i in range(n)] for j in range(n)]
        aux = []

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def valid(x, y, dx, dy, g):
            if (x >= 0) and (x < n) and (y >= 0) and (y < n) and (g[x][y] != 2) and (not visitado[x][y]):
                for i in range(len(pos_muros)):
                    if dx == 1 and pos_muros[i][2] == 2:
                        if pos_muros[i][0] == x and pos_muros[i][1] == y:
                            return False
                    if dx == -1 and pos_muros[i][2] == 4:
                        if pos_muros[i][0] == x and pos_muros[i][1] == y:
                            return False
                    if dy == 1 and pos_muros[i][2] == 1:
                        if pos_muros[i][0] == x and pos_muros[i][1] == y:
                            return False
                    if dy == -1 and pos_muros[i][2] == 3:
                        if pos_muros[i][0] == x and pos_muros[i][1] == y:
                            return False
                    if dx == -1 and pos_muros[i][2] == 2:
                        if pos_muros[i][0] == x + 1 and pos_muros[i][1] == y:
                            return False
                    if dx == 1 and pos_muros[i][2] == 4:
                        if pos_muros[i][0] == x - 1 and pos_muros[i][1] == y:
                            return False
                    if dy == -1 and pos_muros[i][2] == 1:
                        if pos_muros[i][0] == x and pos_muros[i][1] == y + 1:
                            return False
                    if dy == 1 and pos_muros[i][2] == 3:
                        if pos_muros[i][0] == x and pos_muros[i][1] == y - 1:
                            return False
                return True
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
    
    arreglo = []
    root1, x1, y1 = solve(posX, posY, TipoG)
    arreglo = camino(arreglo, root1, x1, y1)
    aux = [x1, y1]
    arreglo.append(aux)
    return arreglo


# In[272]:


def muros(pos_x, pos_y, g):
    direccion = 0
    ruta = []
    ruta = Algoritmo1(pos_x, pos_y, g)
    x1 = ruta[1][0]
    y1 = ruta[1][1]
    x2 = 0
    y2 = 0
    direc, direc2 = x1 - pos_x, y1 - pos_y
    if direc == 0:
        if direc2 == 1:
            direccion = 1
        else:
            direccion = 3
    else:
        if direc == 1:
            direccion = 2
        else:
            direccion = 4       
            
    if direccion == 2:
        num = rd.randint(1, 2)
        if num == 1: x2, y2 = x1, y1 + 1
        else: x2, y2 = x1, y1 - 1 
    if direccion == 4:
        num = rd.randint(1, 2)
        if num == 1: x2, y2 = x1, y1 - 1
        else: x2, y2 = x1, y1 + 1
    if direccion == 1:
        num = rd.randint(1, 2)
        if num == 1: x2, y2 = x1 + 1, y1
        else: x2, y2 = x1 - 1, y1
    if direccion == 3:
        num = rd.randint(1, 2)
        if num == 1: x2, y2 = x1 - 1, y1
        else: x2, y2 = x1 + 1, y1
    
    if x2 >= 9 or x2 < 0 or y2 >= 9 or y2 < 0:
        return False
    
    for i in range(len(pos_muros)):
        if (pos_muros[i][0] == x1 and pos_muros[i][1] == y1 and pos_muros[i][2] == direccion) or (pos_muros[i][0] == x2 and pos_muros[i][1] == y2 and pos_muros[i][2] == direccion):
            return False         
                
    pos_muros.append((x1, y1, direccion))
    pos_muros.append((x2, y2, direccion))
    
    if not Conexo(pos_x, pos_y, g):
        pos_muros.pop(-1)
        pos_muros.pop(-1)
        return False
    
    return True

def BOT(arr_x, arr_y, pos_x, pos_y, g, dist, dist2, pos_x2, pos_y2, g2, cont):
    if dist <= dist2 or cont == 0 or not muros(pos_x2, pos_y2, g2):
        ruta = []
        ruta = Algoritmo1(pos_x, pos_y, g)
        dist = len(ruta)
        x1 = ruta[1][0]
        y1 = ruta[1][1]
        pos_x = x1
        pos_y = y1
        arr_x.append(x1)
        arr_y.append(y1)
    else:
        arr_x.append(pos_x)
        arr_y.append(pos_y)
        cont -= 1
    return arr_x, arr_y, pos_x, pos_y, dist, cont

def Start():
    pos_x, pos_y = 0, 4
    pos_x2, pos_y2 = 8, 4
    dist, dist2 = 0, 0
    arr_x, arr_y = [], []
    cont, cont2 = 10, 10
    
    arr_x.append(pos_x)
    arr_y.append(pos_y)
    arr_x.append(pos_x2)
    arr_y.append(pos_y2)
    dibujar(arr_x, arr_y, pos_muros)
    arr_x.pop(0)
    arr_y.pop(0)
    
    while True:
        arr_x, arr_y, pos_x, pos_y, dist, cont = BOT(arr_x, arr_y, pos_x, pos_y, g1, dist, dist2, pos_x2, pos_y2, g4, cont)
        dibujar(arr_x, arr_y, pos_muros)
        if g1[pos_x][pos_y] == 1:
            print("Ganador BOT TOP")
            break
        
        while len(arr_x) != 1:
            arr_x.pop(0)
            arr_y.pop(0)
            
        arr_x, arr_y, pos_x2, pos_y2, dist2, cont2 = BOT(arr_x, arr_y, pos_x2, pos_y2, g4, dist2, dist, pos_x, pos_y, g1, cont2)
        dibujar(arr_x, arr_y, pos_muros)
        
        while len(arr_x) != 1:
            arr_x.pop(0)
            arr_y.pop(0)
            
        if g4[pos_x2][pos_y2] == 1:
            print("Ganador BOT BOTTOM")
            break


# In[273]:


Start()


# In[ ]:





# In[ ]:




