import csv

prize1 = ""
prize2 = ""
prize3 = ""
prize4 = ""
prize5 = ""
empty = ""

with open('data3.csv', 'r') as csv_file:
    for row in csv_file.readlines():
        column = row.split(',')
        name = column[1]
        if name != "Little Buddy's First and Last Name":
            for item in range(2, 6):
                prize = column[item].replace('\n', '')
                if prize == "Light-Up Terrarium":
                    prize1 += name + "\n"
                elif prize ==  "Magnetic Pen":
                    prize2 += name + "\n"
                elif prize == "Heart Eyes Emoji":
                    prize3 += name + "\n"
                elif prize == "Dino":
                    prize4 += name + "\n"
                elif prize == "Sticker Book":
                    prize5 += name + "\n"
                else:
                    empty += name + "\n"
                    
                        
print("------------------PRINTING Light-Up Terrarium------------------")
print(prize1)
print("------------------PRINTING Magnetic Pen------------------")
print(prize2)
print("------------------PRINTING Heart Eyes Emoji------------------")
print(prize3)
print("------------------PRINTING Dino------------------")
print(prize4)
print("------------------PRINTING Sticker Book------------------")
print(prize5)
print("done")