from bs4 import BeautifulSoup
import re
import urllib
import urlparse
import requests

url = "http://thegradcafe.com/survey/index.php?q=stanford+management+science&t=a&pp=250&o=d&p="
start_url = "http://thegradcafe.com/survey/index.php?q=stanford+management+science&t=a&o=&p=1"
#don't want to visit any page twice

urls = [start_url] # BFS queue
visited = [start_url] #visited urls

while len(urls)> 0 :
    try:
        #url [0] for FIFO ordering
        htmltext = urllib.urlopen(urls[0]).read()
        #print htmltext
        regex = "<td class=\"instcol\">(.+?)\W*GRE Subject</strong>"

        pattern = re.compile(regex)
        entry = re.findall(pattern, htmltext)

        for i in entry:
            i= i.replace("<td>", " ")
            i= i.replace("</td>", " ")
            i= i.replace("<span class=\"dAccepted\">", "\n")
            i= i.replace("<span class=\"dRejected\">", "\n")
            i= i.replace("</span>", " ")
            i= i.replace("<a class=\"extinfo\" href=\"#\"><span><strong>Under", "")
            i= i.replace("<br/><strong>", "\n")
            i= i.replace("</strong>", "")
            i= i.replace("<br/><strong", "")
            print i
            print "\n"

    except:
        continue


    soup = BeautifulSoup(htmltext)
    urls.pop(0)
    # print len(urls)
    # print urls


    for link in soup.find_all('a', href=True):
        link['href'] = urlparse.urljoin(url, link['href'])
        if url in link['href'] and link['href'] not in visited:
            urls.append(link['href'])
            visited.append(link['href'])

