#!C:\python\python.exe
import cgi, os
import csv
import re
import cgitb;
cgitb.enable()
valid=[]
invalid=[]
form = cgi.FieldStorage()
print("Content-Type: text/html\r\n\r\n")
# Get filename here.
fileitem = form['filename']
valmal=form.getvalue('valid')
ivalmal=form.getvalue('invalid')
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   message=fileitem.file.read()
   msg = 'The file was uploaded successfully'
   print(msg)
   regex = re.compile(r'([a-z]+[.-_])*[A-Za-z0-9]+@[gmail$]+(\.[com$]{3})+')
   with open('BULKEMAIL.csv', mode ='r') as file:
       csvFile = csv.DictReader(file)
       for lines in csvFile:
           if re.search(regex, str(lines)):
               valid.append(lines)
           else:
               invalid.append(lines)

else:
   msg = 'No file was uploaded'
   print(msg)
if "valid" in form:
    for list in valid:
         print(list,end='\n')
elif "invalid" in form:
    for ilist in invalid:
        print(ilist,end='\n')
else:
    print(":)")

