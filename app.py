'''
Created on Jan 20, 2018

@author: Leslie
'''

import tkinter as tk
from tkinter import *
import getData
import ani_Objects



class AnimeFrame(tk.Frame):
    def __init__(self, key, val, master=None):
        super().__init__(master)
        self.pack(side=LEFT)
        self.create_widgets(key, val)
    
    def create_widgets(self, key, val):
        self.name = tk.Label(self, text=key)
        self.name.pack(side=TOP)
        self.icon = tk.PhotoImage(file=val.get_icon())
        self.icon_lbl = tk.Label(self, bg = "black")
        self.icon_lbl.image=self.icon
        self.icon_lbl.pack()
        self.date = tk.Label(self, text= val.get_date())
        self.date.pack(side=LEFT)
        self.episode = tk.Label(self, text=val.get_episode())
        self.episode.pack(side=RIGHT)
        

anime = getData.anime       
ani = tk.Tk()
for a in anime:
    app = AnimeFrame(a, anime[a], master=ani)
    app.mainloop()
   
        
   


def summ_command():
    summ_top = Toplevel()
    curr_yr = getData.get_Year()
    nxt_yr = int(curr_yr) + 1
    n = str(nxt_yr)
    prev_yr = int(curr_yr) - 1
    p = str(prev_yr)
    prev = Button(summ_top, text= ("Summer" + " " + p), bg = "beige", font="papyrus", relief="groove")
    prev.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    curr = Button(summ_top, text= ("Summer" + " " + curr_yr), bg = "beige", font="papyrus", relief="groove")
    curr.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    nxt = Button(summ_top, text= ("Summer" + " " + n), bg = "beige", font="papyrus", relief="groove")
    nxt.pack(expand = True, side = LEFT, padx = 10, pady = 10)   
    return summ_top


def win_command():
    win_top = Toplevel()
    curr_yr = getData.get_Year()
    nxt_yr = int(curr_yr) + 1
    n = str(nxt_yr)
    prev_yr = int(curr_yr) - 1
    p = str(prev_yr)
    prev = Button(win_top, text= ("Winter" + " " + p), bg = "beige", font="papyrus", relief="groove")
    prev.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    curr = Button(win_top, text= ("Winter" + " " + curr_yr), bg = "beige", font="papyrus", relief="groove")
    curr.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    nxt = Button(win_top, text= ("Winter" + " " + n), bg = "beige", font="papyrus", relief="groove")
    nxt.pack(expand = True, side = LEFT, padx = 10, pady = 10)   
    return win_top

def spr_command():
    spr_top = Toplevel()
    curr_yr = getData.get_Year()
    nxt_yr = int(curr_yr) + 1
    n = str(nxt_yr)
    prev_yr = int(curr_yr) - 1
    p = str(prev_yr)
    prev = Button(spr_top, text= ("Spring" + " " + p), bg = "beige", font="papyrus", relief="groove")
    prev.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    curr = Button(spr_top, text= ("Spring" + " " + curr_yr), bg = "beige", font="papyrus", relief="groove")
    curr.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    nxt = Button(spr_top, text= ("Spring" + " " + n), bg = "beige", font="papyrus", relief="groove")
    nxt.pack(expand = True, side = LEFT, padx = 10, pady = 10)   
    return spr_top


def fall_command():
    fall_top = Toplevel()
    curr_yr = getData.get_Year()
    nxt_yr = int(curr_yr) + 1
    n = str(nxt_yr)
    prev_yr = int(curr_yr) - 1
    p = str(prev_yr)
    prev = Button(fall_top, text= ("Fall" + " " + p), bg = "beige", font="papyrus", relief="groove")
    prev.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    curr = Button(fall_top, text= ("Fall" + " " + curr_yr), bg = "beige", font="papyrus", relief="groove")
    curr.pack(expand = True, side = LEFT, padx = 10, pady = 10)
    nxt = Button(fall_top, text= ("Fall" + " " + n), bg = "beige", font="papyrus", relief="groove")
    nxt.pack(expand = True, side = LEFT, padx = 10, pady = 10)   
    return fall_top



root=tk.Tk()
root.title("Upcoming anime")
root.configure(bg = "black")

button_frame = Frame(root, width=500, height=100)
button_frame.pack(expand = False, side = "bottom", pady = 300)

winter_button = Button(button_frame, text="Winter", bg="white", font="papyrus", relief = "groove", command=win_command)
winter_button.pack(side = LEFT, padx = 10, pady = 10)
spring_button = Button(button_frame, text="Spring", bg="white", font="papyrus", relief = "groove", command=spr_command)
spring_button.pack(side = LEFT, padx = 10, pady = 10)
summer_button = Button(button_frame, text="Summer", bg="white", font="papyrus", relief = "groove", command=summ_command)
summer_button.pack(side = LEFT, padx = 10, pady = 10)
fall_button = Button(button_frame, text="Fall", bg="white", font="papyrus", relief = "groove", command=fall_command)
fall_button.pack(side = LEFT, pady = 10, padx = 10)







#create a side panel with buttons 
'''
panel = Frame(root, width=100, bg="black", height=100, relief="raised", borderwidth = 3)
panel.pack(expand = False, side = "left", fill ="both")
winter_button = Button(panel, text="Winter", bg="white", font="papyrus", cursor="circle")
winter_button.pack()
spring_button = Button(panel,text="Spring", bg="white", font="papyrus",cursor="circle")
spring_button.pack()
summer_button = Button(panel, text="Summer", bg="white", font="papyrus",cursor="circle")
summer_button.pack()
fall_button = Button(panel, text="Fall", bg="white", font="papyrus",cursor="circle")
fall_button.pack()
'''

'''mainarea = Frame(root, bg='white', width=500, height=500)
mainarea.pack(expand=True, fill='both', side='right')
'''
#sakura = tk.PhotoImage(file="sakura.gif")
#lbl = Label(root, bg = "black")
#lbl.image=sakura
#lbl.pack(expand = True)

#anime_frame = Frame(root, height=50, width=150, relief="flat", borderwidth=2)
#anime_frame.pack()


#def get_Winter():
    

#def get_Summer():
    
    

#def get_Fall():

#def get_Spring():
  

root.mainloop()



