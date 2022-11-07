import os
import re
import time
import urllib.request
from config import total

os.system("cls")


print("#########################################################")
print("#        Email Scraper - Dev. By Wellyington            #")
print("#                        thefch                         #")
print("#########################################################\n\n")

try:
    from googlesearch import search
except:
    print("Upgrading Pip")
    print("----------------------------------------------------------")
    os.system("pip3 install --upgrade pip")
    print("Downloading Google Library and Glob2")
    print("----------------------------------------------------------")
    os.system("pip3 install google glob2")
    print("Installation complete: Ready to start scraping")
    print("----------------------------------------------------------")
    os.system("python3 scraper.py")


print("What is the search term?")
query = input("Search: ")
print("\n\n----------------------------------------------------------")
print("\033[1;32;40mStarting Scrapping Function\033[0;37;40m")
print("----------------------------------------------------------")
for j in search(query, tld="com", num=int(total), stop=int(total), pause=2):
    URLs = open("urls - " + query + ".txt", "a")
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


# Extracting Emails
def extract_emails_from_url_text(urlText):
    extracted_email = emailRegex.findall(urlText)
    all_emails = []
    for email in extracted_email:
        all_emails.append(email[0])

    print("\tNumber of Emails : %s\n" % len(all_emails))
    seen = set()
    for email in all_emails:
        if email not in seen:  # faster than `word not in output`
            seen.add(email)
            emailFile.write(email + "\n")  # appending Emails to a file


# HtmlPage Read Func
def html_page_read(url, i):
    try:
        start_time = time.time()
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request)
        url_html_page_read = response.read()
        url_text = url_html_page_read.decode()
        print("%s.%s\tFetched in : %s" % (i, url, (time.time() - start_time)))
        extract_emails_from_url_text(url_text)
    except:
        pass


# EmailsLeechFunction
def emails_leech_func(url, i):
    try:
        html_page_read(url, i)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            try:
                url = 'http://webcache.googleusercontent.com/search?q=cache:' + url
                html_page_read(url, i)
            except:
                pass
        else:
            pass

        # TODO: Open a file for reading urls


start = time.time()
urlFile = open("urls - " + query + ".txt", 'r')
emailFile = open("emails - " + query + ".txt", 'a')
i = 0
# Iterate Opened file for getting single url
for urlLink in urlFile.readlines():
    urlLink = urlLink.strip('\'"')
    i = i + 1
    emails_leech_func(urlLink, i)
print("Elapsed Time: %s" % (time.time() - start))

urlFile.close()
emailFile.close()

print("\n\n----------------------------------------------------------")
print("\033[1;32;40mScrapping Function Ended\033[0;37;40m")
print("----------------------------------------------------------")
