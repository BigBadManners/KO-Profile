
'''

Python script to aggregate Smash player KO data

 ___  ___   ___        ___  __  __  ( )        
| _ )|_ _| / __|      | _ )|  \/  |  \|     ___
| _ \ | | | (_ |      | _ \| |\/| |        (_-/
|___/|___| \___|      |___/|_|  |_|        /__/
 _  __         ___                ___             __  _  _           
| |/ /        / _ \              | _ \ _ _  ___  / _|(_)| | ___  _ _ 
|   <   _    | (_) |  _          |  _/| '_|/ _ \|  _|| || |/ -_)| '_|
|_|\_\ (_)    \___/  (_)         |_|  |_|  \___/|_|  |_||_|\___||_|  



This is not a finished project but it is a working prototype.
Currently the main problem I am aiming to address is making the generation of charts more robust so that I might add extra scenarios in the future (such as KOs off of combos, juggles, landing traps, and so on)


A tribute to - https://shimigames.com/how-when-where-smash-pros-kill/

'''


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys, getopt, time
from textwrap import wrap

'''

class Explode:
    def findExplode(a, b, c):
        chunk1 = 0
        chunk2 = 0
        chunk3 = 0
        if (a > b and a > c):
            chunk1+=0.1
        elif (b > a and b > c):
            chunk2+=0.1
        elif (c > a and c > b):
            chunk3+=0.1
        else:
            print("get noscoped")
        return (chunk1, chunk2, chunk3)

    @findExplode.overload("int","int","int","int")
    def findExplode(self, a, b, c, d):
        chunk1 = 0
        chunk2 = 0
        chunk3 = 0
        chunk4 = 0

    
        if (a > b and a > c and a > d):
            chunk1+=0.1
        elif (b > a and b > c and b > d):
            chunk2+=0.1
        elif (c > a and c > b and c > d):
            chunk3+=0.1
        elif (d > a and d > b and d > c):
            chunk4+=0.1
        else:
            print("get noscoped")


        return (chunk1, chunk2, chunk3, chunk4)

        Will figure out how to do this later...
    
'''

def main(argv):
    global playername

    inputfile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o",["ifile="])
    except getopt.GetoptError:
        print("usage: killprofile -i <inputfile>")
        sys.ex(2)
    for opt, arg in opts:
        if opt == "-h":
            print("usage: killprofile -i <inputfile>")
            print("Input files MUST be formatted under the following fields: [PlayerName], Move(How),Kill%(When),Where,W/L.")
            print("Leave empty fields lie, delimit with commas.")
            sys.exit()
        elif opt in ("-i","--ifile"):
            inputfile = arg
        else:
            print("usage: killprofile -i <inputfile>")

    kill_data = pd.read_csv(inputfile)
    #print(kill_data)
    playername = str(kill_data.columns[0])
    processChart1(kill_data)
    processChart2(kill_data)
    processChart3(kill_data)

    return 0

