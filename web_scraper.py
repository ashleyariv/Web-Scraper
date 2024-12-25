import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440")
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()

for a in soup.find_all(class_='hasSub'):
    name = a.find('a')
    if name and name.text not in results:
        results.append(name.text)

for b in soup.find_all(class_='hasSub'):
    list = b.find('li')
    if list and list.text not in results:
        other_results.append(list.text)

df = pd.DataFrame({'Names': results, ' List-Items': other_results})
df.to_csv('names.cvs', index=False, encoding='utf-8')