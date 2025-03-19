#imports modules needed for the charts
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("top50_spotify_songs_IE.csv")#opens the csv file into a dataframe

df['snapshot_date'] = pd.to_datetime(df['snapshot_date'], dayfirst = True)#converts the date in the dataset 

df['month'] = df['snapshot_date'].dt.month

monthly_dfs = {month: group for month, group in df.groupby('month')}#categorises a chosen dataset by months


#this divides the months into separate dataframes
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

#creates an array of songs and an empty statistics list
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


#*****************
#January pie chart
#*****************

#this counts the amount of times a certain song appeared in the given month
for x in df1.index:
    if df1.loc[x, "name"] in janSongs:
        count = (df1["name"] == df1.loc[x, "name"]).sum()
        janStats.append([df.loc[x, "name"], int(count)])
        janSongs = janSongs[janSongs != df1.loc[x, "name"]]

#this sorts the list obtained from ^^^ by the number of times it appeared in a given month in a descending order
janStats.sort(key=lambda x: x[1], reverse=True)

#this adds the total daily rank of a song in a given month
for sublist in janStats:
    song = sublist[0]
    song_sum = df1[df1['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)

#limits the list from ^^^ to 10 elements(for top 10) and sorts it in ascending order
janStats = janStats[:10]
 
janStats.sort(key=lambda x: x[1])

#creates a lists of song names, their daily ranks and reverses the order of the ranks(to show song popularity in a descending order)
song_names = [item[0] for item in janStats]
daily_ranks = [item[1] for item in janStats]
daily_ranks.reverse()

#creates a pie chart of equal proportions in a clockwise direcion with a black border, with a legend attached; shows the chart
plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of January in Ireland")

plt.show()

#later code works in the same way

#*****************
#February pie chart
#*****************


for x in df2.index:
    if df2.loc[x, "name"] in febSongs:
        count = (df2["name"] == df2.loc[x, "name"]).sum()
        febStats.append([df.loc[x, "name"], int(count)])
        febSongs = febSongs[febSongs != df2.loc[x, "name"]]

febStats.sort(key=lambda x: x[1], reverse=True)

for sublist in febStats:
    song = sublist[0]
    song_sum = df2[df2['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)

febStats = febStats[:10]

febStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in febStats]
daily_ranks = [item[1] for item in febStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of February in Ireland")

plt.show()


#*****************
#March pie chart
#*****************


for x in df3.index:
    if df3.loc[x, "name"] in marSongs:
        count = (df3["name"] == df3.loc[x, "name"]).sum()
        marStats.append([df.loc[x, "name"], int(count)])
        marSongs = marSongs[marSongs != df3.loc[x, "name"]]

marStats.sort(key=lambda x: x[1], reverse=True)



for sublist in marStats:
    song = sublist[0]
    song_sum = df3[df3['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
marStats = marStats[:10]

marStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in marStats]
daily_ranks = [item[1] for item in marStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of March in Ireland")

plt.show()


#*****************
#April pie chart
#*****************


for x in df4.index:
    if df4.loc[x, "name"] in aprSongs:
        count = (df4["name"] == df4.loc[x, "name"]).sum()
        aprStats.append([df.loc[x, "name"], int(count)])
        aprSongs = aprSongs[aprSongs != df4.loc[x, "name"]]

aprStats.sort(key=lambda x: x[1], reverse=True)

for sublist in aprStats:
    song = sublist[0]
    song_sum = df4[df4['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
aprStats = aprStats[:10]

aprStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in aprStats]
daily_ranks = [item[1] for item in aprStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of April in Ireland")

plt.show()

#*****************
#May pie chart
#*****************

for x in df5.index:
    if df5.loc[x, "name"] in maySongs:
        count = (df5["name"] == df5.loc[x, "name"]).sum()
        mayStats.append([df.loc[x, "name"], int(count)])
        maySongs = maySongs[maySongs != df5.loc[x, "name"]]

mayStats.sort(key=lambda x: x[1], reverse=True)

for sublist in mayStats:
    song = sublist[0]
    song_sum = df5[df5['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
mayStats = mayStats[:10]

mayStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in mayStats]
daily_ranks = [item[1] for item in mayStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of May in Ireland")

plt.show()

#*****************
#June pie chart
#*****************


for x in df6.index:
    if df6.loc[x, "name"] in junSongs:
        count = (df6["name"] == df6.loc[x, "name"]).sum()
        junStats.append([df.loc[x, "name"], int(count)])
        junSongs = junSongs[junSongs != df6.loc[x, "name"]]

junStats.sort(key=lambda x: x[1], reverse=True)

for sublist in junStats:
    song = sublist[0]
    song_sum = df6[df6['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
junStats = junStats[:10]

junStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in junStats]
daily_ranks = [item[1] for item in junStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of June in Ireland")

plt.show()


#*****************
#July pie chart
#*****************

for x in df7.index:
    if df7.loc[x, "name"] in julSongs:
        count = (df7["name"] == df7.loc[x, "name"]).sum()
        julStats.append([df.loc[x, "name"], int(count)])
        julSongs = julSongs[julSongs != df7.loc[x, "name"]]

julStats.sort(key=lambda x: x[1], reverse=True)

for sublist in julStats:
    song = sublist[0]
    song_sum = df7[df7['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
julStats = julStats[:10]

julStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in julStats]
daily_ranks = [item[1] for item in julStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of July in Ireland")

plt.show()


#*****************
#August pie chart
#*****************


for x in df8.index:
    if df8.loc[x, "name"] in augSongs:
        count = (df8["name"] == df8.loc[x, "name"]).sum()
        augStats.append([df.loc[x, "name"], int(count)])
        augSongs = augSongs[augSongs != df8.loc[x, "name"]]

augStats.sort(key=lambda x: x[1], reverse=True)

for sublist in augStats:
    song = sublist[0]
    song_sum = df8[df8['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
augStats = augStats[:10]

augStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in augStats]
daily_ranks = [item[1] for item in augStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of August in Ireland")

plt.show()


#*****************
#September pie chart
#*****************


for x in df9.index:
    if df9.loc[x, "name"] in sepSongs:
        count = (df9["name"] == df9.loc[x, "name"]).sum()
        sepStats.append([df.loc[x, "name"], int(count)])
        sepSongs = sepSongs[sepSongs != df9.loc[x, "name"]]

sepStats.sort(key=lambda x: x[1], reverse=True)

for sublist in sepStats:
    song = sublist[0]
    song_sum = df9[df9['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
sepStats = sepStats[:10]

sepStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in sepStats]
daily_ranks = [item[1] for item in sepStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of September in Ireland")

plt.show()


#*****************
#October pie chart
#*****************


for x in df10.index:
    if df10.loc[x, "name"] in octSongs:
        count = (df10["name"] == df10.loc[x, "name"]).sum()
        octStats.append([df.loc[x, "name"], int(count)])
        octSongs = octSongs[octSongs != df10.loc[x, "name"]]

octStats.sort(key=lambda x: x[1], reverse=True)

for sublist in octStats:
    song = sublist[0]
    song_sum = df10[df10['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
octStats = octStats[:10]

octStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in octStats]
daily_ranks = [item[1] for item in octStats]
daily_ranks.reverse()


plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of October in Ireland")

plt.show()


#*****************
#November pie chart
#*****************


for x in df11.index:
    if df11.loc[x, "name"] in novSongs:
        count = (df11["name"] == df11.loc[x, "name"]).sum()
        novStats.append([df.loc[x, "name"], int(count)])
        novSongs = novSongs[novSongs != df11.loc[x, "name"]]

novStats.sort(key=lambda x: x[1], reverse=True)

for sublist in novStats:
    song = sublist[0]
    song_sum = df11[df11['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
novStats = novStats[:10]

novStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in novStats]
daily_ranks = [item[1] for item in novStats]
daily_ranks.reverse()


plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of November in Ireland")

plt.show()


#*****************
#December pie chart
#*****************


for x in df12.index:
    if df12.loc[x, "name"] in decSongs:
        count = (df12["name"] == df12.loc[x, "name"]).sum()
        decStats.append([df.loc[x, "name"], int(count)])
        decSongs = decSongs[decSongs != df12.loc[x, "name"]]

decStats.sort(key=lambda x: x[1], reverse=True)

for sublist in decStats:
    song = sublist[0]
    song_sum = df12[df12['name'] == song]['daily_rank'].sum()
    sublist[1] = int(song_sum)
    
decStats = decStats[:10]

decStats.sort(key=lambda x: x[1])

song_names = [item[0] for item in decStats]
daily_ranks = [item[1] for item in decStats]
daily_ranks.reverse()

plt.figure(figsize=(10, 10))
plt.pie(daily_ranks, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

plt.legend(song_names, title="Songs", loc="lower left", bbox_to_anchor=(-0.18, -0.15))

plt.axis('equal')

plt.title("Top 10 Popular Spotify Songs of December in Ireland")

plt.show()