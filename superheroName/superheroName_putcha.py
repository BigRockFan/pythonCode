# Rohan P
# 2 May 2018
# superheroName_putcha.py
# gives superhero name based on entered information

from tkinter import *
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = "lime green")
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.head = Label(self, text = "What's your superhero name?", bg = "lime green", fg = "purple4", font = ("Arial", "18", "bold"))
        self.head.grid(row = 1, column = 0, columnspan = 20, padx = 15, pady = 15)
        
        self.q1 = Label(self, text = "Enter your first name: ", bg = "lime green", fg = "blue4", font = ("Arial", "18", "bold"))
        self.q1.grid(row = 2, column = 0, sticky = W)
        self.ent1 = Entry(self, bg = "lime green", fg = "red4", font = ("Arial", "14", "bold"))
        self.ent1.grid(row = 2, column = 1, sticky = W)
        
        self.q2 = Label(self, text = "Enter your last name: ", bg = "lime green", fg = "blue4", font = ("Arial", "18", "bold"))
        self.q2.grid(row = 3, column = 0, sticky = W)
        self.ent2 = Entry(self, bg = "lime green", fg = "red4", font = ("Arial", "14", "bold"))
        self.ent2.grid(row = 3, column = 1, sticky = W)
        
        self.q4 = Label(self, text = "Enter your middle name\n(if NA use last name): ", bg = "lime green", fg = "blue4", font = ("Arial", "18", "bold"))
        self.q4.grid(row = 5, column = 0, sticky = W)
        self.ent3 = Entry(self, bg = "lime green", fg = "red4", font = ("Arial", "14", "bold"))
        self.ent3.grid(row = 5, column = 1, sticky = W)
        
        self.q3 = Label(self, text = "Birth day: ", bg = "lime green", fg = "blue4", font = ("Arial", "18", "bold"))
        self.q3.grid(row = 6, column = 0, sticky = W)
        self.ent4 = Spinbox(self, from_ = 0, to = 31, bg = "lime green", fg = "red4", font = ("Arial", "14", "bold"))
        self.ent4.grid(row = 6, column = 1, sticky = W)
        
        self.sb = Button(self, text = "Submit", command = self.namefinder,
                         bg = "lime green", fg = "red4",
                         font = ("Arial", "12", "bold"))
        self.sb.grid(row = 19, column = 0, sticky = W)
        
        self.clearall = Button(self, text = "Clear", command = self.clearallfields,
                         bg = "lime green", fg = "red4",
                         font = ("Arial", "12", "bold"))
        self.clearall.grid(row = 19, column = 1, sticky = W)
        
    def clearallfields(self):
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.ent4.insert(0, 0)
        
    def namefinder(self):
        self.top = Toplevel(self, bg = "brown1")
        
        myFile1 = open("firstName.txt", "r")
        myFile2 = open("lastName.txt", "r")
        myFile3 = open("middleName.txt", "r")
        myFile4 = open("birthDay.txt", "r")

        #avoids crashes by ensuring all typed fields are full
        if self.ent1.get() == "" or self.ent2.get() == "" or self.ent3.get() == "":
            self.super = Label(self.top, text = "All Fields Required: Incomplete Information", bg = "brown1", fg = "red4", font = ("Arial", "40", "bold"))
            self.super.grid(row = 0, column = 0, columnspan = 20, padx = 15, pady = 15)

        #avoids crashes by ensuring the birthday is logical
        elif int(self.ent4.get()) <= 0 or int(self.ent4.get()) > 31:
            self.super = Label(self.top, text = "Invalid Birthday", bg = "brown1", fg = "red4", font = ("Arial", "40", "bold"))
            self.super.grid(row = 0, column = 0, columnspan = 20, padx = 15, pady = 15)

        else:
            first = ord(((self.ent1.get())[0]).lower()) -96
        
            last = ord(((self.ent2.get())[0]).lower()) -96
        
            middle = ord(((self.ent3.get())[0]).lower()) -96
        
            bday = int(self.ent4.get())

            full_name = ""
            ans = ""
            
            for i in range(first):
                ans = myFile1.readline()
            full_name += ans.strip()
            full_name += " "
            for i in range(last):
                ans1 = myFile2.readline()
            full_name += ans1.strip()
            full_name += ", "
            for i in range(bday):
                ans2 = myFile4.readline()
            full_name += ans2.strip()
            full_name += " "
            for i in range(middle):
                ans3 = myFile3.readline()
            full_name += ans3.strip()
            
            self.intro = Label(self.top, text = "You are... ", justify = CENTER, bg = "brown1", fg = "red4", font = ("Arial", "20", "bold"))
            self.intro.grid(row = 0, column = 0, columnspan = 20)
            
            self.super = Label(self.top, text = full_name, bg = "brown1", fg = "red4", font = ("Arial", "40", "bold"))
            self.super.grid(row = 1, column = 0, columnspan = 20, padx = 15, pady = 15)
            
            
            
root = Tk()
root.title("Superhero name")
root.configure(bg = "lime green")
app = Application(root)
root.mainloop()
