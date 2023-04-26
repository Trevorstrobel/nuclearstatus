#Author:    Trevor Strobel
#Date:      4/26/23

import urllib3
import re

# Create a pool manager for sending requests
http = urllib3.PoolManager()

# sending a Get request and getting back response as HTTPResponse object.
response = http.request("GET", "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/powerreactorstatusforlast365days.txt")

# Print the returned data
#(print(response.data))

filename="../data/nrc365data.txt"

#print(response.data)

data = response.data

data = data.decode('utf-8').strip('\r')


if(response.status == 200):
    f = open(filename, 'w')
    f.write(data)
    f.close()
    


#open the file and read lines.
f = open(filename, 'r')
lines = f.readlines()
lines = lines[:-1] #dropping the last line. it's empty.

for line in lines:
    #delimiting the line on the "|" character
    l = re.split("\|", line)
    #striping time from date/time
    l[0] = l[0].split(" ", 1)
    l[0] = l[0][0]

    #stripping new line character from the end
    l[2] = l[2].strip("\n")
    
    
    print(l)
    #TODO: data is ready to be put into a database.