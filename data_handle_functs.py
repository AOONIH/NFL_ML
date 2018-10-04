import pandas as pd
import numpy as np


def subset_seasons(csv_path, col_var):
    """Function to subset datagrame from csv based on values
        in seasons column. csv_path = str,
        col_var = [str for col name and list/tuple/arr for seasons"""

    df = pd.read_csv(csv_path)   # read in table
    # subset_df = df[df['season'] == seasons]
    sub_ix = df[col_var[0]].isin(col_var[1])
    subset_df = df[sub_ix]
    return subset_df


def subset_team_result(df, season, team_name):
    """ Generates reg season df for 1 team for 1 season
        df = reg season df.
        season = int
        team_name = Capitalised nickname e.g 'Eagles'"""

    sub_season = df[df['season'] == season]  # select season
    # select rows where team played either home or away
    team_ix = (sub_season['home_team'] == team_name) | (sub_season['visiting_team'] == team_name)
    team_result = sub_season[team_ix]   # index using bool

    return team_result


def calc_score(df,team_name):
    reg_season_scores = []
    for index, r in df.iterrows():
        if r['home_team'] == team_name:
            win_margin = r['home_score']-r['visitors_score']
        elif r['visiting_team'] == team_name:
            win_margin = r['visitors_score'] - r['home_score']
        reg_season_scores.append(win_margin)

    return np.array(reg_season_scores)


def gen_1hot_arr(score_arr):
    win_arr = []
    for score in score_arr:
        if score > 0:
            win_arr.append(1)
        elif score <= 0:
            win_arr.append(0)
    return np.array(win_arr)


def season_perf(df,season,team_name):
    """ Returns win-loss array and points margin array"""

    season_df = subset_team_result(df,season,team_name)
    points_margin_arr = calc_score(season_df, team_name)
    win_loss_1hot = gen_1hot_arr(points_margin_arr)

    return win_loss_1hot, [points_margin_arr]


# eg_df = subset_seasons('reg_season_2002-2017.csv',('season',{2014,2015,2016}))
# win_margin = season_perf(eg_df, 2014, 'Eagles')[0]
# win_1hot = season_perf(eg_df, 2014, 'Eagles')[1]

