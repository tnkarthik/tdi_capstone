import urllib2
import re
from bs4 import BeautifulSoup as bs

def abc_def():
    ## please import this.
    print "its really working"
    

def read_and_save_url(all_urls, folder_to_write):
    #all_urls = open("./data/verge_urls","r")
    ## Takes a list of urls and writes all data found in the url in the folder_to_write/url
    
    for url in all_urls:
        device = re.split("/",url)[-1]
        #device = re.findall("([^\s]+)",device)
        #print device
        print "Currently reading %s at %s" %(device, url)
        filename = device

        data = urllib2.urlopen(url).read()
        data_bs = bs(data, "lxml")
        review_data = data_bs
        fh = open(folder_to_write+"/"+filename, "w")
        fh.write(str(review_data))
        fh.close()
        #break
        

def get_all_urls_from_pages(base_url,suffix_list):
    ## Takes base url and suffix list and returns a list of all webpage links found
    all_urls = []
    base_url = base_url.rstrip("/")
    print base_url
    for suffix in suffix_list:
        url = base_url +'/'+ str(suffix)
        try:
            data = urllib2.urlopen(url).read()
        except:
            print "Can't open url:", url
            break
        data_bs = bs(data, "lxml")
        for line in data_bs.find_all('div', class_ = "body"):
            all_urls = all_urls +[ line.a["href"]]
            #print line.a["href"]
    return all_urls
    
#abc_def()


def read_body_from_url(url):
    #data = urllib2.urlopen(url).read()
    data = open(url)
    data_bs = bs(data,"lxml")
    #print data_bs
    data_list = data_bs.find_all("p")
    list_to_return = []
    for data in data_list:
        list_to_return = list_to_return + [data.get_text()]
    return list_to_return
    
    
    