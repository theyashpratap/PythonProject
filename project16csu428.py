
#PYTHON PROGRAM TO DISPLAY SYSTEM DETAILS OF A COMPUTER

#BY: YASH PRATAP SINGH
#16CSU428

#TIP: USE WINDOWS TO GET MEMORY ALL DETAILS
#WAIT 1-2 MINUTES TO ALLOW PROGRAM TO GET DETAILS

from tkinter import *
import platform
import subprocess


if(platform.system()=="Windows"):
    s1=subprocess.check_output('systeminfo |find "Total Physical Memory"',shell=True)
    s2=subprocess.check_output('systeminfo |find "Available Physical Memory"',shell=True)
    s3=subprocess.check_output('systeminfo |find "Processor"',shell=True)
    s4=subprocess.check_output('systeminfo |find "System Type"',shell=True)
    s5=subprocess.check_output('wmic cpu get loadpercentage',shell=True)
    s6 = subprocess.check_output('systeminfo |find "BIOS Version"', shell=True)
    s7 = subprocess.check_output('systeminfo |find "Network Card(s)"', shell=True)
    s8 = subprocess.check_output('systeminfo |find "Time Zone"', shell=True)
    s9 = subprocess.check_output('systeminfo |find "Boot Device"', shell=True)


    Mes="                                   Device Running Windows\n                                   All Details Available\n"


else:
    s1 = "Total Physical Memory: Not Available"
    s2 = "Available Physical Memory: Not Available"
    s3 = "Processors Installed: Not Available"
    s4 = "System Type: Not Available"
    s5 = "CPU Load: Not Available"
    s6 = "BIOS Version: Not Available"
    s7 = "Network Card(s):Not Available"
    s8 = "Time Zone: Not Available"
    s9 = "Boot Device: Not Available"

    Mes="                                   System not Running Windows\n                                   Cannot Display all Details\n                                   TIP: Use Windows for all Details"

y1="Machine Type:"+ platform.machine()

y2="Operating System Version:" + platform.version()


y3="Platform Type:"+platform.platform()

y4="Processor:"+platform.processor()

y5="System:"+platform.system()

y6="Architechture:"+str(platform.architecture())

y7="System Nodes:"+platform.node()

y8="Python Version:"+platform.python_version()



root = Tk()
h=Text(root, height=4, width=100)
Mess= Text(root, height=3, width=100)
T = Text(root, height=1, width=100)
T2 = Text(root, height=1, width=100)
T3 = Text(root, height=1, width=100)
T4 = Text(root, height=1, width=100)
T5 = Text(root, height=2, width=100)
T6 = Text(root, height=1, width=100)
T7 = Text(root, height=1, width=100)
T8 = Text(root, height=1, width=100)
T9 = Text(root, height=2, width=100)
x1 = Text(root, height=1, width=100)
x2 = Text(root, height=1, width=100)
x3 = Text(root, height=1, width=100)
x4 = Text(root, height=1, width=100)
x5 = Text(root, height=1, width=100)
x6 = Text(root, height=1, width=100)
x7 = Text(root, height=1, width=100)
x8 = Text(root, height=1, width=100)
h.pack()
Mess.pack()
x1.pack()
x2.pack()
x3.pack()
x4.pack()
x5.pack()
x6.pack()
x7.pack()
x8.pack()
T.pack()
T2.pack()
T3.pack()
T4.pack()
T5.pack()
T6.pack()
T7.pack()
T8.pack()
T9.pack()
h.insert(END,"                                   ***** SYSTEM DETAILS *****\nDevloped By:\nYash Pratap Singh\n16CSU428")
Mess.insert(END,Mes)
x1.insert(END,y1)
x2.insert(END,y2)
x3.insert(END,y3)
x4.insert(END,y4)
x5.insert(END,y5)
x6.insert(END,y6)
x7.insert(END,y7)
x8.insert(END,y8)
T.insert(END,s1)
T2.insert(END,s2)
T3.insert(END,s3)
T4.insert(END,s4)
T5.insert(END,s5)
T6.insert(END,s6)
T7.insert(END,s7)
T8.insert(END,s8)
T9.insert(END,s9)
mainloop()

