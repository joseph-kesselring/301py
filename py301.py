import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfile
Tk().withdraw()
fileToRead = askopenfilename(defaultextension="*.csv", title="Select .CSV")
copy = "CSV 301 Redirect\nDeveloped by: Joseph Kesselring (CodeMob, LLC)\nMarch 2012\n\n"
print copy
fields = ['URL', 'Response Code']
read = csv.DictReader(open(fileToRead, 'rb'), fields)
fh = asksaveasfile()
http = raw_input("Please input domain name of site: (http:// and trailing / will be added automatically)\n").strip()
if(http[:6] != "http://"):
    http = "http://" + http
if(http[-1] != "/"):
    http = http + "/"
offset = http.__len__()
url = ""
for row in read: 
    if(row['Response Code'] == "404"):
        line = "redirect 301 " + row['URL'][offset:] + " " + http + "\n"
        fh.writelines(line)
print "\nAll Done!"