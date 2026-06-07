import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"
responses = requests.get(url)
soup = BeautifulSoup(responses.text, "html.parser")
cards = soup.find_all("div", class_="card")

jobs = []
for card in cards:
    vacancy_tag = card.find("h2", class_="title")
    vacancy = vacancy_tag.get_text(strip=True) if vacancy_tag else "N/A"
    company_tag = card.find("h3", class_="company")
    company = company_tag.get_text(strip=True) if company_tag else "N/A"
    location_tag = card.find("p", class_="location")
    location = location_tag.get_text(strip=True) if location_tag else "N/A"
    apply_link = card.find_all("a", string="Apply")[0]["href"]
    jobs.append({
        "vacancy": vacancy,
        "company": company,
        "location": location,
        "apply_link": apply_link
    })

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["vacancy", "company", "location", "apply_link"])
    writer.writeheader()
    writer.writerows(jobs)