def processChart1(kill_data):
    ''' Calculate stuff for plotting Chart 1 - K.O. %s '''
    kill_data['Rating'] = pd.cut(kill_data['Kill%(When)'],bins=[0,99,125,150,999],labels=['Under 100%','100-125%','125-150%','Over 150%'])
    ko_range_data = kill_data['Rating'].value_counts(normalize=True,sort=False)


    ko_range_q1 = ko_range_data[0]
    ko_range_q2 = ko_range_data[1]
    ko_range_q3 = ko_range_data[2]
    ko_range_q4 = ko_range_data[3]

    data = [ko_range_q1,ko_range_q2,ko_range_q3,ko_range_q4]
    labels = 'Under 100%','100-125%','125-150%','Over 150%'
    labels = [ '\n'.join(wrap(l,20)) for l in labels]
    colors = ['gold','yellowgreen','lightcoral','lightskyblue']
    explode=findChart1Explode(ko_range_q1,ko_range_q2,ko_range_q3,ko_range_q4)
    plt.pie(data,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.title(playername+"'s Average K.O. %s")
    plt.axis('equal')
    plt.savefig(playername + ' Average KO Percents.png', dpi = 100)
    plt.show()


    return 0

def processChart2(kill_data): 
    ''' Calculate stuff for plotting Chart 2 - K.O. Location '''
    # group the records in kill_data by Where...
    ledge_group = kill_data['Where'].value_counts().loc['L'] # return the total number of rows that have L in column 'Where'
    edgeguard_group = kill_data['Where'].value_counts().loc['E']
    else_group = kill_data['Where'].value_counts().loc['?']

   


    data = [ledge_group,edgeguard_group,else_group]
    labels = 'Ledgetrap/Corner Pressure: '+str(ledge_group), 'Edgeguard/2-frame: '+str(edgeguard_group), 'Elsewhere: '+str(else_group)
    labels = [ '\n'.join(wrap(l,20)) for l in labels]
    colors = ['gold','yellowgreen','lightcoral']
    explode=findChart2Explode(ledge_group,edgeguard_group,else_group)
    plt.pie(data,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.title(playername+"'s Average K.O. Location")
    plt.axis('equal')
    plt.savefig(playername + ' KO Location.png', dpi = 100)
    plt.show()

    return 0


def processChart3(kill_data):
    ''' Calculate stuff for plotting chart 3 - Mean K.O % and Location '''

    kill_data = kill_data.sort_values('Kill%(When)', ascending=False)
   
    # L = Ledgetrap/Corner pressure
    # E = Edgeguard/2-frame
    # ? = Elsewhere (centrestage, grounded, juggle, and so on)

    ''' Calculate stuff for plotting Chart 3 - Kill %s and Location'''
    percent_location = kill_data.groupby(['Where']) # group the records in kill_data by Where...
    ledge_group = percent_location.get_group('L').mean(1) # ONLY return numerical values so we don't accidentally get our field titles caught in the mix...
    edgeguard_group = percent_location.get_group('E').mean(1)
    else_group = percent_location.get_group('?').mean(1)

    ledge_data = ledge_group.mean().round(2) # From ledge_group data, calculate the mean.
    edgeguard_data = edgeguard_group.mean().round(2)
    else_data = else_group.mean().round(2)
   
    # set up piechart plot data
    data = [ledge_data, edgeguard_data, else_data]
    labels = 'Ledgetrap\n('+str(ledge_data)+')', 'Edgeguard/2-frame\n('+str(edgeguard_data)+')', 'Elsewhere\n('+str(else_data)+')'
    plt.bar(labels, data)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.ylabel('Average K.O. %')
    plt.text(5,5,'test')
    plt.title(playername + "'s Average K.O. %")
    plt.savefig(playername + ' Average KO Percents + Location.png', dpi = 100)
    plt.show()

    return 0

def findChart2Explode(a, b, c):
    chunk1 = 0
    chunk2 = 0
    chunk3 = 0
    if (a > b and a > c):
        chunk1+=0.1
    elif (b > a and b > c):
        chunk2+=0.1
    elif (c > a and c > b):
        chunk3+=0.1
    else:
        print("get noscoped")
    return (chunk1, chunk2, chunk3)

def findChart1Explode(a, b, c, d):
    chunk1 = 0
    chunk2 = 0
    chunk3 = 0
    chunk4 = 0

    
    if (a > b and a > c and a > d):
        chunk1+=0.1
    elif (b > a and b > c and b > d):
        chunk2+=0.1
    elif (c > a and c > b and c > d):
        chunk3+=0.1
    elif (d > a and d > b and d > c):
         chunk4+=0.1
    else:
        print("get noscoped")


    return (chunk1, chunk2, chunk3, chunk4)
    
#function calls
if __name__ == "__main__":
    main(sys.argv[1:])

