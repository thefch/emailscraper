import os
clear = lambda: os.system("cls")
clear()
from config import total

print("#########################################################")
print("#        Email Scraper - Dev. By Wellyington            #")
print("#          https://wellyington.github.io/               #")
print("#########################################################\n\n")

try:
    from googlesearch import search
except:
    upgrade_pip = lambda: os.system("pip install --upgrade pip")
    install_google = lambda: os.system("pip install google glob2")
    reload_scraper = lambda: os.system("python scraper.py")
    print("Upgrading Pip")
    print("----------------------------------------------------------")
    upgrade_pip()
    print("Downloading Google Library and Glob2")
    print("----------------------------------------------------------")
    install_google()
    print("Instalation complete: Ready to start scraping")
    print("----------------------------------------------------------")
    reload_scraper()
import re, urllib.request, time
print("What is the search term?")
query = input("Search: ")
print("\n\n----------------------------------------------------------")
print("Starting Scrapping Function")
print("----------------------------------------------------------")
for j in search(query, tld="com", num=int(total), stop=int(total), pause=2):
    URLs = open("urls - " + query + ".txt","a")
    URLs.write(j + "\n")
    print(j)

emailRegex = re.compile(r'''
#example :
#something-.+_@somedomain.com
(
([a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+)
)
''', re.VERBOSE)

#Extacting Emails
def extractEmailsFromUrlText(urlText):
    extractedEmail = emailRegex.findall(urlText)
    allemails = []
    for email in extractedEmail:
        allemails.append(email[0])
    lenh = len(allemails)
    print("\tNumber of Emails : %s\n"%lenh )
    seen = set()
    for email in allemails:
        if email not in seen:  # faster than `word not in output`
            seen.add(email)
            emailFile.write(email+"\n") #appending Emails to a filerea

#HtmlPage Read Func
def htmlPageRead(url, i):
    try:
        start = time.time()
        headers = { 'User-Agent' : 'Mozilla/5.0' }
        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request)
        urlHtmlPageRead = response.read()
        urlText = urlHtmlPageRead.decode()
        print ("%s.%s\tFetched in : %s" % (i, url, (time.time() - start)))
        extractEmailsFromUrlText(urlText)
    except:
        pass
    
#EmailsLeechFunction
def emailsLeechFunc(url, i):
    
    try:
        htmlPageRead(url,i)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            try:
                url = 'http://webcache.googleusercontent.com/search?q=cache:'+url
                htmlPageRead(url, i)
            except:
                pass
        else:
            pass    
      
# TODO: Open a file for reading urls
start = time.time()
urlFile = open("urls - " + query + ".txt", 'r')
emailFile = open("emails - " + query + ".txt", 'a')
i=0
#Iterate Opened file for getting single url
for urlLink in urlFile.readlines():
    urlLink = urlLink.strip('\'"')
    i=i+1
    emailsLeechFunc(urlLink, i)
print ("Elapsed Time: %s" % (time.time() - start))

urlFile.close()
emailFile.close()

print("\n\n----------------------------------------------------------")
print("Scrapping Function Ended")
print("----------------------------------------------------------")