from selenium import webdriver
import webbrowser
driver = webdriver.PhantomJS() #needed to add PhantomJS program into ~/.bashrc

"""
IT WORKSSS!!!! May want to refine it
What I want this to do:
Read the splash page of Cucumber Quest, see if there is a new page.

If new page, will open link to the page.

If no new page, then will yield a statement saying so!
"""

URL = "http://cucumber.gigidigi.com/"

driver.get(URL)

partial_txt = "Or read the most recent" #This may be the culprit of not getting the right URL text
#each update will change how the href text will say

recent_page_link = driver.find_elements_by_partial_link_text(partial_txt) #this is a list that holds the info for the URL, BUT not the actual URL
recent_page_link_URL = ""

for n in recent_page_link:
    recent_page_link_URL += n.get_attribute("href") #This translates the above into a URL

#--------------------------------------------------------------------------------------------------------------------------------------------------

#Experimenting with "clicking" a link, navigating to it, and then reading stuff.
#The may be a more refined way of doing this

driver.get(recent_page_link_URL) #Goes into new URL. Is there a better way? This seems to be the most obvious/easiest

#make a function. I am repeating myself here.

class_name_for_newest_page = 'post-details'
css_selector_for_newest_page = "a[rel~='bookmark']"

#Below gets "<a rel="bookmark" href="http://cucumber.gigidigi.com/cq/page-748/">" from the page
div_class = driver.find_element_by_class_name(class_name_for_newest_page)
URL_elem = div_class.find_elements_by_css_selector(css_selector_for_newest_page)
#See this: http://stackoverflow.com/questions/5608808/css-style-a-link-based-on-its-rel-attribute

newest_page_URL = ""

for n in URL_elem:
    newest_page_URL += n.get_attribute("href") #This translates the above into a URL

#--------------------------------------------------------------------------------------------------------------------------------------------------


with open('CucoQuest.txt', 'r') as f:
    content = f.readlines()
    content = ''.join(content)

if ((not content) or (content != newest_page_URL)): 
    with open('CucoQuest.txt', 'w') as f:
        f.write(newest_page_URL)
    content = newest_page_URL
    webbrowser.open(content)
else:
    print ("No new pages!")   

driver.close()
