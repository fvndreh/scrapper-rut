from bs4 import BeautifulSoup
import cloudscraper
import os

url_api = os.getenv("URL_API")

def call_api(rut):
    scraper = cloudscraper.create_scraper()
    form_data = {"term": rut}

    data_items = []
    response = scraper.post(url_api, data=form_data)
    html_response = response.text
    soup = BeautifulSoup(html_response, "html.parser")
    for item in soup.find_all(lambda tag: tag.name in ["th", "td"]):
        data_items.append(item.text)
    
    if len(data_items) % 2 == 0:
        matched_pairs = {}

        for i in range(len(data_items) // 2):
            current_item = data_items[i]
            next_item = data_items[i + len(data_items) // 2]

            matched_pairs[current_item] = next_item

        return matched_pairs
    else:
        return "No data retrieved"