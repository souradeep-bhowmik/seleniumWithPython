# seleniumWithPython
__Date of Project:__ April 2019

This project was my first try at selenium automation. I have used Python to code a web scraper that extracts first names from a website and last names form another website using headless Chrome and a form filler that uses this information to create Google accounts. The web scraper uses XPath for capturing the names in both the websites and then loads them into two separate files, one for first and the other for last names. The form filler Python script takes into account the username suggestions automatically provided by Google, and if for some reason they do not appear (which seems to be the case for quite a few times) it creates its own username using the first and last names and then appending a randomly generated number at the end. If the username already exists, the Google accounts website will give an error and the Python script handles this exception and continues to the next iteration instead of stopping the script. These two tricks ensure a 100% success rate in account creation.

_NOTE:_ One thing to note is that Google requires phone numbers for account creation, so the script does not actually create an account, rather it fills the form itself and handles all exceptions, if any.

__Web scraping:__ A web scraper is used to extract data from websites. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis. Web scraping a web page involves fetching it and extracting from it. The content of a page may be parsed, searched, reformatted, its data copied into a spreadsheet, and so on. Web scrapers typically take something out of a page, to make use of it for another purpose somewhere else. An example would be to find and copy names and phone numbers, or companies and their URLs, to a list (contact scraping).

Wiki source and more information: https://en.wikipedia.org/wiki/Web_scraping

__Form filler:__ A form filler is a software program that automatically fills forms in a UI. Form fillers can be part of a larger program, like a password manager or an enterprise single sign-on (E-SSO) solution.

Wiki source and more information: https://en.wikipedia.org/wiki/Form_filler

# Instructions for environment setup:
* Install __Python 3.x.x__ using [Python downloads page](https://www.python.org/downloads/) and selecting your operating system and latest stable release
* Install __Selenium__ in Python using `[sudo] pip install selenium`

_NOTE:_ You don't need to download a chrome webdriver because I have uploaded the same along with my Python scripts.

# Execution instructions:
* First execute the _Web_Scraper.py_ using `python Web_Scraper.py`. This will create two files: `first_names.txt` and `last_names.txt`
* Then execute the _Form_Filler.py_ using `python Form_Filler.py`
