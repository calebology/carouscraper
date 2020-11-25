import re
import requests
from bs4 import BeautifulSoup as bs
import csv
from os.path import basename

my_url = "https://www.carousell.sg/search/guitar?"

resp = requests.get(my_url)

# HTML Parsing
my_soup = bs(resp.content, "html.parser")

# Grabbing each listing
containers = my_soup.findAll("div", {"class": "An6bc8d5sQ _9IlksbU0Mo _2t71A7rHgH"})

# Image downloading with basename
for x in range(len(containers)):
    img_links = containers[x].find_all("img")
    for img in img_links:
        image_src = img["src"]
        with open(basename(image_src), "wb") as f:
            f.write(requests.get(image_src).content)
        # urllib.request.urlretrieve(image_src, str(number))
        # number += 1




'''
## Testing on a single carousell listing

# Scraping description from a single instance
single = containers[0]
desc_result = single.findAll(
    "p",
    attrs={
        "class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv"
    },
)
for desc in desc_result:
    print(desc.text)


# Scraping price from a single instance
price_result = single.find_all("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6"})
for price in price_result:
    print(price.text)

'''

# Iterating through the whole page and finding descriptions, prices and urls
# csv_file = open("carousell_scrape.csv", "w", encoding = "UTF-8")

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["Description", "Price", "URL"])

# for x in range(len(containers)):
#     descs = containers[x].find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv"}).text
#     print(descs)
#     prices = containers[x].find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6"}).text
#     print(prices)
#     links = [a["href"] for a in containers[x].find_all("a",href=True) if a.text]
#     urls = "carousell.sg" + links[1]
#     print(urls)
#     csv_writer.writerow([descs, prices, urls])

# csv_file.close()

'''
## To Do List

# Scrape the pictures
# Add in time function
# Find some way for the info to be compiled onto the csv iteratively
# Integrate a sorting algorithm

'''

