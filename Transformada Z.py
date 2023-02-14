import numpy as np
import matplotlib.pyplot as plt

def transf_z(a, n):
    return np.array([a**k if k >= 0 else 0 for k in n]) # a^n*u(n)

def transf_fourier(a, w):
    return 1 / (1 - a * np.exp(-1j * w))

a = 0.5 # constante
n = np.arange(-10, 10)
w = np.linspace(-np.pi, np.pi, 1000) # frequencia para a Transf. Fourier

z = transf_z(a, n)
f = transf_fourier(a, w)

# Plotar a Transf. Z
plt.stem(n, z)
plt.title("x[n] = a^n * u(n)")
plt.xlabel("n")
plt.ylabel("")
plt.show()

# Plotar os pólos
Circ_Unit = np.exp(1j * np.linspace(0, 2*np.pi, 1000)) 
plt.plot(Circ_Unit.real, Circ_Unit.imag, 'k--') 
plt.plot(a, 0, 'x', color='red', markersize=10) 
plt.title("Posição dos Polos") 

plt.xlabel("Re") 
plt.ylabel("Im") 
plt.xlim(-2, 2) 
plt.ylim(-2, 2) 
plt.show()

# Definindo o tamanho da frequencia
w = np.linspace(0, 10, 1000)

# Definindo a função de transf.
H = transf_fourier(0.1, w)

# Plotando a magnitude
plt.figure()
plt.plot(w, 20*np.log10(abs(H)))
plt.xlabel('Frequencia')
plt.ylabel('Magnitude (dB)')
plt.title('Magnitude')
plt.grid()

# Plotando a fase
plt.figure()
plt.plot(w, np.angle(H))
plt.xlabel('Frequencia')
plt.ylabel('Fase (rad)')
plt.title('Fase')
plt.grid()

plt.show()
