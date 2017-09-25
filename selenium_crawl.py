from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import re
import csv

driver = webdriver.Firefox()

driver1 = webdriver.Firefox()


class GetOutOfLoop( Exception ):
    pass

urllist=["https://maroof.sa/BusinessType/BusinessesByTypeList?bid=23&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=14&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=24&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=25&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=16&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=26&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=34&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=35&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=41&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=47&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=48&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=49&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=51&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=39&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=45&sortProperty=BestRating&DESC=True"]

# check out the docs for the kinds of things you can do with 'find_all'
# this (untested) snippet should find tags with a specific class ID
# see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
# for tag in soup.find_all("a", class_="tab-pro-container"):
#     print tag


# button = driver.find_elements_by_class_name("btn btn-primary")
# button = driver.  ("btn btn-primary")[0]

def getCategoryUrls(catUrl):

    # driver.get(catUrl)

    # html = driver.page_source
    # # print "html",html
    # # soup = BeautifulSoup(html)
    # button = driver.find_element_by_xpath("//button[@class='btn btn-primary']");
    site_url="https://maroof.sa"
    i=0
    while(True):
        # driver.get('https://maroof.sa/BusinessType/BusinessesByTypeList?bid=23&sortProperty=BestRating&DESC=True')
        # driver.set_page_load_timeout(30)

        driver.get(catUrl)
        html = driver.page_source
        # print "html",html
        button = driver.find_element_by_xpath("//button[@class='btn btn-primary']");
        # print(button)
        soup = BeautifulSoup(html)
        # print "soup",soup
        i+=1
        try:
            button.click()
            print "button clicked", i

            # tags = soup.find_all("a", class_="tab-pro-container")
            
            # links = browser.find_elements_by_partial_link_text('##')

            wait = WebDriverWait(driver, 10)
            tags = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='tab-pro-container']")))
            urllist=[]
            print "urlcount", len(tags)
            for link in tags:
                print "link.href", link.get_attribute("href")
                url=link.get_attribute("href")
                urllist.append(url)
            
            if i == 1:
                # driver.close()
                return urllist  
                # raise GetOutOfLoop

        except GetOutOfLoop:
            print "no more button"


def getStoreUrlDetails(url):
    storedet=[]

    # driver1.set_page_load_timeout(10)

    driver1.get(url)
    print "url get done"
    html1 = driver1.page_source
    # print "html",html1
    soup1 = BeautifulSoup(html1)
    # storename=soup1.find_element_by_xpath("//h3[@class='media-heading text-primary']")

    # List<WebElement> list = driver.findElements(By.xpath(".//*[@class='media-heading text-primary']//h2/a"));

# /h3/span/font
# /h3/font
    elemlist = soup1.find_all('h3',class_="media-heading text-primary")
    print "elemlist length",len(elemlist)
    for el in elemlist:
        try:
            print "element",el.text
            if(el.text!="" and el.text not in storedet):
                storedet.append(el.text)
        except:
            continue
    storename,tagline,category=["","",""]
    # tagline=soup1.find_element_by_xpath("//div[@class='media-body']/h3/font")
    # category=soup1.find_element_by_xpath("//div[@class='media-body']/p/font")
    # ratingelem=driver1.find_element_by_xpath("//span[@class='rating-num']/font")  
    ratingelem=soup1.find_all("span",class_="rating-num")
    print "ratingelem",ratingelem

    for el in ratingelem:
        try:
            print "span elem",el.text
            if(el.text!="" and el.text not in storedet):
                storedet.append(el.text)
        except:
            continue

    phoneno=soup1.findAll('a', href=re.compile("tel"))
    print "pohoneno",phoneno

    for el in phoneno:
        try:
            print "a elem",el.string
            if(el.string!="" and el.string not in storedet):
                storedet.append(el.string)
        except:
            continue

    email=soup1.findAll('a', href=re.compile("mail"))
    print "email",email
    for el in email:
        try:
            print "a email elem",el.contents
            if(el.string!="" and el.string not in storedet):
                storedet.append(el.string)
        except:
            continue
    return storedet
    # driver1.close()


if __name__ == "__main__":
    print "urlist",urllist
    i=0
    for cat in urllist :
        urls= getCategoryUrls(cat)
        print "returned urls",urls
        arr = [str(r) for r in urls]
        print "str urls",arr
        i=i+1
        filename='category'+str(i)+'.csv'

        outcsv= open(filename, 'wb')
        writer = csv.writer(outcsv)
        # writer.writerow(["Date", "temperature 1", "Temperature 2"])
        for l in arr:
            details=getStoreUrlDetails(l)
            print "storedetails", details
            temparr = [r.encode('utf-8').strip() for r in details]

            writer.writerow(temparr )
        outcsv.close()
        break

#  [starts-with(@id, 'foo') 

# <div class="media-body"
# span class="rating-num"
# <font><font>
# <h3 class="media-heading text-primary">
# <span><font>Storename

# a href="tel:0564810503"
# a href="mailto:yummyfoods90@gmail.com"