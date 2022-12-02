from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    resume = str(input("Press 'p' to pause"))
    if resume == "p":
      source.paused = True
    else:
      continue
while True:
   
  os.system("clear")
  
  print("🎵 Ritwik's Music Player 🎵")
  time.sleep(1)
  
  choice = int(input("Do you want to play some music?\n Press 1 to Play \n Press 2 to exit "))
  time.sleep(1)
  
  if choice ==1:
    print("Playing the music now")
    play()
  elif choice==2:
    break
  else:
    continue

print("Exiting the music player")
time.sleep(1)