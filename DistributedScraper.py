from pyspark import SparkContext
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import csv
import time

def save_to_csv(data, filename="output.csv"):
    if not data:
        print("No data to save.")
        return
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")


def scrape_url(row_range):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://coinmarketcap.com/")

    data = []
    for i in range(row_range[0]+1, row_range[1]+1):
        try:
            row = driver.find_element(By.CSS_SELECTOR, f"tbody tr:nth-child({i})")
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 8:
                data.append({
                    "Name": columns[2].text,
                    "Price": columns[3].text,
                    "Market Cap": columns[7].text,
                    "Volume": columns[8].text,
                })
        except Exception as e:
            print(f"Error in row {i}: {e}")

    driver.quit()
    return data

if __name__ == "__main__":
    start_time = time.time()
    sc = SparkContext("local[*]", "CoinMarketCapScraper")
    row_ranges = [(i, i + 10) for i in range(0, 80, 10)]
    rdd = sc.parallelize(row_ranges)
    results = rdd.map(scrape_url).collect()

    final_data = [item for sublist in results for item in sublist] # Combine results
    save_to_csv(final_data, "crypto_data.csv") # print(final_data)

    print(f"PySpark + Selenium Execution Time: {time.time() - start_time} seconds")
