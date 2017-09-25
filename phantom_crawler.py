# from selenium import webdriver
# driver = webdriver.PhantomJS()
# driver.set_window_size(1120, 550)
# driver.get("https://duckduckgo.com/")
# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
# print driver.current_url
# driver.quit()


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import re
import csv

driver = webdriver.PhantomJS()

driver1 = webdriver.PhantomJS()


class GetOutOfLoop( Exception ):
    pass
# ("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=14&sortProperty=BestRating&DESC=True","E-Marketing"),


urllist=[("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=23&sortProperty=BestRating&DESC=True","Kitchen and Bakery"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=24&sortProperty=BestRating&DESC=True","Electronic Solutions"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=25&sortProperty=BestRating&DESC=True","Academy Services"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=16&sortProperty=BestRating&DESC=True","take photo"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=26&sortProperty=BestRating&DESC=True","Accessories women"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=34&sortProperty=BestRating&DESC=True","design and print"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=35&sortProperty=BestRating&DESC=True","Planning events and concerts"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=41&sortProperty=BestRating&DESC=True","Electronics and Accessories"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=47&sortProperty=BestRating&DESC=True","Cars"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=48&sortProperty=BestRating&DESC=True","Real estate"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=49&sortProperty=BestRating&DESC=True","Furniture and Decoration"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=51&sortProperty=BestRating&DESC=True","Crafts and handicrafts"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=39&sortProperty=BestRating&DESC=True","Stylist and beauty"),
("https://maroof.sa/BusinessType/BusinessesByTypeList?bid=45&sortProperty=BestRating&DESC=True","Other")]

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
   
    # driver.get('https://maroof.sa/BusinessType/BusinessesByTypeList?bid=23&sortProperty=BestRating&DESC=True')
    # driver.set_page_load_timeout(30)

    driver.get(catUrl)
    html = driver.page_source
    # print "html",html
    button = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
    # print(button)
    soup = BeautifulSoup(html)
    urllist=[]
    tags=[]
    # print "soup",soup
    while(True):
        i+=1
        # print "inside loop",i
        try:
            # tags = soup.find_all("a", class_="tab-pro-container")
            
            # links = browser.find_elements_by_partial_link_text('##')

            wait = WebDriverWait(driver, 10)
            tags = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='tab-pro-container']")))
            print "urlcount", len(tags)

            # button[0] = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//button[@class='btn btn-primary']")))
            
            button = driver.find_element_by_xpath("//button[@class='btn btn-primary']")


            button.click()
            print "button clicked", i
            
            # if i == 500:
            #     for link in tags:
            #         print "link.href", link.get_attribute("href")
            #         url=link.get_attribute("href")
            #         urllist.append(url)

            #     # driver.close()

            #     return urllist  
                # raise GetOutOfLoop

        except:
            print "no more button"
            for link in tags:
                # print "link.href", link.get_attribute("href")
                url=link.get_attribute("href")
                urllist.append(url)
            # driver.close()
            return urllist 

def getStoreUrlDetails(url,category):
    storedet=[]

    # driver1.set_page_load_timeout(10)
    storedet.append(category)
    driver1.get(url)
    print "url get done"
    html1 = driver1.page_source
    # print "html",html1
    soup1 = BeautifulSoup(html1)
    # storename=soup1.find_element_by_xpath("//h3[@class='media-heading text-primary']")

    # List<WebElement> list = driver.findElements(By.xpath(".//*[@class='media-heading text-primary']//h2/a"));

# /h3/span/font
# /h3/font
    # elem=soup1.findNext('p',{'style':'margin-bottom:0px;'}).findNext('font').findAll('font') 
    # print "category elem",elem

    elemlist = soup1.find_all('h3',class_="media-heading text-primary")
    # print "elemlist length",len(elemlist)
    for el in elemlist:
        try:
            # print "element",el.text[0]
            if(el.text!="" and el.text not in storedet):
                storedet.append(el.text)
        except:
            continue
    storename,tagline,category=["","",""]
    # tagline=soup1.find_element_by_xpath("//div[@class='media-body']/h3/font")
    # category=soup1.find_element_by_xpath("//div[@class='media-body']/p/font")
    # ratingelem=driver1.find_element_by_xpath("//span[@class='rating-num']/font")  
    ratingelem=soup1.find_all("span",class_="rating-num")
    # print "ratingelem",ratingelem

    for el in ratingelem:
        try:
            # print "span elem",el.text
            if(el.text!="" and el.text not in storedet):
                storedet.append(el.text)
        except:
            continue

    phoneno=soup1.findAll('a', href=re.compile("tel"))
    # print "pohoneno",phoneno

    for el in phoneno:
        try:
            # print "a elem",el.string
            if(el.string!="" and el.string not in storedet):
                storedet.append(el.string)
        except:
            continue

    email=soup1.findAll('a', href=re.compile("mail"))
    # print "email",email
    for el in email:
        try:
            # print "a email elem",el.contents
            if(el.string!="" and el.string not in storedet):
                storedet.append(el.string)
        except:
            continue
    storedet.append(url)
    print "storedetails fetched"
    return storedet
    # driver1.close()


if __name__ == "__main__":
    print "urlist",urllist
    i=0
    for cat in urllist :
        urls= getCategoryUrls(cat[0])
        print "returned urls",urls
        arr = [str(r) for r in urls]
        # print "str urls",arr
        i=i+1
        filename='category_'+cat[1]+'.csv'

        outcsv= open(filename, 'wb')
        writer = csv.writer(outcsv)
        # writer.writerow(["Date", "temperature 1", "Temperature 2"])
        for l in arr:
            details=getStoreUrlDetails(l,cat[1])
            # print "storedetails", details
            temparr = [r.encode('utf-8').strip() for r in details]

            writer.writerow(temparr )
        outcsv.close()
        print "category finished",cat[1]
        # break


    # details=getStoreUrlDetails("https://maroof.sa/15709","category")
    # print "storedetails", details


#  [starts-with(@id, 'foo') 

# <div class="media-body"
# span class="rating-num"
# <font><font>
# <h3 class="media-heading text-primary">
# <span><font>Storename

# a href="tel:0564810503"
# a href="mailto:yummyfoods90@gmail.com"