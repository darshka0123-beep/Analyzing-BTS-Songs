import pandas as pd
import matplotlib.pyplot as plt

pd.set_option( 'display.max_columns', None)
pd.set_option('max_colwidth', None)

# Bts music info data set csv
songData = pd.read_csv('bts.csv')
favSong = "Spring Day"
print("My favorite BTS song is " + favSong + ".")

# print(songData.head())
# print(songData["eng_track_title"])

# Filter Data
print("\nThe data for my favorite song is:\n")

# Create a new variable to store your favorite album data
favSongbooleanlist = songData["eng_track_title"] == favSong
#print(fav_album_boolean_list)

favSongdata = songData.loc[favSongbooleanlist]
print(favSongdata)

print("\n\n")

album_title = favSongdata["eng_album_title"].iloc[0]
albumbooleanlist = songData["eng_album_title"] == album_title
albumsongdata = songData.loc[albumbooleanlist]
numofsongs = len(albumsongdata)

print("We will be comparing " + favSong + " to other songs in the album " + album_title)
print("There are " + str(numofsongs) + " songs in the album " + album_title)

print("...............................................................................................................")
print("\n\n")
input("Press enter to see more information about how " + favSong + " compares to other songs in " + album_title + "\n")
print("\n\n")

# Shortest Song Duration
minduration = albumsongdata["spotify_track_duration_ms"].min()
print("The shortest song duration (ms) in this album is: " + str(minduration))
min_difference = 274097 - minduration
print(favSong + " is " + str(min_difference) +" longer than the shortest song in this album.")
print("\n")

# Longest Song Duration
maxduration = albumsongdata["spotify_track_duration_ms"].max()
print("The longest song duration (ms) in this album is: " + str(maxduration))
max_difference = maxduration - 274097
print(favSong + " is " + str(max_difference) + " shorter than the longest song in this album.")
print("\n")

# find median
median = albumsongdata["spotify_track_duration_ms"].median()
print("The median song duration of the data set is: " +str(median))
print(favSong + " is longer than the median.")
print("\n")

# find mean
mean = albumsongdata["spotify_track_duration_ms"].mean()
print("The mean song duration of the data set is: " +str(mean))
print(favSong + " is longer than the mean")
print("\n")

print("............................................................................................................")
input("Press enter to see data visualizations. \n")

# Create graphs
#Convert duration from milliseconds to minutes
duration_in_minutes = songData["spotify_track_duration_ms"] / 60000

# Create histogram
plt.hist(duration_in_minutes,bins=20)

# Labels
plt.grid(True)
plt.title("Track Duration of All BTS Songs Histogram")
plt.xlabel("Track Duration (Minutes)")
plt.ylabel("Number of Songs")

# Prints Interpretation of histogram
print(
    "According to the histogram, most fall under the duration between 3 to 5 minutes. The shape of the histogram is a bell curve showing it is likely normally distributed."
)
print()

# Show Histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

# Convert string values to float/int
songData["spotify_track_duration_ms"] = pd.to_numeric(songData["spotify_track_duration_ms"], errors="coerce")

# Convert duration from ms to minutes for cleaner numbers
duration_min = songData["spotify_track_duration_ms"]/60000

# make the window wider and taller to give the labels space
plt.figure(figsize=(10,8))

# Create Scatterplot
plt.scatter(duration_min, songData["eng_album_title"], alpha=0.7, color='purple')

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Track Duration vs Album")
plt.xlabel("Track Duration (Minutes)" "\n")
plt.ylabel("Album Name")

plt.tick_params(axis='y', labelsize=8)
plt.tight_layout()

# Prints Interpretation of scatterplot
print("According to the scatter plot, we can conclude there is no obvious correlation between track duration and album.")
print()

plt.show()
print("\nThank you for reading through my data analysis!")