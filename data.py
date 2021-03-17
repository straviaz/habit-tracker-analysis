import pandas as pd
import numpy as np 
import csv 
import matplotlib.pyplot as plt
from IPython.display import display, HTML, display_html

def convert_csv_to_df(path):
    df = pd.read_csv(path, header=0)
    return df

def get_habit_df():
    df = convert_csv_to_df('Datasets/data.csv')
    return df

def convert_activity_csv_to_dict(path):
    csv_file = open(path, "r")
    dict_reader = csv.DictReader(csv_file)
    ordered_dict_from_csv = list(dict_reader)[0]
    dict_from_csv = dict(ordered_dict_from_csv)
    for key in dict_from_csv:
        dict_from_csv[key] = float(dict_from_csv[key])
        
    return dict_from_csv

def convert_csv_to_dict(path):
    csv_file = open(path, "r")
    dict_reader = csv.DictReader(csv_file)
    ordered_dict_from_csv = list(dict_reader)[0]
    dict_from_csv = dict(ordered_dict_from_csv)

    return dict_from_csv

def display_side_by_side(*args):
    html_str=''
    for df in args:
        html_str+=df.to_html(index=False)
    display_html(html_str.replace('table', 'table style="display:inline"'), raw=True)

def init():
    activities_df = get_habit_df()
    activity_dict = convert_activity_csv_to_dict('Datasets/activity-code.csv')
    mood_dict = convert_csv_to_dict('Datasets/mood-code.csv')   

    return activities_df, activity_dict, mood_dict   

init()