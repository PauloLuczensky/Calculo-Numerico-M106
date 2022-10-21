# -*- coding: utf-8 -*-
# importa a biblioteca NumPy
import numpy as np
#matriz dos coeficientes A  cria a matriz A2x2 
A = np.array([[3,2,2],[1,2,-1],[1,2,3]])
#vetor dos termos independentes B  cria a matriz b2x1
b = np.array([-3,2,-2]) 
#cálculo da solução do sistema  cria o vetor solução x
x = np.linalg.solve(A, b) 
#mostra o vetor solução
print('X = ', x)

