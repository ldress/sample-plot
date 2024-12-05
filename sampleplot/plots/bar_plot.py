import matplotlib.pyplot as plt

def plot_bar(data):
    plt.figure()
    plt.bar(data['categories'], data['values'])
    plt.title('Bar Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.savefig('bar_plot.png')
    plt.close()
