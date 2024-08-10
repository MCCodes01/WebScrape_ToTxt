import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all text from the page
        text = soup.get_text(separator='\n')
        
        # Write the text to a .txt file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f"Text has been successfully scraped and saved to {output_file}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

#User input the url and output file name
url = "https://medium.com/hashicorp-engineering/hosting-dedicated-terraria-server-to-learn-hcp-boundary-4fd0451834ee"
output_file = "scraped_text.txt"
scrape_text_from_url(url, output_file)

