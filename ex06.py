import pandas as pd
import matplotlib.pyplot as plt

def plot_graphic(teta,tal):
    plt.figure(figsize = (8,5))
    plt.style.use("ggplot")
    plt.tight_layout()
    plt.title("Torque vs Velocidade Mecâncica",fontsize=18)
    plt.plot(teta,tal, label="Torque")
    plt.xlabel(r'$n_{mec}$, rpm')
    plt.ylabel(r'$\tau_{ind}$, N.m')
    plt.xlim(0, max(teta))
    plt.ylim(0,)
    plt.legend()
    plt.grid(False)
    plt.show()

data = pd.read_excel("velocity_torque.xls")
velocity = (data["Velocidade Mecânica"]).values
torque = (data["Toque Induzido"]).values
plot_graphic(velocity, torque)