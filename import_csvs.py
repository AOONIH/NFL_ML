import os, pickle
import pandas as pd

# Establish working directory and dir for nfl csvs
home_dir = os.getcwd()  # Can changed if data not in python directory
datadir = 'nfl_results_csvs'

game_results_dir = os.path.join(home_dir,datadir)
game_results_contents = os.listdir(game_results_dir)

# Import csv files

# to_import = {'2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
#               '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'}

all_seasons_dict = {}
for season_csv in game_results_contents:
    if '.csv' in season_csv:
        # print(season_csv)
        season_str = season_csv.replace('nfl ','')
        season_str = season_str.replace('.csv','')
        # print(season_str)
        season_df = pd.read_csv(os.path.join(game_results_dir,season_csv))
        curr_season_dict = {int(season_str):season_df}
        all_seasons_dict.update(curr_season_dict)

# # sort keys for all seasons
# seasons = list(all_seasons_dict.keys())
# seasons.sort()

# or specify seasons
seasons = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
           2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

all_seasons_df = all_seasons_dict[seasons[0]][
    ['season','week','home_team','home_score','visitors_score','visiting_team']]

for season in seasons[1:]:
    all_seasons_df = all_seasons_df.append(all_seasons_dict[season][
        ['season','week','home_team','home_score','visitors_score','visiting_team']])

print(all_seasons_df.shape)
all_seasons_df['week'] = all_seasons_df['week'].astype(int)
reg_season_df = all_seasons_df[all_seasons_df['week'] <= 17]

reg_season_df.to_csv('reg_season_2002-2017')