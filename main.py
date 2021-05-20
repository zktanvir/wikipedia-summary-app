import tkinter
from tkinter import *
import wikipedia

class WikiApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Wikipedia Summary App')
        self.root.geometry("770x650")
        self.root.resizable(False, False)
        self.root.config(bg='gray')

        self.frame = Frame(
            self.root,
        )
        self.frame.pack()

        self.entry = Entry(
            self.frame, 
            bd=2,
            width=65,
            bg='#FFF',
        )
        self.entry.pack(side=LEFT, ipady=6, expand=True, fill='y')


        self.search_btn = Button(
            self.frame,
            bd=5,
            text='Search',
            command=self.get_summary,
            bg="#FFF",
        )
        self.search_btn.pack(side=LEFT, expand=True, fill='y')
   

        self.text = Text(
            self.root,
            bd=0,
            highlightthickness=0,
            bg='#FFF',
        )
        self.text.pack(expand=True, fill='both')

    def get_summary(self):
        self.text.delete(1.0, END)
        query = self.entry.get()
        try:
            result = wikipedia.summary(query)
        except wikipedia.exceptions.DisambiguationError as e:
            query = e.options[0]
            result = wikipedia.summary(query)
        
        except Exception as ex:
            result = 'Something went wrong!'

        self.text.insert(INSERT, result)
        

    def mainloop(self):
        self.root.mainloop()


wiki_app = WikiApp()
wiki_app.mainloop()
        

