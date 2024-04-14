from tkinter import *
import time
import msvcrt
import sys

paragraph = "The golden sun dipped below the horizon, casting a warm glow over the tranquil meadow. The gentle breeze rustled the leaves of the towering oak trees, creating a symphony of whispers. Birds chirped merrily, their melodious songs echoing through the air. As I walked along the winding path, my feet sinking softly into the lush green grass, I marveled at the beauty of nature surrounding me. The delicate scent of wildflowers wafted through the air, filling my senses with a sweet fragrance. I closed my eyes and let the serenity of the moment wash over me, grateful for this peaceful haven amidst the chaos of the world"
print(paragraph)
def countdown_timer(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Go!")

countdown_timer(3)
text= ""
start_time = time.time()
while True:
    if msvcrt.kbhit():
        key = msvcrt.getwch()
        if key == '\r': 
            break
        sys.stdout.write(key)
        sys.stdout.flush()
        text += key
    current_time = time.time()
    if current_time - start_time > 60: 
        break
print(text)
text = text.split(" ")
paragraph = paragraph.split(" ")
count = 0
for i in range(len(text)):
    if text[i]==paragraph[i]:
        count+=1
print("Total Words Entered:",len(text),"\nCorrect words entered (WPM):", count,"\nAccuracy:", count/len(text))

# expanding this to perform test in a window
'''
window = Tk()
window.title("Typing Test")
window.geometry("800x500")

window.mainloop()
'''



















