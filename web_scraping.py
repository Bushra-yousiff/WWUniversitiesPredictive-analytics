from selenium import webdriver
import pandas as pd
import time
import pickle

driver = webdriver.Chrome('/Users/lailaalmajnuni/downloads/chromedriver')
#did it from 2019 and 2020
url = 'https://www.topuniversities.com/university-rankings/world-university-rankings/2019'
driver.get(url)

driver.maximize_window()
time.sleep(10)

driver.find_element_by_link_text("Rankings indicators").click()
time.sleep(10)

#Do it only if you had to(eg. if your program crashes before reaching the last
#page needed and had to do scraping multiple times then set n=last page scraped)
'''
for i in range(n):
    driver.find_element_by_class_name("page-link.next").click()
    time.sleep(1)
'''

university_details_list = []


for i in range(n):  
    uni_det = driver.find_elements_by_class_name('td-wrap-in')
    for u in range(len(uni_det)):
        university_details_list.append(uni_det[u].text)
    
    driver.find_element_by_class_name("page-link.next").click()
    time.sleep(5)

#the university details were listed separately so every 8 elements is one instance
university_details_list = [university_details_list[i:i+8] for i in range(0, 
                            len(university_details_list), 8)]


df_university_details = pd.DataFrame(university_details_list)

#renaming columns of dataframs
df_university_details.rename(columns={0:'University',
                                      1:'Overall Score',
                                      2:'International Students Ratio',
                                      3:'International Faculty Ratio',
                                      4:'Faculty Student Ratio',
                                      5:'Citations per Faculty',
                                      6:'Academic Reputation', 
                                      7:'Employer Reputation'}, inplace=True)

df_university_details.to_pickle('2019website.pkl')