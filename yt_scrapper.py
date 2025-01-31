import time
import json
import csv
import datetime
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def txt_to_array(filename):
    """
        Reads YouTube URLs from a text file and returns them as a list.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f" Error: File '{filename}' not found!")
        exit(1)
    
# Argument Parser
parser = argparse.ArgumentParser(description="YouTube Video Scraper - Extracts titles & descriptions.")
parser.add_argument("-f", "--filepath", type=str, required=True, help="Path to the text file containing YouTube URLs.")
parser.add_argument("-o", "--output-format", type=str, choices=["csv", "json", "both"], default="both",
                    help="Output format: csv, json, or both (default: both).")
args = parser.parse_args()



# Load url from txt file
txt_file = args.filepath
video_urls = txt_to_array(txt_file)

# timestamp for unique file names 
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
csv_filename = f"yt_desc_{timestamp}.csv"
json_filename = f"yt_desc_{timestamp}.json"

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run Chrome in the background
chrome_options.add_argument("--disable-gpu")  # Prevents GPU rendering issues
chrome_options.add_argument("--no-sandbox")  # Bypass OS security restrictions
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents shared memory issues
chrome_options.add_argument("--log-level=3")  # Suppresses unnecessary logs
chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Block images (faster loading)
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream": 2,  # Block video & audio autoplay
    "profile.default_content_setting_values.sound": 2,  # Disable all sounds
    "profile.default_content_setting_values.images": 2,  # Block images (optional)
})


# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

data = []

try:
    for url in video_urls:
        driver.get(url)
        wait = WebDriverWait(driver, 15)

        print(f"🔄 ⚠ Scrapping: {url}")

        # Extract Video Title
        try:
            title_ele = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#title yt-formatted-string"))
            )
            video_title = title_ele.text.strip()
        except:
            print(f"⚠ Could not extract title for {url}")
            video_title = "N/A"

        # Click "Show More"
        try:
            show_more_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#expand"))
            )
            show_more_button.click()
            time.sleep(2)
        except:
            print("ℹ No 'Show More' button found. Extracting description...")

        
        # Extract video description
        try:
            description_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#description-inline-expander yt-attributed-string"))
            )
            description_text = description_element.text.strip()
        except Exception as e:
            print(f"⚠ Could not extract description for {url}: {e}")
            description_text = "N/A"

        data.append({
            "url": url, 
            "title": video_title,
            "description": description_text
        })

        print(f"✅ Successfully scraped: {video_title}")

    if args.output_format in ["csv", "both"]:
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["url", "title", "description"])
            writer.writeheader()
            writer.writerows(data)
            
    if args.output_format in ["json", "both"]:
        with open(json_filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    print(f"\n Data saved to:\n - {csv_filename}\n - {json_filename}")

finally:
    driver.quit()
