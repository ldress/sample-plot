import matplotlib.pyplot as plt

def plot_line(data):
    plt.figure()
    plt.plot(data['x'], data['y'])
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig('line_plot.png')
    plt.close()
