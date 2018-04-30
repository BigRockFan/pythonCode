#Rohan Putcha
#27 April 2018
#buzzfeedQuiz_putcha.py
#Buzzfeed quiz

from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, bg = "DodgerBlue2")
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.titlelab = Label(self, text = "QUIZ:\nWhich Batman supervillain are you?", bg = "DodgerBlue2", fg =  "blue4", font = ("Arial", "12", "bold"))
        self.titlelab.grid(row = 0, column = 0, columnspan = 15)

        #<----Instruction Label (Q1)---->
        self.label1 = Label(self, text = "Enter name:", bg = "DodgerBlue2", fg = "red4", font = ("Arial", 9, "bold"))
        self.label1.grid(row = 1, column = 0, sticky = W)
        self.nament1 = Entry(self, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.nament1.grid(row = 1, column = 1, sticky = W)

        #<----Instruction label (Q2)---->
        self.label2 = Label(self, text = "What do you want the most (choose one)?", bg = "DodgerBlue2", fg = "red4", font = ("Arial", 9, "bold"))
        self.label2.grid(row = 2, column = 0, sticky = W, columnspan = 15)

        #var for radiobutton:
        self.check_personality = StringVar()
        self.check_personality.set(None)
        
        #create check for justice (two-face)
        self.charent = Radiobutton(self, text = "Justice", variable = self.check_personality, value = "justice", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 3, column = 0, sticky = W)
        
        #create check for money (deathstroke and deadshot)
        self.charent = Radiobutton(self, text = "Money", variable = self.check_personality, value = "money", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 4, column = 0, sticky = W)

        #create check for power (bane)
        self.charent = Radiobutton(self, text = "Power", variable = self.check_personality, value = "power", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 5, column = 0, sticky = W)

        #create check for revenge (scarecrow)
        self.charent = Radiobutton(self, text = "Revenge", variable = self.check_personality, value = "revenge", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 3, column = 1, sticky = W)

        #create check for nothing (joker)
        self.charent = Radiobutton(self, text = "Nothing", variable = self.check_personality, value = "nothing", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 4, column = 1, sticky = W)

         #<----Instruction label (Q3)---->
        self.label3 = Label(self, text = "Which one is your weapon of choice (choose one)?", bg = "DodgerBlue2", fg = "red4", font = ("Arial", 9, "bold"))
        self.label3.grid(row = 6, column = 0, sticky = W, columnspan = 15)

        #var for radiobutton:
        self.check_weapon = StringVar()
        self.check_weapon.set(None)
        
        #create check for gun (deadshot and two-face)
        self.charent = Radiobutton(self, text = " Gun", variable = self.check_weapon, value = "gun", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 7, column = 0, sticky = W)
        
        #create check for fists (bane)
        self.charent = Radiobutton(self, text = " Fists", variable = self.check_weapon, value = "fists", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 8, column = 0, sticky = W)

        #create check for sword (deathstroke)
        self.charent = Radiobutton(self, text = "Sword", variable = self.check_weapon, value = "sword", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 9, column = 0, sticky = W)

        #create check for mind (joker)
        self.charent = Radiobutton(self, text = "Mind", variable = self.check_weapon, value = "mind", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 7, column = 1, sticky = W)

        #create check for fear (scarecrow)
        self.charent = Radiobutton(self, text = "Fear", variable = self.check_weapon, value = "fear", bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.charent.grid(row = 8, column = 1, sticky = W)

         #<----Instruction label (Q4)---->
        self.label4 = Label(self, text = "On a scale of 1-10, how likely would it be for you to use chemicals (in some way), being a villain?", bg = "DodgerBlue2", fg = "red4", font = ("Arial", 9, "bold"))
        self.label4.grid(row = 10, column = 0, sticky = W, columnspan = 15)

        #var for scale:
        self.scalerank = IntVar()

        #create the scale
        self.scale1 = Scale(self, from_ = 0, to = 10, orient = HORIZONTAL, variable = self.scalerank, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.scale1.grid(row = 11, column = 0, sticky = W, columnspan = 2)

        #<----Instruction label (Q5)---->
        self.label5 = Label(self, text = "How would your friends describe you?", bg = "DodgerBlue2", fg = "red4", font = ("Arial", 9, "bold"))
        self.label5.grid(row = 12, column = 0, sticky = W, columnspan = 5)

        #var for optionmenu
        self.describe = StringVar()
        self.describe.set("Description:")
        self.thelist = ["Absolute maniac","Always boasting about skills","Moral person","Greedy for money","Intimidating","Incredibly powerful"]

        #create dropdown menu
        self.opmenu = OptionMenu(self, self.describe, *self.thelist)
        self.opmenu.grid(row = 13, column = 0, sticky = W, columnspan = 3)

        #<----Instruction label (Q6)---->
        self.label6 = Label(self, text = "Select all that apply: What is wrong with people in society?", bg = "DodgerBlue2", fg = "red4", font = ("Arial", 9, "bold"))
        self.label6.grid(row = 14, column = 0, sticky = W, columnspan = 5)

        #create check for puny
        self.people_puny = BooleanVar()
        self.cb1 = Checkbutton(self, text = "They're all so puny", variable = self.people_puny, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.cb1.grid(row = 15, column = 0, sticky = W, columnspan = 5)

        #create check for unjust
        self.people_unjust = BooleanVar()
        self.cb2 = Checkbutton(self, text = "They don't know what's right and what's wrong", variable = self.people_unjust, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.cb2.grid(row = 16, column = 0, sticky = W, columnspan = 5)

        #create check for crazy
        self.people_crazy = BooleanVar()
        self.cb3 = Checkbutton(self, text = "They're crazy, just like everything else in this world", variable = self.people_crazy, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.cb3.grid(row = 17, column = 0, sticky = W, columnspan = 5)

        #create check for money
        self.people_money = BooleanVar()
        self.cb3 = Checkbutton(self, text = "They don't pay enough money", variable = self.people_money, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.cb3.grid(row = 15, column = 5, sticky = W, columnspan = 5)

        #create check for confidence
        self.people_confidence = BooleanVar()
        self.cb3 = Checkbutton(self, text = "They're too confident and brave", variable = self.people_confidence, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.cb3.grid(row = 16, column = 5, sticky = W, columnspan = 5)

        #create check for inaccuracy
        self.people_inaccuracy = BooleanVar()
        self.cb3 = Checkbutton(self, text = "They're so inaccurate in everything they do", variable = self.people_inaccuracy, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.cb3.grid(row = 17, column = 5, sticky = W, columnspan = 5)

        #submit
        self.submit = Button(self, text = "Submit", command = self.calculate, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.submit.grid(row = 18, column = 0, sticky = W)

        #textbox with results
        self.results = Text(self, width = 60, height = 5, wrap = WORD, bg = "DodgerBlue2", fg = "blue4", font = ("Arial", 9, "bold"))
        self.results.grid(row = 19, column = 0, columnspan = 5)

    def calculate(self):
        #order: Scarecrow, Joker, Two-face, Bane, Deathstroke, Deadshot
        villains = [0,0,0,0,0,0]

        #<<< 2 >>>
        if self.check_personality.get() == "justice":
            villains[2] += 1
        elif self.check_personality.get() == "money":
            villains[4] += 1
            villains[5] += 1
        elif self.check_personality.get() == "power":
            villains[3] += 1
        elif self.check_personality.get() == "revenge":
            villains[0] += 1
        elif self.check_personality.get() == "nothing":
            villains[1] += 1

        #<<< 3 >>>
        if self.check_weapon.get() == "gun":
            villains[5] += 1
            villains[2] += 1
        elif self.check_weapon.get() == "fists":
            villains[3] += 1
        elif self.check_weapon.get() == "sword":
            villains[4] += 1
        elif self.check_weapon.get() == "mind":
            villains[1] += 1
        elif self.check_weapon.get() == "fear":
            villains[0] += 1

        #<<< 4 >>>
        chemicals = self.scalerank.get()
        if chemicals == 10 or chemicals == 9:
            villains[0] += 1
        elif chemicals == 8 or chemicals == 7:
            villains[3] += 1
        elif chemicals == 6 or chemicals == 5:
            villains[1] += 1
        else:
            villains[2] += 1
            villains[4] += 1
            villains[5] += 1
            
        #<<< 5 >>>
        if self.describe.get() == "Absolute maniac":
            villains[1] += 1
        elif self.describe.get() == "Always boasting about skills":
            villains[5] += 1
        elif self.describe.get() == "Moral person":
            villains[2] += 1
        elif self.describe.get() == "Greedy for money":
            villains[4] += 1
        elif self.describe.get() == "Intimidating":
            villains[0] += 1
        elif self.describe.get() == "Incredibly powerful":
            villains[3] += 1

        #<<< 6 >>>
        if self.people_puny.get() == True:
            villains[3] += 1
        if self.people_unjust.get() == True:
            villains[2] += 1
        if self.people_crazy.get() == True:
            villains[1] += 1
        if self.people_money.get() == True:
            villains[4] += 1
        if self.people_confidence.get() == True:
            villains[0] += 1
        if self.people_inaccuracy.get() == True:
            villains[5] += 1

        #for loop to find the index with the largest number
        maxnum = -1
        for i in villains:
            if i > maxnum:
                maxnum = i

        #finds all the villains with the same number and puts their indices into all_pos
        all_poss = []
        counter = 0
        for i in villains:
            if i == maxnum:
                all_poss += [counter,]
            counter += 1
            
        #if multiple villains have the same number, a random villain
        #out of the highest numbers is selected
        randy = random.randint(0, len(all_poss)-1)
        villain_num = all_poss[randy]
        
        if villain_num == 0:
            final_villain = "Scarecrow"
        elif villain_num == 1:
            final_villain = "Joker"
        elif villain_num == 2:
            final_villain = "Two-face"
        elif villain_num == 3:
            final_villain = "Bane"
        elif villain_num == 4:
            final_villain = "Deathstroke"
        elif villain_num == 5:
            final_villain = "Deadshot"
        
        final_print = ""
        final_print += "Hello, " +self.nament1.get()+ "! Thanks for taking the quiz!\n"
        final_print += "Your results:\n"
        final_print += "You got " + final_villain + "!!!"
        self.results.delete(0.0, END)
        self.results.insert(0.0, final_print)
        
        
root = Tk()
root.title("Buzzfeed Quiz")
root.configure(bg = "DodgerBlue2")
app = Application(root)
root.mainloop()

