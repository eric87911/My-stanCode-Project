## 👶 Baby Names Web Crawler 爬蟲分析專案

  This project is my first hands-on practice in web crawling and data analysis using Python + Selenium + BeautifulSoup.
  這是我第一次使用 Python、Selenium 與 BeautifulSoup 進行的爬蟲資料分析練習，目標是從美國社會安全局 (SSA) 提供的「嬰兒名字統計資料」網站擷取資料並進行數據整理。

---

## 📌 Project Overview 專案簡介

  資料來源 / data source：
  
  https://www.ssa.gov/oact/babynames/decades/names2010s.html
  
  https://www.ssa.gov/oact/babynames/decades/names2000s.html
  
  https://www.ssa.gov/oact/babynames/decades/names1990s.html

---

## 📌 程式流程 Program Flow

  使用 Selenium WebDriver 打開網頁並等待載入完成
  Use Selenium WebDriver to open the webpage and wait until it is fully loaded.
  
  以 BeautifulSoup 解析 HTML 表格內容
  Parse the HTML table data using BeautifulSoup.
  
  擷取 Top 200 男性與女性名字的數量資料
  Extract the counts of Top 200 male and female names.
  
  將統計結果輸出到 Console
  Print the calculated results to the console.

---

## 🛠️ Technologies 使用技術

  Python 3.x
  
  Selenium – 網頁自動化與動態內容抓取
  
  BeautifulSoup4 – HTML 資料解析
  
  Chrome WebDriver – 瀏覽器驅動

---

## 🚀 How to Run 執行方式

  安裝相依套件
  
  pip install selenium beautifulsoup4
  
  
  確認已安裝 Chrome WebDriver 並將其加入 PATH
  
  執行程式
  
  python webcrawler.py

---

## Console 輸出結果 (Example Output 範例輸出)：

  ---------------------------
  2010s
  Male Number: 12345678
  female_number: 11223344
  ---------------------------
  2000s
  Male Number: ...
  female_number: ...
  ---------------------------
  1990s
  Male Number: ...
  female_number: ...

---

## ✨ Learning Outcomes 學習收穫

  學會使用 Selenium + BeautifulSoup 抓取動態網站資料
  Learned how to use Selenium + BeautifulSoup to crawl dynamic website data.
  
  練習 HTML Table 解析與數據清理
  Practiced HTML table parsing and data cleaning.
  
  體驗到資料擷取、整理與轉換成可分析數據的流程
  Experienced the workflow of data extraction, organization, and transformation into analyzable format.
  
  作為進一步資料分析、視覺化專案的基礎
  Built a foundation for future projects in data analysis and visualization.
