import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("mobileRating.csv")

graph = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"])
graph.show()