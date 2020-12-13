import pandas as pd
import plotly_express as px

data = pd.read_csv("Covid.csv")
chart = px.scatter(data,x = "cases",y="date",color = "country",title = "Covid Data")
chart.show()