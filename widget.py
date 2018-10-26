import ui
import time
import clipboard
import sys

key = "test"


def encrypt(Text, Key):
    text = Text.lower()
    key = Key.lower
    lent = len(text)
    lenk = len(key)
    h = ""
    
    if lent > lenk:
			tk=lent-lenk
			for x in range(0, (tk)):
				key = key + key[x]
			
			for y in range(0, lent):
				to1_26text = ord(word[y])-97
					to1_26key = ord(key[y])-97
					s = to1_26text + to1_26key
					ms = s%26
					c=chr(ms+97)
					h = h + c
		
    
    
def encrypt_button_tapped(sender):
    clipboard.set(encrypt(clipboard.get(), key)
    sender.title = "encrypted!"
    
