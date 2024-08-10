# WebScrape_ToTxt
Web Scraping Script

This Python script scrapes all the text from a given webpage and saves it to a .txt file. The script uses the requests library to send a GET request to the specified URL and the BeautifulSoup library from bs4 to parse the HTML and extract the text.

Features

Sends an HTTP GET request to a specified URL.
Parses the HTML content of the page and extracts all text.
Saves the extracted text to a specified output file in .txt format.
Provides feedback upon successful completion or in case of errors.
Prerequisites

Python 3.6 or higher.
requests library
beautifulsoup4 library
You can install the necessary libraries using pip:

bash
Copy code
pip install requests beautifulsoup4

Usage:

Save the Script: Ensure the script is saved in a .py file, for example, scrape_text.py.
Specify the URL and Output File: Modify the script to input the desired URL and specify the output file name.
Run the Script: Execute the script with Python.

The script will scrape all the text from the specified URL and save it to scraped_text.txt.
Error Handling

The script includes basic error handling. If an HTTP request fails (e.g., due to a connection issue or a bad URL), the script will catch the RequestException and print an error message.

License

This script is provided as-is without any warranty. Feel free to modify and use it for personal or commercial projects.
