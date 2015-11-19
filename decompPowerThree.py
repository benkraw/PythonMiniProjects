#!/usr/bin/python3

from Tkinter import *
import pdb
fields = ('Enter a Number', 'Decompose')


def decompose(entries):
   next = True
   while(next):
      nums = [1,3,9,27,81]
      #org_target = raw_input("Please enter a number: ")
      org_target = entries['Enter a Number'].get()
      org_target = int(org_target) #Get the number to decompose and cast to an integer
      negative = False
      add = 1
      if org_target < 0: # Check to see if the number is negative
         org_target = abs(org_target)
         negative = True
      target = org_target

      used_nums = []
      how_used = []
      first = True
      summ = 0
      while(True):
         if target == 1: #If the target is equal to one then the number wanted is 1
            temp_nums = [1]
         elif target in range(2,5):
            temp_nums = nums[:2] #Slice array to only use [1,3]
         elif target in range(5,14):
            temp_nums = nums[:3] #Slice array to only use [1,3,9]
         elif target in range(14, 41):
            temp_nums = nums[:4] #Slice array to only use [1,3,9,27]
         else:
            temp_nums = nums #All numbers would be used [1,3,9,27,81]
         summ += temp_nums[-1] * add #Keep adding numbers and checking distance from target
         target = org_target - summ #Calculate distance from the target
         if not first: #If it is not the first iteration check to see if we add or subtract
            if not negative:
               if add == 1: 
                  how_used.append('+')
               else: 
                  how_used.append('-')
            else:
               if add == 1: 
                  how_used.append('-')
               else: 
                  how_used.append('+')
         add = 1 
         if target < 0: #If the target it less than 0 then subtract
            add = -1
         target = abs(target)
         used_nums.append(temp_nums[-1]) #Append all numbers used to create string later on
         if target == 0: #if target is 0 break out of loop, case is done
            break
         first = False
      outstring = '' 
      if negative: #If negative then need to flip the sign first
         outstring += '-'
      for i, num in enumerate(used_nums[:-1]):
         outstring += str(num) + ' ' + how_used[i] + ' ' #loop over created array to create answer string

      outstring += str(used_nums[-1]) 
      if not negative:
         output= str(org_target) + " = " + outstring  #Correct format for output
      else:
         output= "-" + str(org_target) + " = " + outstring 
      entries['Decompose'].delete(0, END)
      entries['Decompose'].insert(0, output)
      next = False


def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   var = StringVar()
   label = Label(root, textvariable=var, relief=RAISED)
   var.set("Created by: Ben Krawitz and Nathan Pilcowitz")
   label.pack()

   root.title("Decomposition Power of 3")
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Submit!',
          command=(lambda e=ents: decompose(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
