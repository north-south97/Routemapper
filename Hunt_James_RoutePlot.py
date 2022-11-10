#Route Mapper
#Author: James Hunt

#the cord part gets used as a list later.
#the punc bit is for removing punctuation from some lists later on
punc = ",[]'"
cord = []


print("Welcome to route mapper!")

#The grid is stored as 12 lists. The Y coord decides which list, X is which index in that list. 
#If these lists are above the while loop, the Xs will remain. If in the loop, they reset.
#The lists are the wrong way around because i didn't read the instructions till after i did this bit
#They get printed later on with row 12 at the top and 1 at the bottom
#The numbers for each list take up the 0 Index which is simplifies coordinates later on

l1 = ["1  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l2 = ["2  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l3 = ["3  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l4 = ["4  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l5 = ["5  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l6 = ["6  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l7 = ["7  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l8 = ["8  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l9 = ["9  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l10 = ["10 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l11 = ["11 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
l12 = ["12 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]

loop = True
while loop == True:
    

#I'm convinced there's a better way to do this but everytime i change it everything breaks 
    ask = True
    while ask == True:
        file = input("Enter name of route next route or STOP to end: ")
        
        if file == "STOP":
            ask = False
            print("Thanks for using Route Mapper")
            break
#I'm aware that the way ive done this bit means only these 3 files can be used and im not particulally happy with it
#I know there's likely a better way but I refuse to resort to Google        
        if file == "route001.txt":
            route = open(file, "r")
            break
            
        if file == "route002.txt":
            route = open(file, "r")
            break
            
        if file == "route003.txt":
            route = open(file, "r")
            break
            
        else:
            print("File Not Found!")

#This sets the 1st line of the file to X coordinates and the 2nd to Y coordinates
    xcord = (int(route.readline()))
    ycord = (int(route.readline()))

    
    
    go = True
    while go == True:
   
#This bit replaces the relevent part of the list with an X 
#I have also discovered that lower case L is a poor choice of vairable name 
#Unfortunately I've already used it 24 times  
        if ycord == 1:
            l1[int(xcord)] = "_X_|"
            
        elif ycord == 2:
            l2[int(xcord)] = "_X_|"
            
        elif ycord == 3:
            l3[int(xcord)] = "_X_|"
            
        elif ycord == 4:
            l4[int(xcord)] = "_X_|"
            
        elif ycord == 5:
            l5[int(xcord)] = "_X_|"
            
        elif ycord == 6:
            l6[int(xcord)] = "_X_|"
            
        elif ycord == 7:
            l7[int(xcord)] = "_X_|"
            
        elif ycord == 8:
            l8[int(xcord)] = "_X_|"
            
        elif ycord == 9:
            l9[int(xcord)] = "_X_|"
            
        elif ycord == 10:
            l10[int(xcord)] = "_X_|"
            
        elif ycord == 11:
            l11[int(xcord)] = "_X_|"
            
        elif ycord == 12:
            l12[int(xcord)] = "_X_|"
        #this bit is left over from the 1st build i did were I was manually inputing coordinates
        #I don't think it should get printed anymore as it should get overode(overided?) by the error msgs further down but i'll leave it just in case
        else:
            print("~~~~~~~~~~~~~~~~")
            print("#Invalid Input!#")
            print("~~~~~~~~~~~~~~~~")
      
    #This part removes the punctuation from the list output  
    #It uses the punc bit from the start to define what i want removed from the list output
    #otherwise the grid wouldn't print correctly because of the commas and brackets
    #basiclly it sets up a new blank vairable and then puts everyting from the list that isn't in the punc vairable into it
    #Again, im sure i can find a way to do this without repeating it every time for each line/list
      
        l1a = ""
        for char in l1:
            if char not in punc:
                l1a = l1a + char
                
        l2a = ""
        for char in l2:
            if char not in punc:
                l2a = l2a + char
                
        l3a = ""
        for char in l3:
            if char not in punc:
                 l3a = l3a + char
                 
        l4a = ""
        for char in l4:
             if char not in punc:
                 l4a = l4a + char 
                 
        l5a = ""
        for char in l5:
            if char not in punc:
                l5a = l5a + char
                
        l6a = ""
        for char in l6:
            if char not in punc:
                l6a = l6a + char
                
                
        l7a = ""
        for char in l7:
            if char not in punc:
                l7a = l7a + char
                
        l7a = ""
        for char in l7:
            if char not in punc:
                l7a = l7a + char
                
        l8a = ""
        for char in l8:
            if char not in punc:
                l8a = l8a + char
                
        l9a = ""
        for char in l9:
            if char not in punc:
                l9a = l9a + char
                
        l10a = ""
        for char in l10:
            if char not in punc:
                l10a = l10a + char
                
        l11a = ""
        for char in l11:
            if char not in punc:
                l11a = l11a + char
                
        l12a = ""
        for char in l12:
            if char not in punc:
                l12a = l12a + char
        
        
    
    #This bit picks up the next line in the file
        move = route.readline()
                                    
        
        #This bit prints the updated grid   
        #This is also in a loop so every move gets its own plot and set of coords printed below it                          
        print(l12a)
        print(l11a)
        print(l10a)
        print(l9a)
        print(l8a)
        print(l7a)
        print(l6a)
        print(l5a)
        print(l4a)
        print(l3a)
        print(l2a)
        print(l1a)
        print("    1   2   3   4   5   6   7   8   9   10  11  12")
        print("Coordinates for the above plot are " + str(xcord) + "," + str(ycord))
        print("")
        
        #This part builds a list of coordinates for printing at the end.
        cord.append(xcord)
        cord.append(ycord)
       
        
                                    
                                          
                                    
                                    
        #This part converts N S E and W into changes in coordinates                            
        if "N" in move:
            ycord = int(ycord) + 1
                                        
        if "S" in move:
            ycord = int(ycord) - 1
                                
        if "E" in move:
            xcord = int(xcord) + 1
                            
        if "W" in move:
            xcord = int(xcord) - 1
            
        #when it reaches the end of the file, this bit prints the coordinates    
        if move == "":
            print("Route Complete!")
            print("Coordinates: ")
            cord.append("END")
            x = 0
            y = 2
            list = True
            
            while list == True:
                end = cord[x:y]
                print(cord[x:y])
                x = x + 2
                y = y + 2
                if "END" in end:
                    cord.clear()
                    break
           
           #These 3 blocks of lists reset the grid back to empty
           #Otherwise successive routes end up on top of each other
           
            l1 = ["1  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l2 = ["2  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l3 = ["3  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l4 = ["4  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l5 = ["5  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l6 = ["6  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l7 = ["7  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l8 = ["8  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l9 = ["9  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l10 = ["10 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l11 = ["11 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l12 = ["12 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            break
        
        #These 2 bits print errors if the route goes outside the 12x12 grid
        
        if ycord > 12 or ycord < 1:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("# Error! The Y Coordinates of this route go outside the allowed area! #")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            l1 = ["1  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l2 = ["2  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l3 = ["3  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l4 = ["4  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l5 = ["5  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l6 = ["6  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l7 = ["7  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l8 = ["8  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l9 = ["9  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l10 = ["10 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l11 = ["11 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l12 = ["12 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            break
            
        if xcord > 12 or xcord < 1:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("# Error! The X Coordinates of this route go outside the allowed area! #")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            l1 = ["1  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l2 = ["2  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l3 = ["3  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l4 = ["4  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l5 = ["5  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l6 = ["6  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l7 = ["7  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l8 = ["8  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l9 = ["9  ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l10 = ["10 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l11 = ["11 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            l12 = ["12 ","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|","___|"]
            break
           
            #Well that was my first proper program in python, i've wanted to try coding for a while
            #I did actually enjoy it so I think i'll try one of the more advanced course next
            #I've tried to keep it as clean as I can but i still think I can squeeze a some bits into fewer lines
            
            #By James Hunt
            
        
                
                        
        


        


