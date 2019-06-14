import pandas as pd
df = pd.read_csv('untitled.txt', sep='|')
def convert_row(row):
    return """<movietitle="%s">
    <type>%s</type>
    <format>%s</format>
    <year>%s</year>
    <rating>%s</rating>
    <stars>%s</stars>
    <description>%s</description>
</movie>""" % (
    row.Title, row.Type, row.Format, row.Year, row.Rating, row.Stars, row.Description)

print '\n'.join(df.apply(convert_row, axis=1))
import csv              
f = open('movies2.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
   data.append(row)
f.close()

print data[1:]
