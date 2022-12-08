from urllib import request
import sys

# download file from webpage
myUrl = "http://adv400.tripod.com/kartinka.jpg"
myFile = "O:\\invatat\\adv-it-course\\python\\mykartinka.jpg"

try:
    print("Start Downloading file from: " + myUrl)
    request.urlretrieve(myUrl, myFile) # download file from myUrl in myFile
except Exception:
    print("Ahtung !!!!")
    print(sys.exc_info()[1])
    exit()

print("File downloaded and saved at: " + myFile)