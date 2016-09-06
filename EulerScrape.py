"""
Goal: Scrape Euler problems into a database

Selenium + PhantomJS on Windows is kind of slow.

TODO:
- Make a working protoype of getting ONE problem. Then extrapolate from there.
    - Read table of links
    - Get links' text for title
    - Access links
    - Scrape corresponding page's text, put in sql database
    - Go back to main link page //This right here? This is the main problem. Selenium doesn't have a graceful way of accessing link and going back
- Read database

Ideas to solve above problem:
    1) 
    - Store the links in a list or file
    - Loop through the entire list/file and click the links each iteration
    - Go back to main page to click stored link (see: http://stackoverflow.com/questions/27626783/python-selenium-browser-driver-back)
    - Also see: http://stackoverflow.com/questions/24775988/how-to-navigate-to-a-new-webpage-in-selenium
    2)
    - Scrape each link, store it into a list
    - Loop through list, and have the driver.get(new_URL) each iteration
    - And also scrape the words each iteration as well.
    - This seems to be the less elegant way/just uses the basics of driver.get() really

Some useful info:
(td class="id_column") contains the column number and underneath is the link to the problem


#driver.find_element_by_xpath("//a[contains(@href, 'problem')]").click() #works in clicking the link. Now what? 
Doesn't seem to be an elegant way of clicking the link, doing something, and going back
The easiest solution is the bluntest: store all links in advance (in a list), "driver.get(URL_link)" and do stuff in a loop

"""
#The below encoding needs to be UTF-8 to match the HTML
# -*- coding: utf-8 -*-
#sqlite3 can't store multiple values at a time. And there is no loop. (see: http://stackoverflow.com/questions/6172815/sqlite-alter-table-add-multiple-columns-in-a-single-statement)
#Maybe later, but for now will use txt
from selenium import webdriver

path = r"C:\Users\achu\Desktop\Misc\Phantomjs\bin\phantomjs.exe" #seems like this is the only way to get PhantomJS on Windows.
#need to do "executable_path = path" inside PhantomJS()
web_page = "https://projecteuler.net/archives"


#should this driver variable be global or in a function?
driver = webdriver.PhantomJS() #This works only if PhantomJS is on path (with linux, it is)

def save_prompt(driver, count, id_num, title, URL, web_page):   
    with open('Euler.txt', 'a') as f:
    #Need to append to have file contain all prompts
        driver.get(web_page)     
        f.write("%s. %s" % (id_num, title))        
        f.write("\n")    

        driver.get(URL)         

        f.write(driver.find_element_by_class_name("problem_content").text)
        f.write("\n")        
        f.write("---" * 30)        
        f.write('\n\n')

        if count == 1:
            print ("Please wait. Just getting started")
        elif count == 10:
            print ("About one quarter of the way")        
        elif count == 25:
            print ("About half way there")
        elif count == 35:
            print ("About three quarters of the way")
        elif count == 49:
            print ("Finished!")



"""
#NOTE. YOU NEED TO DO element**s** to find all the elements. Not a singular element (Under docs for Locating Elements)
for element in driver.find_elements_by_xpath("//a[contains(@href, 'problem')]"): #This is the href tag text
    print (element.text) #prints problems' titles from page 1
#Crap. I guess I have to know XPATH. I stole this from http://stackoverflow.com/questions/33887410/python-selenium-locate-elements-by-href
""" 

driver.get(web_page)
count = 1

content = driver.find_elements_by_xpath("//a[contains(@href, 'problem')]")
id_content = driver.find_elements_by_class_name('id_column')
#don't know why, but you have to store the elements, otherwise, it becomes stale!
id_num_list = []
titles_list = []
links_list = [] #seems like you do have to store the links, otherwise will get Stale Element Reference error
#Can't iterate off the "links = driver.find_element_by_xpath"


for id_n in id_content:
    id_num_list.append(id_n.text) 

for title in content:#driver.find_elements_by_xpath("//a[contains(@href, 'problem')]"): #This is searching the href tag text
    links_list.append(title.get_attribute('href')) #gets link URL's (problems 1-50)    
    titles_list.append(title.text)
      

id_num_list.pop(0)   


for id_num, URL, title in zip(id_num_list, links_list, titles_list):      
    save_prompt(driver, count, id_num, title, URL, web_page)
    count += 1

driver.close()
