
import argparse
import yaml
from sampleplot.utils.data_loader import load_data
from sampleplot.plots.line_plot import plot_line
from sampleplot.plots.bar_plot import plot_bar

def parse_args():
    parser = argparse.ArgumentParser(description='SamplePlot: A simple plotting tool.')
    parser.add_argument('config', help='Path to the YAML configuration file.')
    return parser.parse_args()

def main():
    args = parse_args()
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    data_path = config.get('data_path')
    data = load_data(data_path)

    plots = config.get('plots', [])
    if 'line_plot' in plots:
        plot_line(data)
    if 'bar_plot' in plots:
        plot_bar(data)

if __name__ == '__main__':
    main()
