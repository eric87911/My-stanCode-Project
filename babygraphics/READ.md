# 👶 Baby Names Visualizer  
這是一份使用 Python 製作的嬰兒名字排名視覺化工具。  
This is a Python project for visualizing historical baby name rankings in the United States.

---

## 📚 專案簡介 / Project Overview  
本專案讀取由美國社會安全署提供的嬰兒姓名資料，並支援搜尋與視覺化功能：  
- 以折線圖呈現某些名字在各年份的受歡迎程度（排名）  
- 提供子字串搜尋功能，找出所有包含該字串的姓名  

This project reads baby name data files and supports two main features:
- Line chart visualization of name popularity across years  
- Substring search for finding all matching names  

---

## 🗂️ 檔案說明 / File Descriptions

### `babynames.py` （我撰寫的程式）
A supporting module for reading and organizing baby name ranking data.
It parses multiple text files and structures name–year–rank info into a dictionary.  
資料讀取與查詢邏輯  
- 讀取多個檔案並整理出姓名的年度排名  
- 支援搜尋功能，找出包含特定字串的名字  

**Main functions:**
- `add_data_for_name(data, year, rank, name)`
- `read_files(filenames)`
- `search_names(data, target)`
- `print_names(data)`
- `main()` – 可從 command line 操作

---

### `babygraphics.py` （我撰寫的程式）  
The main script that draws baby name ranking trend lines on a tkinter canvas. 
It calculates coordinates, plots the background grid, draws name trends, and connects with `babygraphicsgui.py`.  
視覺化模組  
- 使用 tkinter 畫布呈現折線圖  
- 每個名字一條線，不同顏色區分  
- 如果某年未進入前1000名，顯示星號 `*`  

**Main functions:**
- `get_x_coordinate(width, year_index)`
- `draw_fixed_lines(canvas)`
- `draw_names(canvas, name_data, lookup_names)`
- `main()` – 可測試畫圖功能

---

### `babygraphicsgui.py` （老師提供）  
Provided by the instructor. This is the GUI interface module that sets up buttons, 
canvas, input fields, and calls drawing functions from `babygraphics.py`.  
GUI 互動模組（未修改）  
- 提供輸入介面  
- 呼叫我撰寫的函式進行畫圖與搜尋  
- 負責錯誤訊息與互動邏輯

---

## 🔧 Usage / 使用方式  

1. Prepare the baby name data files in `.txt` format, structured as specified.  
   準備好嬰兒姓名的 `.txt` 格式資料，依指定格式存放。  
2. Run the program using Python 3.  
   使用 Python 3 執行主程式。  
3. Enter names in the GUI to visualize ranking trends.  
   在 GUI 輸入姓名後，即可視覺化顯示排名變化趨勢圖。

---

## 📌 範例畫面 / Example


<img width="1352" height="882" alt="螢幕擷取畫面 2025-10-03 145635" src="https://github.com/user-attachments/assets/cde27fc3-6bf6-4696-b802-1131aa061edb" />



---

## 📌 Notes / 備註

- `babygraphicsgui.py` was provided by the course instructor.  
  本專案 `babygraphicsgui.py` 是由課程老師提供的檔案。  
- The rest of the code was written as part of the SC101 assignment.  
  其餘程式碼皆為 SC101 作業練習的一部分。   

