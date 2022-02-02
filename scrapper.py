from bs4 import BeautifulSoup
import os
import requests

print("""
_________________
WebScrapper Tool/
made by D3VR4J|‾
‾‾‾‾‾‾‾‾‾‾‾‾‾‾
(FOR COLLEGE PROJECT)
""")

run = True

while run:

    print("___________________________________________________")
    select = int(input("Select Your Web Scrapper(1or2)\n1. Keyword WebScrapper\n2. Latest News Scrapper: "))


    if select == 1:

        #Keyword Search(SiteUsed: https://www.bing.com/)

        search1 = input("Enter Your Keyword: ")
        params = {"q" : search1}
        r = requests.get("https://www.bing.com/search/", params=params)

        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find("ol", {"id":"b_results"})
        links = results.findAll("li", {"class":"b_algo"})
        for item in links:

            
            item_text = item.find("a").text
            item_href = item.find("a").attrs["href"]
            

            if item_text and item_href:
                print("Tittle: ", item_text)
                print("Summary: ", item.find("a").parent.parent.find("p").text)
                print("Link: ", item_href)
                print("___________________________________________________")

    elif select == 2:

        #LatestNewsArticle(SiteUsed: https://indiancybertroops.org)

        r = requests.get("https://indiancybertroops.org/news/current-affairs/") #if any params=params

        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.findAll("div", {"class": "twp-archive-content"})


        for item in links:

            item_href = item.find("a").attrs["href"]
            desc_text = item.find("p").text
            item_text = item.find("a").text


            print("Title: ", item_text, "\nArtile: ", desc_text, "\nArticle link:", item_href)
            print("___________________________________________________")

    else:
        print("ERROR: Wrong Input or Network Error")