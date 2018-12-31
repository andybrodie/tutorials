def readDiary():
    day = input("What day do you want to read? ")
    file = open(day, "r")
    line = file.read()
    print(line)
    file.close()
    

def writeDiary():
    day = input("What day is your diary for? ")
    file = open(day, "w")
    line = input("Enter entry: ")
    file.write(line)
    file.close()
    
operation = input("Read entries or write entries (R/W)? ")

if (operation == "R"):
    readDiary()
elif (operation == "W"):
    writeDiary()
else:
    print("Sorry, you can only enter a R (for read) or W (for write).  Run the program again.")

print("=== All done ===")
