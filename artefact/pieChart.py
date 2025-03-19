import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("top50_spotify_songs_IE.csv")

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

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
janStats = []

febSongs = df2["name"].unique()
febStats = []

marSongs = df3["name"].unique()
marStats = []

aprSongs = df4["name"].unique()
aprStats = []

maySongs = df5["name"].unique()
mayStats = []

junSongs = df6["name"].unique()
junStats = []

julSongs = df7["name"].unique()
julStats = []

augSongs = df8["name"].unique()
augStats = []

sepSongs = df9["name"].unique()
sepStats = []

octSongs = df10["name"].unique()
octStats = []

novSongs = df11["name"].unique()
novStats = []

decSongs = df12["name"].unique()
decStats = []

#

for x in df1.index:
    if df1.loc[x, "name"] in janSongs:
        count = (df1["name"] == df1.loc[x, "name"]).sum()
        janStats.append([df.loc[x, "name"], int(count)])
        janSongs = janSongs[janSongs != df1.loc[x, "name"]]

janStats.sort(key=lambda x: x[1], reverse=True)

for i in range(len(janStats)-1,-1,-1):
    if janStats[i][1] < janStats[0][1]:
        janStats.pop(i)

for sublist in janStats:
    song = sublist[0]
    song_sum = df1[df1['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
janStats.sort(key=lambda x: x[1])

janStats = janStats[:10]

song_names = [item[0] for item in janStats]
daily_ranks = [item[1] for item in janStats]
print(daily_ranks)
daily_ranks.reverse()
print(daily_ranks)

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("10 Popular Songs of January in Ireland")

plt.show()