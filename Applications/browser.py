from os import name
import time
print ("welcome to the EagleOS Browser" + name)
time.sleep (1)
print("what do you want to search?")
search = input("search: ")
print("good choice" + name)
print ("searching...")
time.sleep (1)
print("Loading...")
if search == "YouTube":
  print("https://www.youtube.com/")
elif search == "Google":
  print("https://www.google.com/")
elif search == "Spotify":
  print("https://open.spotify.com/")
elif search == "Discord":
  print("https://discord.com/channels/@me")
elif search == "BBC":
  print("https://www.bbc.com/")
else:
  print("sorry, we couldn't find that")