# If you are asking "what is this?",
# you should know that you are not
# doing anything dangerous
# you are just installing the
# LinuxStore for Python (๑˃̵ᴗ˂̵)و

# The dependencies (most of these are preinstalled - only BeautifulSoup4 and requests are not):
from json.decoder import JSONDecodeError
from tkinter import *
import tkinter.ttk as ttk
import subprocess
import sys
import urllib.request
import urllib.error
import getpass
import platform
import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import urllib
import base64



print("""
   __   _                 ______              
  / /  (_)__  __ ____ __ / __/ /____  _______ 
 / /__/ / _ \/ // /\ \ /_\ \/ __/ _ \/ __/ -_)
/____/_/_//_/\_,_//_\_\/___/\__/\___/_/  \__/ 




▄▀ █▀▀ ▀▄   ▄▀█ █▀█ ░░█ █░█ █▄░█
▀▄ █▄▄ ▄▀   █▀█ █▀▄ █▄█ █▄█ █░▀█

""")
result = ""
clicked = []

root = Tk()
root.geometry('600x400')
root.title("LinuxStore")
root['cursor'] = 'arrow'
style = ttk.Style()
style.configure("Courier.TButton", font=("Courier", 12))


# the app script
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

def install_pip():
    root["cursor"] = 'watch'
    root.update_idletasks()
    install(app.get())
    root["cursor"] = 'arrow'
    root.update_idletasks()
    Label(frame1, text="Installed app via pip").pack()

def install_npm():
    root["cursor"] = 'watch'
    root.update_idletasks()
    subprocess.check_call(["npm", "install", "-g", app.get()])
    root["cursor"] = 'arrow'
    root.update_idletasks()
    Label(frame1, text="Installed app via npm").pack()

def check():
    root["cursor"] = 'watch'
    root.update_idletasks()
    # find on PyPi
    try:
        with urllib.request.urlopen('https://pypi.org/simple/' + app.get() + "/") as f:
            result = f.read(13)
    except urllib.error.HTTPError as e:
        result = "404 Not Found"
    except urllib.error.URLError as e:
        print("Something went wrong")
    if result != "404 Not Found":
        Button(frame1, text = "Install " + app.get() +" on PyPi", command = install_pip, cursor='hand2').pack()
        
    # search on npm
    try:
        with urllib.request.urlopen('https://www.npmjs.com/package/' + app.get()) as f:
            result = f.read(13)
    except urllib.error.HTTPError as e:
        result = "404 Not Found"
    except urllib.error.URLError as e:
        print("Something went wrong")
    if result != "404 Not Found":
        Button(frame1, text = "Install " + app.get() + " on npm", command = install_npm, cursor='hand2').pack()
    root["cursor"] = 'arrow'
    root.update_idletasks()
    
def func(item):
    print(item)
    root["cursor"] = 'watch'
    root.update_idletasks()
    subprocess.check_call(["git", "clone", 'https://github.com/' + item + '.git'])
    root["cursor"] = 'arrow'
    Label(github, text="Check your current working directory folder for the project").pack()
    root.update_idletasks()
    

def github_search():
    global thing
    root["cursor"] = 'watch'
    root.update_idletasks()
    try:
        req = urllib.request.Request('https://api.github.com/search/repositories?q=' + github_repo.get())
        response = urllib.request.urlopen(req)
        result = response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        result = e.read().decode("utf-8")
    result = json.loads(result)
    for thing in result["items"]:
        Button(gitres, text = thing["full_name"], command=lambda s=thing["full_name"]: func(s), cursor='hand2').pack()
    root["cursor"] = 'arrow'
    root.update_idletasks()
    


notebook = ttk.Notebook(root,height=1000,width=1000)
notebook.pack(pady=10, expand=True)
notebook.pressed_index = None
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
github = ttk.Frame(notebook, width=400, height=280)
frame3 = ttk.Frame(notebook, width=400, height=280)

