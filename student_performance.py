import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import numpy as np
import plotly.express as px


# Reading the data
print(os.listdir(r'C:/Users/ata-d/'))
data = pd.read_csv(r'C:/Users/ata-d/OneDrive/Masaüstü/ML/Datasets/StudentsPerformance.csv')
data.info()

# ----------------------------------------------------------------------------------------------------------------------

# Gender vs Exam Results
scores_gender = data[['math score', 'reading score', 'writing score']].groupby(data['gender']).mean()

# ----------------------------------------------------------------------------------------------------------------------

# Race/Ethnicity vs Exam Results
scores_race = data[['math score', 'reading score', 'writing score']].groupby(data['race/ethnicity']).mean()

# ----------------------------------------------------------------------------------------------------------------------

# Lunch vs Exam Results
scores_lunch = data[['math score', 'reading score', 'writing score']].groupby(data['lunch']).mean()

# ----------------------------------------------------------------------------------------------------------------------

# Parental Level of Education vs Exam Results
scores_parental = data[['math score', 'reading score', 'writing score']].groupby(
    data['parental level of education']).mean()

# ----------------------------------------------------------------------------------------------------------------------

# Test Preparation Course vs Exam Results
scores_preparation = data[['math score', 'reading score', 'writing score']].groupby(
    data['test preparation course']).mean()

# ----------------------------------------------------------------------------------------------------------------------

