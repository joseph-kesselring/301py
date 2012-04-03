#Currently this does not check to make sure the data being processed is in fact a valid url.
#Good practices dictate this should be updated to check for and handle this process.
import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfile
#hide tk gui.
Tk().withdraw()
#prompt user for .csv to work with.
fileToRead = askopenfilename(defaultextension="*.csv", title="Select .CSV")
#Print basic author details.
copy = "CSV 301 Redirect\nDeveloped by: Joseph Kesselring (CodeMob, LLC)\nMarch 2012\n\n"
print copy
#these fields are from Google's crawl_errors *.csv file.
fields = ['URL', 'Response Code']
read = csv.DictReader(open(fileToRead, 'rb'), fields)
#prompt user for location and file to save the results to. 
fh = asksaveasfile()
#get domain name for redirection.
http = raw_input("Please input domain name of site: (http://, https://, and/or trailing '/' will be added automatically)\n").strip()
#make sure http is a website.

#add prefix and suffix.
if(http[:6] != "http://"):
    http = "http://" + http
elif(http[:7] != "https://"):
    http = "https://" + http
if(http[-1] != "/"):
    http = http + "/"
offset = http.__len__()
url = ""
#write lines to file.
for row in read:
    if(row['Response Code'] == "404"):
        line = "redirect 301 " + row['URL'][offset:] + " " + http + "\n"
        #this works, but should this be fh.write(line) instead?
        fh.writelines(line)
#Let user know everything is done.
print "\nAll Done!"