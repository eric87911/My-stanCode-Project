"""
File: webcrawler.py
Name: Eric
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()

        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')
        try:
            element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        male_num = 0
        woman_num = 0
        for tag in tags:
            info = tag.find_all('td')
            new_info = info[1:len(info)-2]
            for i in range(200):
                man_amount = new_info[i*5 + 2].text
                woman_amount = new_info[i*5 + 4].text
                man = ''
                woman = ''
                for w in man_amount:
                    if w.isdigit():
                        man += w
                for w in woman_amount:
                    if w.isdigit():
                        woman += w
                male_num += int(man)
                woman_num += int(woman)
            print(f'Male Number: {male_num}')
            print(f'female_number: {woman_num}')



        driver.quit()


if __name__ == '__main__':
    main()
