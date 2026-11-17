import numpy as np 
import sympy as sm
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
t = sm.symbols
m, l, l0, k, g  = sm.symbols ('m l l0 k  g', positive=True)
theta1, theta2 = sm.symbols('theta1 theta2')


x1 = l*sm.sin(theta1) 
y1 = -l*sm.cos(theta1)
x2 = l0+l*sm.sin(theta2)
y2 = -l*sm.cos(theta2)

dx = x2 - x1
dy = y2 - y1
d = sm.sqrt(dx**2 + dy**2)

Ug = -m*g*l*sm.cos(theta1) - m*g*l*sm.cos(theta2)
Uk = 0.5*k*(d - l0)**2
U = Ug + Uk

theta1_dd_expr = -sm.diff(U, theta1)/(m*l**2)
theta2_dd_expr = -sm.diff(U, theta2)/(m*l**2)

cal_aceleracoes = sm.lambdify(
    (theta1, theta2, m, l, l0, k, g),
    [theta1_dd_expr, theta2_dd_expr],
    modules='numpy'
)

params={

     'm':1.0,
     "l":1.0,
     "l0":1.0,
     'k':15.0,
     'g':9.81

}

def sistema_edo(t, estado):
    th1, th1_ponto, th2, th2_ponto = estado
    th1_dois_pontos, th2_dois_pontos = cal_aceleracoes(
        th1, th2, params['m'], params['l'], params['l0'], params['k'], params['g']
    )
    return [th1_ponto, th1_dois_pontos, th2_ponto, th2_dois_pontos]

# condição inicial o pêndulo 1 de 30 graus (em radianos) e o pêndulo 2 do repouso
th1_inicial = np.radians(30)
th2_inicial = np.radians(0)
estado_inicial = [th1_inicial, 0.0, th2_inicial, 0.0]


tempo_simulacao = (0, 10)
tempo_pontos = np.linspace(0, 10, 1000)

solucao = solve_ivp(
    sistema_edo,
    tempo_simulacao, 
    estado_inicial, 
    t_eval=tempo_pontos, 
    method='RK45'
)
plt.figure(figsize=(10, 5))
plt.plot(solucao.t, np.degrees(solucao.y[0]), label='Pêndulo 1 ($\theta_1$)')
plt.plot(solucao.t, np.degrees(solucao.y[2]), label='Pêndulo 2 ($\theta_2$)')
plt.title('Oscilação dos Pêndulos Acoplados (Modelo Exato Não-Linear)')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (graus)')
plt.legend()
plt.grid(True)
plt.show()
