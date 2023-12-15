import numpy as np
import matplotlib.pyplot as plt

def mackey_glass(beta, gamma, tau, n, dt, timesteps):
    x = np.zeros(timesteps)
    x[0] = 0.5  
  # Initial condition

    for t in range(1, timesteps):
        x_tau = x[max(0, t - int(tau / dt))]  
        dx_dt = beta * x_tau / (1 + x_tau**n) - gamma * x[t-1]
        x[t] = x[t-1] + dt * dx_dt

    return x

beta = 0.2
gamma = 0.1
tau = 17
n = 10
dt = 0.1
timesteps = 1000
mg_series = mackey_glass(beta, gamma, tau, n, dt, timesteps)

plt.plot(mg_series)
plt.xlabel('Time Steps')
plt.ylabel('x(t)')
plt.show()
