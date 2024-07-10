#Author:    Trevor Strobel
#Date:      4/26/23

import urllib3
import re
import sys

# Create a pool manager for sending requests
http = urllib3.PoolManager()

# sending a Get request and getting back response as HTTPResponse object.
response = http.request("GET", "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/powerreactorstatusforlast365days.txt")



filename="../data/nrc365data.txt"



data = response.data

data = data.decode('utf-8').strip('\r').rstrip()




if(response.status == 200):
    f = open(filename, 'w')
    for line in data:
        f.write(line.replace('\n', ''))

    f.close()
    


#open the file and read lines.
f = open(filename, 'r')
#lines = f.read()
#lines = lines[:-1] #dropping the last line. it's empty.

for line in f:
    
    #sys.stdout.write(line)
    #delimiting the line on the "|" character
    l = re.split("\|", line)
    #striping time from date/time
    l[0] = l[0].split(" ", 1)
    l[0] = l[0][0]

    #stripping new line character from the end
    l[2] = l[2].replace("\n", "")

    
    
    print(f"{l}")
    #TODO: data is ready to be put into a database.