# package search
#https://user-images.githubusercontent.com/68869672/193342967-c6e936e8-a39d-4853-b584-9db4ab13758a.gif
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
github.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)


Label(frame1, text = "Search for an package:").pack()
app = Entry(frame1)
app.pack()
Button(frame1, text='Check for packages', command = check, cursor='hand2').pack()


# system info
Label(frame2, text="System Information:").pack()
Label(frame2, text="Welcome back, " + getpass.getuser()).pack()
Label(frame2, text="You're running LinuxStore on python " +  platform.python_version()).pack()
Label(frame2, text="Accessed on " + datetime.now().strftime('%m/%d/%Y %H:%M')).pack()
Label(frame2, text="").pack()
Label(frame2, text="Overflowed with results? Try doing a more specific term").pack()

logo = ttk.Label(frame2, text="""
   __   _                 ______              
  / /  (_)__  __ ____ __ / __/ /____  _______ 
 / /__/ / _ \/ // /\ \ /_\ \/ __/ _ \/ __/ -_)
/____/_/_//_/\_,_//_\_\/___/\__/\___/_/  \__/ 
""")
logo.pack()
logo.configure(style="Courier.TButton")


# github search

Label(github, text="Find GitHub repo and download it via git").pack()
github_repo = Entry(github)
github_repo.pack()
Button(github, text="Find a github repo", command=github_search, cursor='hand2').pack()
gitres = Frame(frame3)
gitres.pack(side=TOP, fill="x")


# app search

def searchapps(app):
    links = []
    URL = "https://snapcraft.io/search?q=" + app
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("a", class_="p-media-object--snap", href=True)
    testy = soup.find_all("h4", class_="p-media-object__title")
    testyy = soup.find_all("p", class_="u-overflow-visible")
    for x in results:
        link = {"link": "https://snapcraft.io" + x["href"]}
        link["name"] = ' '.join(testy[results.index(x)].text.split())
        link["by"] = ' '.join(testyy[results.index(x)].text.replace("Publisher:", "").replace("Verified account", "").replace("Star developer", "").split())
        links.append(link)
    return links

def download(item):
    root["cursor"] = 'watch'
    print("Downloading app from " + item)
    # find command
    URL = item
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    installCommand = soup.find(id="snap-install").text
    subprocess.check_call(installCommand.split(" "))
    # finished install
    root["cursor"] = 'arrow'
    

def checkapps():
    # check for apps
    for widget in appsf.winfo_children():
        widget.destroy()
    root["cursor"] = 'watch'
    print("Loading apps...")
    val = appval.get()
    allapps = searchapps(val)
    for y in allapps:
        Button(appsf, text = y["name"] + " by " + y["by"], command=lambda w=y["link"]: download(w), cursor='hand2').pack()
    root["cursor"] = 'arrow'
    


buttonframe = Frame(frame3)
buttonframe.pack(side=TOP, fill="x")
Label(buttonframe, text = "Search for a snap:").pack(side=LEFT)
appval = Entry(buttonframe)
appval.pack(side=LEFT)
Button(buttonframe, text='Check for snaps', command = checkapps, cursor='hand2').pack(side=LEFT)



appsf = Frame(frame3)
appsf.pack(side=TOP, fill="x")
URL1 = "https://user-images.githubusercontent.com/68869672/193332206-06229bcb-5342-4283-8dfc-a2f0eed72181.gif"
u = urllib.request.urlopen(URL1)
raw_data = u.read()
u.close()
b64_data = base64.encodebytes(raw_data)
image = PhotoImage(data=b64_data)
label = Label(appsf, image=image)
label.pack()
Label(appsf, text="Powered by the Snap Store. Requires snapd.").pack()




notebook.add(frame3, text='Apps Store')
notebook.add(frame1, text='Package Store')
notebook.add(github, text='Github Search')
notebook.add(frame2, text='System')

root.mainloop()
