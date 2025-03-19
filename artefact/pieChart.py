import pandas as pd

df = pd.read_csv("top50_spotify_songs_IE.csv")

#dates = df["snapshot_date"].unique()

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#songs = df["name"].unique()

song_popularity = df.groupby("name")["daily_rank"].sum()

df['snapshot_date'] = pd.to_datetime(df['snapshot_date'], dayfirst = True)

df['month'] = df['snapshot_date'].dt.month

monthly_dfs = {month: group for month, group in df.groupby('month')}

df1 = monthly_dfs[1]
df2 = monthly_dfs[2]
df3 = monthly_dfs[3]
df4 = monthly_dfs[4]
df5 = monthly_dfs[5]
df6 = monthly_dfs[6]
df7 = monthly_dfs[7]
df8 = monthly_dfs[8]
df9 = monthly_dfs[9]
df10 = monthly_dfs[10]
df11 = monthly_dfs[11]
df12 = monthly_dfs[12]

janSongs = df1["name"].unique()

for x in df1.index:
    if df1.loc[x, "name"] in janSongs:
        count = (df1["name"] == df1.loc[x, "name"]).sum()
        print(f"""{df.loc[x, "name"]} - {count}""")
        janSongs.drop(df1.loc[x, "name"], axis=0)

#for song, total in song_popularity.items():
#    print(f"{song} - {total}")

#for i in range(len(dates)-1):
#    month = (pd.Timestamp(dates[i])).month
#    if month in months:
#        continue
#    else:
#        months.append(month)

#print(months)

#print(dates)

#print(len(songs))
#print(songs)



#rate = []

#for i in df.index:
#   if df["name"] in rate:


        
