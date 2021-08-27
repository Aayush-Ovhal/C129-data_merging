import csv
import pandas as pd

df1 = []
df2 = []

with open("bright_stars.csv", 'r', encoding = "utf8") as f:
   csv_reader = csv.reader(f)

   for i in csv_reader:
      df1.append(i)

with open("converted_units.csv", 'r', encoding = 'utf8') as f:
   csv_reader = csv.reader(f)

   for i in csv_reader:
      df2.append(i)

header1 = df1[0]
header2 = df2[0]

planet_data1 = df1[1:]
planet_data2 = df2[1:]

headers = header1 + header2

planet_data = []

for i in planet_data1:
   planet_data.append(i)

for i in planet_data2:
   planet_data.append(i)
  
with open("final_data.csv", "w", encoding = "utf8") as f:
   csvwriter = csv.writer(f)
   csvwriter.writerow(headers)
   csvwriter.writerows(planet_data)