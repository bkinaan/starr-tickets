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
                    case "Prize 1":
                        prize1 += name + "\n"
                    case "Prize 2":
                        prize2 += name + "\n"
                    case "Prize 3":
                        prize3 += name + "\n"
                    case "Prize 4":
                        prize4 += name + "\n"
                    case "Prize 5":
                        prize5 += name + "\n"
                        
print("------------------PRINTING LIST 1------------------")
print(prize1)
for i in range(0, 100):
    print(prize1)
print("------------------PRINTING LIST 2------------------")
print(prize2)
print("------------------PRINTING LIST 3------------------")
print(prize3)
print("------------------PRINTING LIST 4------------------")
print(prize4)
print("------------------PRINTING LIST 5------------------")
print(prize5)
print("done")