# Distribution of the Gender
gender_counts = data['gender'].value_counts()
fig = go.Figure(data=[go.Pie(labels=gender_counts.index, values=gender_counts, opacity=0.9)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Distribution of the Gender', title_x=0.5, title_font=dict(size=20))
fig.show()

# Distribution of the Race/Ethnicity
race_counts = data['race/ethnicity'].value_counts()
fig = go.Figure(data=[go.Pie(labels=race_counts.index, values=race_counts, opacity=0.9)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Distribution of the Race/Ethnicity', title_x=0.5, title_font=dict(size=20))
fig.show()

# Distribution of the Parental Level of Education
parental_counts = data['parental level of education'].value_counts()
fig = go.Figure(data=[go.Pie(labels=parental_counts.index, values=parental_counts, opacity=0.9)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Distribution of the Parental Level of Education', title_x=0.5, title_font=dict(size=20))
fig.show()

# Distribution of the Lunch
lunch_counts = data['lunch'].value_counts()
fig = go.Figure(data=[go.Pie(labels=lunch_counts.index, values=lunch_counts, opacity=0.9)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Distribution of the Lunch', title_x=0.5, title_font=dict(size=20))
fig.show()

# Distribution of the Test Preparation Course
preparation_counts = data['test preparation course'].value_counts()
fig = go.Figure(data=[go.Pie(labels=preparation_counts.index, values=preparation_counts, opacity=0.9)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(title_text='Distribution of the Test Preparation Course', title_x=0.5, title_font=dict(size=20))
fig.show()

# Average Exam Scores vs. Genders
'''''''''
fig = go.Figure(data=[
    go.Bar(name='Average Math Scores', x=scores_gender.index, y=scores_gender['math score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Reading Scores', x=scores_gender.index, y=scores_gender['reading score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Writing Scores', x=scores_gender.index, y=scores_gender['writing score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside')
])

fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})

fig.update_yaxes(title_text="Average Scores", title_font={"size": 14})
fig.update_xaxes(title_text="Gender", title_font={"size": 14})

fig.update_layout(title_text='Average Exam Scores for each Gender',
                  title_x=0.5, title_font=dict(size=20))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Average Exam Scores vs. Race/Ethnicity
'''''''''
fig = go.Figure(data=[
    go.Bar(name='Average Math Scores', x=scores_race.index, y=scores_race['math score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Reading Scores', x=scores_race.index, y=scores_race['reading score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Writing Scores', x=scores_race.index, y=scores_race['writing score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside')
])

fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})

fig.update_yaxes(title_text="Average Scores", title_font={"size": 14})
fig.update_xaxes(title_text="Race/Ethnicity", title_font={"size": 14})

fig.update_layout(title_text='Average Exam Scores for each Race/Ethnicity',
                  title_x=0.5, title_font=dict(size=20))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Average Exam Scores vs. Parental Level of Education
'''''''''
fig = go.Figure(data=[
    go.Bar(name='Average Math Scores', x=scores_parental.index, y=scores_parental['math score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Reading Scores', x=scores_parental.index, y=scores_parental['reading score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Writing Scores', x=scores_parental.index, y=scores_parental['writing score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside')
])

fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})

fig.update_yaxes(title_text="Average Scores", title_font={"size": 14})
fig.update_xaxes(title_text="Parental Level of Education", title_font={"size": 14})

fig.update_layout(title_text='Average Exam Scores for each Parental Level of Education',
                  title_x=0.5, title_font=dict(size=20))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Average Exam Scores vs. Lunch
'''''''''
fig = go.Figure(data=[
    go.Bar(name='Average Math Scores', x=scores_lunch.index, y=scores_lunch['math score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Reading Scores', x=scores_lunch.index, y=scores_lunch['reading score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Writing Scores', x=scores_lunch.index, y=scores_lunch['writing score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside')
])

fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})

fig.update_yaxes(title_text="Average Scores", title_font={"size": 14})
fig.update_xaxes(title_text="Lunch", title_font={"size": 14})

fig.update_layout(title_text='Average Exam Scores for Lunch',
                  title_x=0.5, title_font=dict(size=20))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Average Exam Scores vs. Test Preparation Options
'''''''''
fig = go.Figure(data=[
    go.Bar(name='Average Math Scores', x=scores_preparation.index, y=scores_preparation['math score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Reading Scores', x=scores_preparation.index, y=scores_preparation['reading score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside'),

    go.Bar(name='Average Writing Scores', x=scores_preparation.index, y=scores_preparation['writing score'],
           marker=dict(line=dict(width=5)),
           texttemplate='%{y:20,.2f}', textposition='outside')
])

fig.update_layout(barmode='group', xaxis={'categoryorder': 'total descending'})

fig.update_yaxes(title_text="Average Scores", title_font={"size": 14})
fig.update_xaxes(title_text="Test Preparation Course", title_font={"size": 14})

fig.update_layout(title_text='Average Exam Scores for each Test Preparation Options',
                  title_x=0.5, title_font=dict(size=20))
fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
fig.show()
'''''''''

# Relationship between Math and Reading Scores
'''''''''
fig = px.scatter(data, x="math score", y="reading score", trendline="ols",
                 labels={"math score": "Math Score",
                         "reading score": "Reading Score"})
fig.update_layout(title_text='Relationship between Math and Reading Scores',
                  title_x=0.5, title_font=dict(size=20))
fig.data[1].line.color = 'red'
fig.show()
'''''''''

# Relationship between Math and Writing Scores
'''''''''
fig = px.scatter(data, x="math score", y="writing score", trendline="ols",
                 labels={"math score": "Math Score",
                         "writing score": "Writing Score"})
fig.update_layout(title_text='Relationship between Math and Writing Scores',
                  title_x=0.5, title_font=dict(size=20))
fig.data[1].line.color = 'red'
fig.show()
'''''''''

# Relationship between Reading and Writing Scores
'''''''''
fig = px.scatter(data, x="reading score", y="writing score", trendline="ols",
                 labels={"reading score": "Reading Score",
                         "writing score": "Writing Score"})
fig.update_layout(title_text='Relationship between Reading and Writing Scores',
                  title_x=0.5, title_font=dict(size=20))
fig.data[1].line.color = 'red'
fig.show()
'''''''''

# Distribution of the All Scores
'''''''''
fig = go.Figure(data=[go.Scatter3d(
    x=data['math score'],
    y=data['reading score'],
    z=data['writing score'],
    mode='markers+text',
    marker=dict(
        size=5,
        opacity=0.8
    ),
    hovertemplate=
    "Math Score: %{x:}<br>" +
    "Reading Score: %{y:}<br>" +
    "Writing Score: %{z:}"
)])
fig.update_layout(scene=dict(
    xaxis_title='Math Score',
    yaxis_title='Reading Score',
    zaxis_title='Writing Score')
)
fig.update_layout(title_text='Distribution of the All Scores',
                  title_x=0.5, title_font=dict(size=22))

fig.show()
'''''''''

# Distribution of Math Scores by Gender
'''''''''
fig = px.histogram(data, x="math score", color='gender', opacity=0.7)
fig.update_layout(barmode='overlay', xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
fig.update_layout(title_text='Distribution of Math Scores by Gender',
                  title_x=0.5, title_font=dict(size=20))  # Location and the font size of the main title
fig.show()
'''''''''

# Distribution of Reading Scores by Gender
'''''''''
fig = px.histogram(data, x="reading score", color='gender', opacity=0.7)
fig.update_layout(barmode='overlay', xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
fig.update_layout(title_text='Distribution of Reading Scores by Gender',
                  title_x=0.5, title_font=dict(size=20))
fig.show()
'''''''''

# Distribution of Writing Scores by Gender
'''''''''
fig = px.histogram(data, x="writing score", color='gender', opacity=0.7)
fig.update_layout(barmode='overlay', xaxis={'categoryorder': 'total descending'})
fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
fig.update_layout(title_text='Distribution of Writing Scores by Gender',
                  title_x=0.5, title_font=dict(size=20))
fig.show()
'''''''''

# Outliers of the Scores
'''''''''
fig = px.box(data, y=['math score', 'reading score', 'writing score'])
fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
fig.update_layout(title_text='Outliers of the Scores',
                  title_x=0.5, title_font=dict(size=20))
fig.show()
'''''''''
