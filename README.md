# Email Scraper

This script scrape e-mails from Google Search Terms.

## scraper.py
In the following order.

1. Collect search term (i.e: Developers in London)
2. Connect to Googlesearch API and create a TXT File with URLs to be scraped
3. Open the TXT File and scrape emails.

The script requires Google Module in order to connect to Google API. When you first execute the script it will try to include `googlesearch`, if the module is not installed in your computer it will prompt for automatic download and installation of dependencies. The script will reload once installation is completed.

```Python
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
```

### Install Dependencies from Terminal

To install Google Module use the following command in your terminal.

`pip install google`

To install glob2 Module use the following command in your terminal.

`pip install glob2`

## glob.py

It will put all the TXT files together in one file called result.txt

Remember to delete the URLs files before using glob.

## merge.py

This will verify all repeated emails and merge them.


## EDIT WARNING

The email files (`email - [search-term].txt`) must be edited and all bad lines excluded before `glob.py` and `merge.py` are executed.


#### Update (#1)

* Result limit excluded from prompt and set as 1000 as default. To edit search limit go to the file `config.py` and edit the variable `total`.

```Python
total = 1000 
```

