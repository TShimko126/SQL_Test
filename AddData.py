import csv
import sqlite3
from tkFileDialog import askdirectory
from os import listdir


directory = askdirectory()
files = listdir(directory)

txtFiles = []

for f in files:
    if ".txt" in f:
        txtFiles.append(f)

conn = sqlite3.connect("SorterData.db")
c = conn.cursor()

#for f in txtFiles:
curFile = open(directory + "/" + f, "r")
reader = csv.reader(curFile, delimiter="\t")
lineNum = 0
for line in reader:
    if lineNum == 0:
        head = line
        if len(line) == len(head) and lineNum > 0:
            row = line[2]
            column = line[3]
            ext = line[8]
            tof = line[9]
            command = "INSERT INTO rawData VALUES (" + "\"" + str(row) + "\""+ ", " + str(column) + ", " + str(ext) + ", " + str(tof) + ");"
            print command
            c.execute(command)
            conn.commit()
    lineNum += 1

c.close()
