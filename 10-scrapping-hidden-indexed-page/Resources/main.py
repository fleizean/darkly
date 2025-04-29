import requests
from bs4 import BeautifulSoup
import time

""" def scrape_readme_files(url, output_file, keywords, count_active, count=22, sleep_counter=0):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    with open(output_file, 'a') as outfile:
        for link in soup.find_all('a'):
            print(f"Scraping {link.get('href')} from {url}")
            href = link.get('href')
            if href == "../":
                continue
            if count > 0 and count_active:
                count -= 1
                continue
            if count_active and href == "whtccjokayshttvxycsvykxcfm/":
                count_active = False
                print("Count is now inactive")
            full_url = url + href
            if href.endswith('/'):
                scrape_readme_files(full_url, output_file, keywords, count_active, count, sleep_counter)
            elif href == "README":
                readme_response = requests.get(full_url)
                if readme_response.status_code == 200:
                    content = readme_response.text
                    if not any(keyword in content for keyword in keywords):
                        print(f"Found README without keywords at {full_url}")
                        outfile.write(f"Contents of {full_url}:\n")
                        outfile.write(content)
                        outfile.write("\n\n")
            sleep_counter += 1
            if sleep_counter % 6 == 0:
                print("Sleeping for 1 second")
                time.sleep(1)

base_url = "http://localhost:8080/.hidden/"
output_file = "output.txt"
keywords = ["Demande", "Tu veux", "Toujours", "Non ce"]

# Clear the output file before starting
open(output_file, 'w').close()

# Start scraping
scrape_readme_files(base_url, output_file, keywords, count_active=True) """

# Üstteki versiyon hızlıca bitirmek için alttaki realistik versiyonu yazdım.

def scrape_readme_files(url, output_file, keywords, sleep_counter):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    with open(output_file, 'a') as outfile:
        for link in soup.find_all('a'):
            print(f"Scraping {link.get('href')} from {url}")
            href = link.get('href')
            if href == "../":
                continue
            full_url = url + href
            if href.endswith('/'):
                scrape_readme_files(full_url, output_file, keywords, sleep_counter)
            elif href == "README":
                readme_response = requests.get(full_url)
                if readme_response.status_code == 200:
                    content = readme_response.text
                    if not any(keyword in content for keyword in keywords):
                        print(f"Found README without keywords at {full_url}")
                        outfile.write(f"Contents of {full_url}:\n")
                        outfile.write(content)
                        outfile.write("\n\n")
            sleep_counter += 1
            if sleep_counter % 6 == 0:
                print("Sleeping for 1 second")
                time.sleep(1)

base_url = "http://localhost:8080/.hidden/"
output_file = "output.txt"
keywords = ["Demande", "Tu veux", "Toujours", "Non ce"]

# Clear the output file before starting
open(output_file, 'w').close()

# Start scraping
scrape_readme_files(base_url, output_file, keywords, sleep_counter=0)