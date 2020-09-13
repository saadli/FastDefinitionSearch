from tkinter import *
import tkinter as tk
from tkinter import ttk
import wikipedia
from tkinter import messagebox
import time


class Fast_Definition():

    def __init__(self, master):
        self.master = master
        self.master.title('Fast Definition')
        self.master.geometry('335x450')
        self.master.config(bg='#589cbf')

        general_font ='TimesNewRoman 10 bold'


        self.my_entry = tk.Entry(self.master, width=50, bd=5)
        self.my_entry.pack(fill=BOTH)
        self.my_btn = tk.Button(self.master, text = 'Search', width=10, font=('TimesNewRoman 10 bold'),
                                bd=5, bg='green', fg='white', command=self.get_item)
        self.my_btn.pack()

        self.my_comobo = ttk.Combobox(self.master, textvariable=StringVar(), font=general_font, state='readonly')
        self.my_comobo.pack()
        self.my_comobo.config(value=('French', 'English', 'Arabic', 'Italian', 'Spanish',
                                     'German', 'Farsi', 'Japanese', 'Russian', 'Ukrainian', 'Chinise'))

        self.my_frame = Frame(self.master, relief=SUNKEN)
        self.my_frame.pack(fill=BOTH)

        self.scroll = tk.Scrollbar(self.my_frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.my_txt = tk.Text(self.my_frame, width= 40, height=20, yscrollcommand = self.scroll.set)
        self.my_txt.config(wrap = 'word')
        self.scroll.config(command=self.my_txt.yview)
        self.my_txt.pack(fill=BOTH)

        self.my_btn_lan = tk.Button(self.master, text='Clear', width=10, font=('TimesNewRoman 10 bold'),
                                    bd=5, bg='green', fg='white', command=self.btn_clear)
        self.my_btn_lan.pack()


    def get_item(self):
        self.entry_value = self.my_entry.get()
        if len(self.entry_value) == 0 or self.my_comobo.get() not in ['French', 'English', 'Arabic', 'Italian', 'Spanish',
                                                                      'German', 'Farsi','Japanese','Russian','Ukrainian','Chinise']:
            tk.messagebox.showerror(title='Error', message='Empty Field')
        else:
            if self.my_comobo.get() == 'French':
                wikipedia.set_lang('fr')
            elif self.my_comobo.get() == 'English':
                wikipedia.set_lang('en')
            elif self.my_comobo.get() == 'Arabic':
                wikipedia.set_lang('ar')
            elif self.my_comobo.get() == 'Italian':
                wikipedia.set_lang('it')
            elif self.my_comobo.get() == 'Spanish':
                wikipedia.set_lang('es')
            elif self.my_comobo.get() == 'German':
                wikipedia.set_lang('de')
            elif self.my_comobo.get() == 'Farsi':
                wikipedia.set_lang('fa')
            elif self.my_comobo.get() == 'Japanese':
                wikipedia.set_lang('ja')
            elif self.my_comobo.get() == 'Russian':
                wikipedia.set_lang('ru')
            elif self.my_comobo.get() == 'Ukranian':
                wikipedia.set_lang('uk')
            elif self.my_comobo.get() == 'Chinese':
                wikipedia.set_lang('zh')
        self.answer = wikipedia.summary(self.entry_value)


        self.my_txt.insert(INSERT, self.answer)
        self.my_txt.config(state=DISABLED)
    def btn_clear(self):
        self.my_txt.config(state=NORMAL)
        self.my_entry.delete(0, END)
        self.my_txt.delete(1.0, END)
def main():
    master = Tk()
    Fast_Definition(master)
    master.mainloop()
if __name__ == '__main__':
    main()