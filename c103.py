import pandas as pd
import plotly.express as px

df = pd.read_csv("c103.csv")
print(df.date)
fig = px.scatter(df,    x="date",
                        y="cases",
                        color="country"
            )
fig.show()