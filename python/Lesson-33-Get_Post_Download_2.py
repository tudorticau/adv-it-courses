from urllib import request, parse
import sys

myUrl = "https://www.google.com/search?"
value = {'q': 'ANDESA Soft'}

# send data to google as humans to allow python requests
myheader = {}
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
myheader = {"user-agent": UserAgent}

# catch error
try:
    mydata = parse.urlencode(value)  # parse url to mydata variable
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines() # print all google search results as html page
    for line in otvet:
        print(line)
except Exception:
    print("Error occuried during web request!!")
    print(sys.exc_info()[1])
