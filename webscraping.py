import requests
from bs4 import BeautifulSoup
try:
    # for Python3
    import tkinter as tk
except ImportError:
    # for Python2
    import Tkinter as tk

#Passing through false user-agent and browser to bypass Cloudflare(detects scripts/bots/hackers/spamers and it uses Captcha to check it)
headers = {
    'User-Agent': 'Mozilla/5.0'
}

#setting null value
link = 'http://www.enotes.com/homework-help/open-top-boxes-constructed-by-cutting-equal-279105'

#object app
class App:
    def __init__(self):
        #following is basic design + entry field
        self.root = tk.Tk()
        self.root.title("Enter Website URL")
        self.root.geometry("700x200")
        self.entry = tk.Entry(self.root, font=40, width=75)
        self.entry.place(height=10)
        self.entry.pack(pady=5)
        self.entry.focus_set()
        b = tk.Button(self.root, text = "Find Blur", width = 30, command = self.findblurtext)
        b.pack()
        tk.Label(self.root, text="Make Sure To Enter The Correct URL With https://~").pack(padx=30, pady=30)
        self.root.mainloop()
    
    def findblurtext(self):
        link = str(self.entry.get())
        #print(link)
        res = requests.get(link, headers=headers)
        res.raise_for_status()
        Soupobj = BeautifulSoup(res.text, 'html.parser')
        #.select_one("div.c-answer__body o-rte-text u-space--bottom")
        #elem = Soupobj.findAll('div',attrs={"class":"c-answer__body o-rte-text u-space--bottom"})
        top = tk.Toplevel(self.root)
        top.geometry("750x250")
        for div in Soupobj.find_all('div', class_='c-answer__body'):
            for p in div.find_all('p'):
                tk.Label(top, text=p.text).pack(padx=3, pady=3)
                # for each div class name that is found, print

if __name__ == '__main__':
    app = App()
    #init app