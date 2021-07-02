# Email Scraper
Scrape emails using Google Search Terms

## scraper.py
In the following order.

1. Collect search term (i.e: Developers in London)
2. Collect Result limit (i.e: 100)
3. Connect to Googlesearch API and create a TXT File with URLs to be scraped
4. Open the TXT File and scrape emails.

This script requires Google Module

$pip install google

## glob.py
This requires glob2

$pip install glob2

It will put all the TXT files together in one file called result.txt

Remember to delete the URLs files before using glob.

## merge.py
No module required

This will verify all repeated emails and merge them.


### EDIT WARNING
remember to edit your email files and delete bad lines before using GLOB and MERGE.
