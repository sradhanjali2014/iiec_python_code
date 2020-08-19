import pyttsx3
import os
pyttsx3.speak("welcome to my tools")

print()
print('press1:to open chrome browser')
print('press2:to open notepad')
print('press3:to open media player')
print('press4:to open write')
print('press5:to open explorer')
print('press6:to open Internet Explorer')
print('press7:to open Sublime Text3')
print('press8:to open VLC')

print()

print("enter ur choice:",end='')
p=input()
print(p)

if int(p)==1:
	os.system("chrome")

if int(p)==2:
	os.system("notepad")

if int(p)==3:
	os.system("wmplayer")

if int(p)==4:
	os.system("write")

if int(p)==5:
	os.system("explorer")

if int(p)==6:
	os.system("iexplore")

if int(p)==7:
	os.system("sublime_text")

if int(p)==8:
	os.system("vlc")


else:
	print("don't support")