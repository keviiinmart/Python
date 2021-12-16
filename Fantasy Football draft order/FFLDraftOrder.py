'''
This program is meant to select the draft order of the upcoming draft
'''

from tkinter import *
import random as rd
from datetime import date

teams = ['Team1','Team2','Team3','Team4','Team5','Team6','Team7','Team8','Team9','Team10']

def randomOrder(listOfTeams):
    numOfTeams = len(listOfTeams)
    draftOrder = []
    numOfLoops = 50

    while len(draftOrder) < numOfTeams:
        for i in range(numOfLoops):
            pickOrder = rd.choice(listOfTeams)

        if pickOrder not in draftOrder:
            draftOrder.append(pickOrder)

    return draftOrder

def NumOfTeams(num):
    num = num + 1
    return num

def exitWindows():
    exit()

def Display(DraftOrder):
    
    root = Tk() #Start of the GUI window
    root.geometry("800x800")#size of thw window

        
    todays_date = date.today()#Gets the year to show in thw window
    year = todays_date.year

    #Start window info
    Title = Label(text=f"The {year} Draft Order\n").grid(row=8,column= 200)
    # InputTeamNum = Label(text="How many teams?").grid(row=10)
    # e1 = Entry(root)
    # e1.grid(row = 10, column=201)
    # Label(text = e1.get()).grid(row=11)


    #prints the order
    Team10 = Label(text=f"The 10th pick goes to team: {DraftOrder[0]}").grid(row=10,column= 200)
    Team9 = Label(text=f"The 9th pick goes to team: {DraftOrder[1]}").grid(row=11,column= 200)
    Team8 = Label(text=f"The 8th pick goes to team: {DraftOrder[2]}").grid(row=12,column= 200)
    Team7 = Label(text=f"The 7th pick goes to team: {DraftOrder[3]}").grid(row=13,column= 200)
    Team6 = Label(text=f"The 6th pick goes to team: {DraftOrder[4]}").grid(row=14,column= 200)
    Team5 = Label(text=f"The 5th pick goes to team: {DraftOrder[5]}").grid(row=15,column= 200)
    Team4 = Label(text=f"The 4th pick goes to team: {DraftOrder[6]}").grid(row=16,column= 200)
    Team3 = Label(text=f"The 3rd pick goes to team: {DraftOrder[7]}").grid(row=17,column= 200)
    Team2 = Label(text=f"The 2nd pick goes to team: {DraftOrder[8]}").grid(row=18,column= 200)
    Team1 = Label(text=f"The 1st pick goes to team: {DraftOrder[9]}").grid(row=19,column= 200)

    

    

    root.mainloop() #End of the GUI window


DraftOrder = randomOrder(teams)
Display(DraftOrder)

