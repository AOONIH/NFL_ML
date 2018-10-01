import pandas as pd
import numpy as np
import os

csv_list = ['nfl 2015.csv', 'nfl 2016.csv', 'nfl 2017.csv']
year = ['2015', '2016', '2017']
counter = 0

for csv in csv_list:
    df = pd.read_csv(csv)
    # Determine away team
    winner_home_bool = df['AT'].isnull().values

    home_team_col = []
    home_score_col = []
    away_team_col = []
    away_score_col = []
    season_col = [year[counter]]*len(df)

    # Create series in home team, away team format
    for row in zip(df['Winner/tie'],df['PtsW'],df['Loser/tie'],df['PtsL'], winner_home_bool):
        if row[-1] == False:
            home_team_col.append(row[2])
            home_score_col.append(row[3])

            away_team_col.append(row[0])
            away_score_col.append(row[1])

        else:
            home_team_col.append(row[0])
            home_score_col.append(row[1])

            away_team_col.append(row[2])
            away_score_col.append(row[3])

    # format team names
    home_team_col2 = []
    away_team_col2 = []

    for row in home_team_col:
        name = row.split()[-1]
        home_team_col2.append(name)

    for row in away_team_col:
        name = row.split()[-1]
        away_team_col2.append(name)

    # Form final dataframe

    week_col = df['Week']
    # home_team_col = df[]

    df_dict = {'season': season_col,'week': week_col,'home_team': home_team_col2,'home_score':home_score_col,
               'visitors_score': away_score_col, 'visiting_team': away_team_col2}
    formatted_df = pd.DataFrame.from_dict(data=df_dict)
    formatted_df = formatted_df[['season','week','home_team','home_score',
                                'visitors_score','visiting_team']]

    formatted_df.to_csv(os.path.join('nfl_results_csvs',csv)) # save to new folder
    counter += 1

