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

def scrape_all_rows(start_row=1, end_row=80):
    # Set up Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://coinmarketcap.com/")

    data = []
    for i in range(start_row, end_row + 1):
        try:
            # Find row using nth-child
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
    print("Starting pure Selenium scraper...")

    # Scrape all rows in a single loop
    final_data = scrape_all_rows(1, 1000)
    
    # Save the results to a CSV
    save_to_csv(final_data, "crypto_data.csv")

    # Measure and print execution time
    print(f"Pure Selenium Execution Time: {time.time() - start_time} seconds")
