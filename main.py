"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Tereza Petrová  
email: tereza.petrova00@gmail.com
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv


def validate_args():
    if len(sys.argv) != 3:
        print("Chyba: Skript vyžaduje 2 argumenty – URL a výstupní CSV.")
        sys.exit(1)
    url, output = sys.argv[1], sys.argv[2]
    if not url.startswith("http"):
        print("Chyba: První argument musí být platná URL.")
        sys.exit(1)
    if not output.lower().endswith(".csv"):
        print("Chyba: Druhý argument musí být název souboru s koncovkou .csv.")
        sys.exit(1)
    return url, output

def get_soup(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")

def get_municipalities(url):
    soup = get_soup(url)
    municipalities = []

    tables = soup.find_all("table", {"class": "table"})
    for table in tables:
        for row in table.find_all("tr")[2:]:  
            cells = row.find_all("td")
            for i in range(0, len(cells), 2):
                if i + 1 < len(cells):
                    code_cell = cells[i]
                    name_cell = cells[i + 1]
                    if a := code_cell.find("a"):
                        code = code_cell.text.strip()
                        name = name_cell.text.strip()
                        link = "https://www.volby.cz/pls/ps2017nss/" + a["href"]
                        municipalities.append((code, name, link))
    return municipalities

def parse_municipality_page(code, name, url):
    """Načte detailní stránku obce a vrátí výsledky"""
    soup = get_soup(url)
    tables = soup.find_all("table")

    summary_table = tables[0]
    rows = summary_table.find_all("tr")
    try:
        cells = rows[2].find_all("td")  
        volici = cells[3].text.strip().replace('\xa0', '')
        obalky = cells[4].text.strip().replace('\xa0', '')
        hlasy = cells[7].text.strip().replace('\xa0', '')
    except IndexError:
        volici = obalky = hlasy = "0"

    party_tables = tables[1:]
    results = {}
    for t in party_tables:
        for row in t.find_all("tr")[2:]:
            tds = row.find_all("td")
            if len(tds) >= 3:
                party = tds[1].text.strip()
                votes = tds[2].text.strip().replace('\xa0', '')
                results[party] = votes

    return {
        "kód obce": code,
        "název obce": name,
        "voliči v seznamu": volici,
        "vydané obálky": obalky,
        "platné hlasy": hlasy,
        **results
    }

def save_to_csv(data_list, filename):
    base = ["kód obce", "název obce", "voliči v seznamu", "vydané obálky", "platné hlasy"]
    parties = sorted({k for d in data_list for k in d.keys() if k not in base})
    fieldnames = base + parties

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data_list:
            for p in parties:
                row.setdefault(p, "0")
            writer.writerow(row)

def main():
    start_url, output = validate_args()
    print("Načítám seznam obcí…")
    municipalities = get_municipalities(start_url)
    print(f"Nalezeno obcí: {len(municipalities)}")

    data = []
    for code, name, link in municipalities:
        print(f"– Zpracovávám: {name} ({code})")
        data.append(parse_municipality_page(code, name, link))

    save_to_csv(data, output)
    print("Hotovo!")

if __name__ == "__main__":
    main()