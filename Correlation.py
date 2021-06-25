import csv
import plotly.express as px
import numpy as np

def plot_figure(data_path):
    with open(data_path)as f:
        df = csv.DictReader(f)
        graph=px.scatter(df, x='Days', y='Marks')
        graph.show()
def get_data_source(data_path):
    temperature = []
    ice_cream = []
    with open(data_path)as f :
        df = csv.DictReader(f)
        for i in df:
            temperature.append(float(i['Days']))
            ice_cream.append(float(i['Marks']))
    return {
        'x':temperature,
        'y': ice_cream
    }
def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])
def setup():
    data_path ='./data4.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_path)
setup()


