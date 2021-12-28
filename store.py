# If you are asking "what is this?",
# you should know that you are not
# doing anything dangerous
# you are just installing the
# LinuxStore (๑˃̵ᴗ˂̵)و


from tkinter import *
import tkinter.ttk as ttk
import subprocess
import sys
import urllib.request
import urllib.error

result = ""

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_pip():
    install(app.get())
    Label(frame1, text="Installed app via pip").pack()

def install_npm():
    subprocess.check_call(["npm", "install", app.get()])
    Label(frame1, text="Installed app via npm").pack()

def check():
    # find on PyPi
    try:
        with urllib.request.urlopen('https://pypi.org/simple/' + app.get() + "/") as f:
            result = f.read(13)
    except urllib.error.HTTPError as e:
        result = "404 Not Found"
    except urllib.error.URLError as e:
        print("Something went wrong")
    if result != "404 Not Found":
        Button(frame1, text = "Install " + app.get() +" on PyPi", command = install_pip).pack()
        
    # search on npm
    try:
        with urllib.request.urlopen('https://www.npmjs.com/package/' + app.get()) as f:
            result = f.read(13)
    except urllib.error.HTTPError as e:
        result = "404 Not Found"
    except urllib.error.URLError as e:
        print("Something went wrong")
    if result != "404 Not Found":
        Button(frame1, text = "Install " + app.get() + " on npm", command = install_npm).pack()
    
root = Tk()
root.geometry('400x300')
root.title("LinuxStore")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
Label(frame1, text = "Search for an app:").pack()
app = Entry(frame1)
app.pack()

    
Button(frame1, text='Check for apps', command = check).pack()
notebook.add(frame1, text='Store')
notebook.add(frame2, text='My Account')


root.mainloop()