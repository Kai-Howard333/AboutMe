#Imports -
import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

#Commands:
def doCommand():
      global decENTY
      decimal = int(decENTY.get())
      print()
      print(f"Decimal Input: {decimal}")
      calcBinary()
      calcHex()
      calcOctal()
      print()

#Screen Config -
mainframe = tk.Tk()
mainframe.title("Decimal to Binary/Octal/Hex")
mainframe.geometry("400x250")

inputFrame = tk.Frame(mainframe)
inputFrame.pack(pady=30)

calcBTN = tk.Frame(mainframe)
calcBTN.pack()


#Calculate Button -
calculateBTN = tk.Button(inputFrame, text="Calculate", font=("Times New Roman",14), command=lambda:doCommand())
calculateBTN.pack(side=tk.BOTTOM)

#User Input Label -
INPTLBL = tk.Label(inputFrame, text="Enter a decimal number: ",
                          compound="center",
                          font=("Times New Roman", 14),
                          fg="gold",
                          bg="black")
INPTLBL.pack(side=tk.LEFT)

#Get User Input -
decENTY = tk.Entry(inputFrame, font=("Times New Roman",14))
decENTY.pack(side=tk.LEFT)


#Output Labels -
binOutputLBL = tk.Label(calcBTN, text="Binary Output: ", font=("Times New Roman",14))
binOutputLBL.pack(pady=5)

hexOutputLBL = tk.Label(calcBTN, text="Hexadecimal Output: ", font=("Times New Roman",14))
hexOutputLBL.pack(pady=5)

octOutputLBL = tk.Label(calcBTN, text="Octal Output: ", font=("Times New Roman",14))
octOutputLBL.pack(pady=5)


#Calculate Binary -
def calcBinary():
      global decENTY, binOutputLBL
      decimal = int(decENTY.get())

      binCheckList = []

      i = 0
      while decimal >= 2**i:
          #insert will allow you to put where you want (location,value)
          binCheckList.insert(0,2**i)
          i += 1

      for i in range(len(binCheckList)):
        if decimal >= binCheckList[i]:
            decimal -= binCheckList[i]
            binCheckList[i] = "1"
        else:
            binCheckList[i] = "0"

      binaryOut = ""

      for b in binCheckList:
          binaryOut += b

      print(f"\nBinary: {binaryOut}")

      binOutputLBL.destroy()
      binOutputLBL = tk.Label(calcBTN, text=f"Binary: {binaryOut}", font=("Times New Roman",14))
      binOutputLBL.pack(pady=5)

#Calculate Hexadecimal -
def calcHex():
      global decENTY, hexOutputLBL
      decimal = int(decENTY.get())
      hexCheckList = []
      

      
      i = 0
      while decimal >= 16**i:
            # insert will allow you to put a value where you want (index, value)
            hexCheckList.insert(0,16**i)
            i += 1

      #this loop calculates the bin string or converts int to hexadecimal
      for i in range(len(hexCheckList)):
            #if the 16**hexCheckList[i] is less than or equal to our integer
            remainder = decimal % hexCheckList[i]  #the users number remainder when you divide by 1,16,256,512,etc
            decimal = decimal // hexCheckList[i]   #the users number divided by1,16,256,512,etc with a whole number
            if decimal == 10:
                  letter = 'A'
                  hexCheckList[i] = letter
            elif decimal == 11:
                  letter = 'B'
                  hexCheckList[i] = letter
            elif decimal == 12:
                  letter = 'C'
                  hexCheckList[i] = letter
            elif decimal == 13:
                  letter = 'D'
                  hexCheckList[i] = letter
            elif decimal == 14:
                  letter = 'E'
                  hexCheckList[i] = letter
            elif decimal == 15:
                  letter = 'F'
                  hexCheckList[i] = letter
            else:
                  hexCheckList[i] = str(decimal)
            decimal = remainder
      

      #out put string
      hexOut = ""
      for b in hexCheckList:
            hexOut += str(b)
      print(f"\nHex: {hexOut}")

      hexOutputLBL.destroy()
      hexOutputLBL = tk.Label(calcBTN, text=f"Hexadecimal: {hexOut}", font=("Times New Roman",14))
      hexOutputLBL.pack(pady=5)
#Calculate Octal -
def calcOctal():
      global decENTY, octOutputLBL
      decimal = int(decENTY.get())
      octCheckList = []
      newlist = []

      #this while loop generates the list to calculate the bin string
      i = 0
      while decimal >= 2**i:
            # insert will allow you to put a value where you want (index, value)
            octCheckList.insert(0,2**i)
            i += 1

      #this loop calculates the bin string or converts int to binary
      for i in range(len(octCheckList)):
            #if the 2**octCheckList[i] is less than or equal to our integer
            if decimal >= octCheckList[i]:
                  decimal -= octCheckList[i]
                  octCheckList[i] = "1"
            else:
                  octCheckList[i] = "0"
      # print(octCheckList)
      #out put string
      out = "0b"
      for b in octCheckList:
            out += b
      # print("Binary: ",out)

      if len(octCheckList) % 3 == 1:
            octCheckList.insert(0,0)
            octCheckList.insert(0,0)

      if len(octCheckList) % 3 == 2:
            octCheckList.insert(0,0)
      # print(octCheckList)

      #
      for i in range(len(octCheckList)):
            if i % 3 == 0:
                  newlist.append(octCheckList[i:i+3])
      # print(newlist)

      for i in range(len(newlist)):
            newlist[i] = (int(newlist[i][0]) * 4)+(int(newlist[i][1]) * 2)+(int(newlist[i][2]) * 1)

      octOut=""
      for b in newlist:
            octOut+=str(b)
      print(f"\nOctal: {octOut}")

      octOutputLBL.destroy()
      octOutputLBL = tk.Label(calcBTN, text=f"Octal: {octOut}", font=("Times New Roman",14))
      octOutputLBL.pack(pady=5)


#Last Screen Config -
mainframe.mainloop()