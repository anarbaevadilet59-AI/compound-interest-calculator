import matplotlib.pyplot as plt

def plot_growth(history):
    plt.plot(history)
    plt.xlabel("Months")
    plt.ylabel("Balance")
    plt.title("Investment Growth")
    plt.show()