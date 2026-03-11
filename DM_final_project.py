import pandas as pd
import sqlite3
import os

file_path = r"C:\Users\ajaoo\Downloads\def_players_stats.csv"

if os.path.exists(file_path):
    df_off_player_stats = pd.read_csv(file_path)
    print("File loaded successfully!")
else:
    print("Make sure the file is in your GitHub folder!")
