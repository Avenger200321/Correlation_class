import plotly.express as px 
import csv 
with open('data2.csv') as f:
    df = csv.DictReader(f)
    graph = px.scatter(df, x = 'TV', y='Time')
    graph.show()