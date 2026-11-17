# Simulação de Pêndulos Acoplados (Modelo Não-Linear Exato)

Este projeto implementa uma simulação numérica da dinâmica de **dois pêndulos simples acoplados por uma mola**. Diferente das abordagens clássicas que utilizam a aproximação de pequenos ângulos ($\sin \theta \approx \theta$), este código resolve o **modelo exato não-linear** do sistema utilizando computação simbólica e integração numérica em Python.

## Sobre o Modelo Físico

O sistema é composto por duas massas idênticas ($m$) suspensas por fios inextensíveis de mesmo comprimento ($l$), separadas na base por uma distância ${l}_{0}$ e conectadas entre si por uma mola de constante elástica $k$ e comprimento natural ${l}_{0}$.

### Formulação Matemática

1. **Cinemática:** As posições cartesianas $({x}_{1},{y}_{1})$ e $({x}_{2},{y}_{2})$ de cada massa são definidas em função dos ângulos ${\theta }_{1}$ e ${\theta }_{2}$ em relação à vertical.

2. **Energia Potencial (**$U$**):**

   * **Gravitacional (**${U}_{g}$**):** ${U}_{g}=-mgl\cos ({\theta }_{1})-mgl\cos ({\theta }_{2})$

   * **Elástica (**${U}_{k}$**):** ${U}_{k}=\frac{1}{2}k(d-{l}_{0}{)}^{2}$, onde $d=\sqrt{({x}_{2}-{x}_{1}{)}^{2}+({y}_{2}-{y}_{1}{)}^{2}}$ é a distância instantânea entre as massas.

3. **Equações de Movimento:** As acelerações angulares (${\ddot{\theta }}_{1}$ e ${\ddot{\theta }}_{2}$) são derivadas simbolicamente a partir do gradiente da energia potencial total ($U={U}_{g}+{U}_{k}$):

   $${\ddot{\theta }}_{i}=-\frac{1}{m{l}^{2}}\frac{\partial U}{\partial {\theta }_{i}}$$

## &nbsp;Tecnologias e Bibliotecas

* [**SymPy**](https://www.sympy.org/)**:** Utilizada para modelagem simbólica, cálculo das derivadas parciais da energia potencial e conversão das expressões analíticas em funções numéricas rápidas (`lambdify`).

* [**NumPy**](https://numpy.org/)**:** Manipulação de arrays, conversões angulares e geração da malha temporal.

* [**SciPy**](https://scipy.org/)**:** Resolução do sistema de Equações Diferenciais Ordinárias (EDOs) de primeira ordem utilizando o método de Runge-Kutta de ordem 5(4) (`solve_ivp` com `method='RK45'`).

* [**Matplotlib**](https://matplotlib.org/)**:** Visualização gráfica do comportamento oscilatório e da transferência de energia (batimento) entre os pêndulos ao longo do tempo.

## Parâmetros da Simulação

Os valores padrão configurados no script são:

| Parâmetro | Símbolo | Valor Padrão | Descrição |
| :---- | :---- | :---- | :---- |
| Massa | `m` | $1.0\text{ kg}$ | Massa de cada pêndulo |
| Comprimento | `l` | $1.0\text{ m}$ | Comprimento dos fios |
| Distância / Comp. Natural | `l0` | $1.0\text{ m}$ | Distância entre os pivôs e comprimento relaxado da mola |
| Constante Elástica | `k` | $15.0\text{ N/m}$ | Rigidez da mola de acoplamento |
| Gravidade | `g` | $9.81\text{ m/s}^2$ | Aceleração gravitacional local |

### Condições Iniciais

* **Pêndulo 1 (**${\theta }_{1}$**):** Deslocado a $3{0}^{\circ }$ em repouso (${\dot{\theta }}_{1}=0$).

* **Pêndulo 2 (**${\theta }_{2}$**):** Em equilíbrio na vertical (${0}^{\circ }$) e em repouso (${\dot{\theta }}_{2}=0$).

* **Tempo de Simulação:** $0$ a $10$ segundos ($1000$ pontos avaliados).

## Como Executar

### 1\. Pré-requisitos

Certifique-se de ter o Python 3 instalado junto com as dependências necessárias:

```
pip install numpy sympy scipy matplotlib

```

### 2\. Execução

Salve o código em um arquivo (por exemplo, `pendulos_acoplados.py`) e execute-o no terminal:

```
python pendulos_acoplados.py

```
## &nbsp;Resultado Esperado

Ao executar o código, uma janela gráfica será exibida mostrando a evolução temporal dos ângulos ${\theta }_{1}$ e ${\theta }_{2}$ (em graus). É possível observar claramente o fenômeno de **transferência de energia (batimento)**, onde a amplitude de oscilação passa alternadamente do Pêndulo 1 para o Pêndulo 2 devido ao acoplamento da mola.
