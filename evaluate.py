import csv

prize1 = ""
prize2 = ""
prize3 = ""
prize4 = ""
prize5 = ""

with open('data.csv', 'r') as csv_file:
    for row in csv_file.readlines():
        column = row.split(',')
        name = column[1]
        if name != "Little Buddy's First and Last Name":
            for item in range(2, 8):
                prize = column[item].replace('\n', '')
                match prize:
                    case "Dino Launcher":
                        prize1 += name + "\n"
                    case "Magnetic Tiles":
                        prize2 += name + "\n"
                    case "Gem Art Kit":
                        prize3 += name + "\n"
                    case "Elephant":
                        prize4 += name + "\n"
                    case "Dog":
                        prize5 += name + "\n"
                        
print("------------------PRINTING Dino Launcher------------------")
print(prize1)
print("------------------PRINTING Magnetic Tiles------------------")
print(prize2)
print("------------------PRINTING Gem Art Kit------------------")
print(prize3)
print("------------------PRINTING Elephant------------------")
print(prize4)
print("------------------PRINTING Dog------------------")
print(prize5)
print("done")