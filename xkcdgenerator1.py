import requests
import io
import sys
import os
import base64
import tkinter as tk
from urllib.request import urlopen
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import webbrowser
 


	
def run():
	url="https://c.xkcd.com/random/comic/"

	response=requests.get(url)
	linkk=response.url
	html=response.content
	soup= BeautifulSoup(html,'html.parser')
	comicbox=soup.find('div',attrs={'id':'comic'})
	comicpic=[]
	comicpic=str(comicbox)
    
	start_link = comicpic.find("src")
	start_quote = comicpic.find('"', start_link)
	end_quote = comicpic.find('"', start_quote + 1)
	comiclink = comicpic[start_quote + 1: end_quote]

	start_linkq = comicpic.find("title")
	start_quoteq = comicpic.find('"', start_linkq)
	end_quoteq = comicpic.find('"', start_quoteq + 1)
	comictitle= comicpic[start_quoteq + 1: end_quoteq]

	image_url = "https:"+comiclink	

	root = tk.Tk()
	root.title("RANDOM XKCD GENERATOR")

	w = 1300
	h = 600

	root.geometry("1300x600")

	image_byt = urlopen(image_url).read()
	image_b64 = base64.encodestring(image_byt)
	photo = tk.PhotoImage(data=image_b64)

	cv = tk.Canvas(bg='lightblue')

	cv.pack(side='top', fill='both', expand='yes')

	cv.create_image(650,300,image=photo, anchor='center')

	if(len(comictitle)>115):
		comictitle=comictitle[:115] + '\n' + comictitle[115:]


	titlelable=tk.Label(cv,text=comictitle,font="Consolas 14 bold")
	titlelable.pack()

	newwindowbutton=tk.Button(cv,text="New comic!",fg="orange",font="Consolas 23",command=restart)
	newwindowbutton.place(x=1000,y=500)

	

	codebutton=tk.Button(cv,text=comiclink,font="Consolas 15 bold").place(x=450,y=500)

	exitbutton=tk.Button(cv,text="Exit",fg="red",font="Consolas 23",command=quit)
	exitbutton.place(x=150,y=500)

	root.mainloop()
	

def restart():
	os.execv(sys.executable, ['python'] + sys.argv)

def openlink(link):
    webbrowser.open(link)
run()
