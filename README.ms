# **YouTube Video Scraper**  

A Python script to extract video titles and descriptions from a list of YouTube URLs using **Selenium**. The extracted data can be saved in **CSV**, **JSON**, or both formats.

## **Features**
✅ Scrapes **YouTube video titles** and **descriptions**  
✅ Supports **CSV** and **JSON** output formats  
✅ Uses **headless Chrome** for fast and efficient scraping  
✅ CLI-based execution with error handling  

---

## **Requirements**
- Python 3.x  
- Google Chrome (latest version)  
- Chrome WebDriver (compatible with your Chrome version)  

---

## **Installation**
1️⃣ **Clone the repository:**  
```sh
git clone https://github.com/your-username/youtube-video-scraper.git
cd youtube-video-scraper
```

2️⃣ **Install dependencies:**  
```sh
pip install -r requirements.txt
```

---

## **Usage**
Run the script with a text file containing YouTube URLs:

```sh
python scraper.py -f urls.txt -o csv
```

### **Arguments:**
| Argument | Description | Required |
|----------|------------|----------|
| `-f, --filepath` | Path to the text file containing YouTube URLs | ✅ |
| `-o, --output-format` | Output format: `csv`, `json`, or `both` (default: `both`) | ❌ |

Example:
```sh
python scraper.py -f youtube_links.txt -o both
```

---

## **Input File Format**
Create a **text file** (`urls.txt`) with **one YouTube URL per line**:

```
https://www.youtube.com/watch?v=videoID1
https://www.youtube.com/watch?v=videoID2
https://www.youtube.com/watch?v=videoID3
```

---

## **Output**
After execution, the script saves the extracted data as:

- `yt_desc_YYYYMMDD-HHMMSS.csv`
- `yt_desc_YYYYMMDD-HHMMSS.json`

Example **CSV output:**
```
url,title,description
https://www.youtube.com/watch?v=abc123,Sample Video Title,Sample Video Description
```

Example **JSON output:**
```json
[
  {
    "url": "https://www.youtube.com/watch?v=abc123",
    "title": "Sample Video Title",
    "description": "Sample Video Description"
  }
]
```

---

## **Dependencies**
- `selenium`
- `argparse`
- `csv`
- `json`
- `datetime`

To install dependencies:
```sh
pip install selenium
```

---

## **Notes**
⚠ **Ensure that Chrome WebDriver is installed** and is compatible with your Chrome browser.  
⚠ **YouTube may block excessive requests**—use delays if scraping a large number of videos.  

---

## **License**
MIT License © 2025 Your Name

---

Let me know if you want modifications! 🚀