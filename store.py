# If you are asking "what is this?",
# you should know that you are not
# doing anything dangerous
# you are just installing the
# LinuxStore for Python (๑˃̵ᴗ˂̵)و

# The dependencies:
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
root.geometry('400x300')
root.title("LinuxStore")
root['cursor'] = 'arrow'


# the app script
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

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
    subprocess.check_call(["npm", "install", app.get()])
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
        Button(github, text = thing["full_name"], command=lambda s=thing["full_name"]: func(s), cursor='hand2').pack()
    root["cursor"] = 'arrow'
    root.update_idletasks()

  


notebook = ttk.Notebook(root,height=1000,width=1000)
notebook.pack(pady=10, expand=True)
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
github = ttk.Frame(notebook, width=400, height=280)
# app search
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
Label(frame1, text = "Search for an app:").pack()
app = Entry(frame1)
app.pack()
Button(frame1, text='Check for apps', command = check, cursor='hand2').pack()
# system info
Label(frame2, text="System Information:").pack()
Label(frame2, text="Welcome back, " + getpass.getuser()).pack()
Label(frame2, text="You're running LinuxStore on python " +  platform.python_version()).pack()

# github search

Label(github, text="Find GitHub repo and download it via git").pack()
github_repo = Entry(github)
github_repo.pack()
Button(github, text="Find a github repo", command=github_search, cursor='hand2').pack()


notebook.add(frame1, text='Store')
notebook.add(github, text='Github Search')
notebook.add(frame2, text='System')

root.mainloop()