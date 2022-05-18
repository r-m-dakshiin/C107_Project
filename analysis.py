import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')


student_df = df.loc[df['student_id'] == "TRL_987"]

fig = px.scatter(
    y=student_df.groupby("level")['attempt'].mean(),
    x=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    color=student_df.groupby("level")['attempt'].mean(),
    size=student_df.groupby("level")['attempt'].mean()
)
fig.show()