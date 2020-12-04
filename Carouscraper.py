import re
import requests
from bs4 import BeautifulSoup as bs
import csv
from os.path import basename
import os
import time
import glob
import xlsxwriter
import pandas as pd

# Creating lists for easy indexing
desc_list = []
price_list = []
url_list = []
pic_list = []

my_url = "https://www.carousell.sg/search/guitar?"
resp = requests.get(my_url)

# HTML Parsing
my_soup = bs(resp.content, "html.parser")

# Grabbing each listing
containers = my_soup.findAll("div", {"class": "An6bc8d5sQ _9IlksbU0Mo _2t71A7rHgH"})

# Function for scraping descriptions
def get_descs(inp):
    descs = inp.find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv"}).text
    return descs

# Function for scraping prices
def get_prices(inp):
    prices = inp.find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6"}).text
    return prices


# Function for scraping URLs
def get_urls(inp):
    links = [a["href"] for a in inp.find_all("a",href=True) if a.text]
    urls = "carousell.sg" + links[1]
    return urls 

# Function for scraping images
def get_imgs(inp):
    img_links = inp.find_all("img")
    for img in img_links:
        image_src = img["src"]
        with open(basename(image_src), "wb") as f:
            picture = f.write(requests.get(image_src).content)
            pic_list.append(basename(image_src))
    return picture

############################################################################################################################

# Creating Excel File #
workbook = xlsxwriter.Workbook(os.path.join(os.path.dirname(os.path.abspath(__file__)), "scraped_data.xlsx"))
worksheet = workbook.add_worksheet()
# Writing headers
worksheet.write("A1", "Description")
worksheet.write("B1", "Price")
worksheet.write("C1", "URL")
worksheet.write("D1", "Image")

# Scraping relevant parameters with a for loop
for x in range(len(containers)): 
    descs = get_descs(containers[x])
    desc_list.append(descs)
    prices = get_prices(containers[x])
    price_list.append(prices)
    urls = get_urls(containers[x])
    url_list.append(urls)
    pics = get_imgs(containers[x])

    # Writing descriptions
    worksheet.write(x+1, 0, descs)
    # Writing prices
    worksheet.write(x+1, 1, prices)
    # Writing URLs
    worksheet.write(x+1, 2, urls)
    # Writing images
    # worksheet.write(x+1, 3, pics)

workbook.close()

# for x in range(len(containers)):
#     str(desc_list[x])
#     str(price_list[x])
#     str(url_list[x])
#     str(pic_list[x])
#     print(desc_list[x].encode("utf-8"))
#     print(price_list[x].encode("utf-8"))
#     print(url_list[x].encode("utf-8"))
#     print(pic_list[x].encode("utf-8"))


# List comprehension
desc_list = [x.encode("utf-8") for x in desc_list]
price_list = [x.encode("utf-8") for x in price_list]
url_list = [x.encode("utf-8") for x in url_list]
pic_list = [x.encode("utf-8") for x in pic_list]


# Creating pandas dataframe
data = [desc_list, price_list, url_list]
# scraped_df = pd.DataFrame(desc_list, price_list, url_list)
scraped_df = pd.DataFrame(data)
# scraped_df.columns = ["Description", "Price", "URL"]
print(scraped_df)



# Building script to open desired jpg file



####################################   DEPRECATED VERSION   ###################################################################################################################

# Creating csv file to store scraped content
# csv_file = open("carousell_scrape.csv", "w", encoding = "UTF-8")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["Description", "Price", "URL"])

# for x in range(len(containers)):
#     descs = containers[x].find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv"}).text
#     print(descs.encode("utf-8"))
    # # Scraping descriptions 
    # descs = containers[x].find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv"}).text
    # print(descs)
    # # Scraping prices
    # prices = containers[x].find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6"}).text
    # print(prices)
    # # Scraping links to the carousell listing
    # links = [a["href"] for a in containers[x].find_all("a",href=True) if a.text]
    # urls = "carousell.sg" + links[1]
    # print(urls)

    # # Scraping (downloading) images
    # img_links = containers[x].find_all("img")
    # for img in img_links:
    #     image_src = img["src"]
    #     with open(basename(image_src), "wb") as f:
    #         pic = f.write(requests.get(image_src).content)
    # csv_writer.writerow([descs, prices, urls])
# csv_file.close()


# Building the while loop to compile the data with
# while True:
#     time.sleep(5)
#     my_url = "https://www.carousell.sg/search/guitar?"
#     resp = requests.get(my_url)
#     # HTML Parsing
#     my_soup = bs(resp.content, "html.parser")
#     # Grabbing each listing
#     containers = my_soup.findAll("div", {"class": "An6bc8d5sQ _9IlksbU0Mo _2t71A7rHgH"})

#     if glob.glob("*.csv"):
#         # Write onto the existing CSV file

#     else:
#         # Create the csv
#         # csv_file = open("carousell_scrape.csv", "w", encoding = "UTF-8")
#         # csv_writer = csv.writer(csv_file)
#         # csv_writer.writerow(["Description", "Price", "URL"])
        
    


'''
## To Do List

# Scrape the pictures (done)

# Add in time function (done)

# Try to use an excel writer instead of csv writer !!!

# Find some way for the info to be compiled onto the csv iteratively (while loop)?
## Add in a condition, if there's no file in directory, create one. If there is, compile on top of it.


# Figure out how to use the pictures that are downloaded
    # They can't be inserted into CSV... find another file format???
# Integrate a sorting algorithm; check whether it's actually a guitar
    # Image processing ML? lol....

# Conclude the project after I figure out how to present the images together with the other content 
'''

