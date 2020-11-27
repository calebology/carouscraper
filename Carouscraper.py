import re
import requests
from bs4 import BeautifulSoup as bs
import csv
from os.path import basename
import os
import time
import glob
import xlsxwriter


my_url = "https://www.carousell.sg/search/guitar?"
resp = requests.get(my_url)

# HTML Parsing
my_soup = bs(resp.content, "html.parser")

# Grabbing each listing
containers = my_soup.findAll("div", {"class": "An6bc8d5sQ _9IlksbU0Mo _2t71A7rHgH"})

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



# Function for scraping descriptions
def get_descs(inp):
    descs = inp.find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv"}).text
    return print(descs)

# Function for scraping prices
def get_prices(inp):
    prices = inp.find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6"}).text
    return print(prices)


# Function for scraping URLs
def get_urls(inp):
    links = [a["href"] for a in inp.find_all("a",href=True) if a.text]
    urls = "carousell.sg" + links[1]
    return print(urls)

# Function for scraping images
def get_imgs(inp):
    img_links = inp.find_all("img")
    for img in img_links:
        image_src = img["src"]
        with open(basename(image_src), "wb") as f:
            picture = f.write(requests.get(image_src).content)
    return picture

# Creating Excel File
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
    prices = get_prices(containers[x])
    urls = get_urls(containers[x])
    pics = get_imgs(containers[x])
    for item in range(len(containers)):
        # Writing descriptions
        worksheet.write(item+1, 0, descs)
        # Writing prices
        worksheet.write(item+1, 1, prices)
        # Writing URLs
        worksheet.write(item+1, 2, urls)
        # Writing images
        # worksheet.write(item+1, 3, pics)
        # Struggling to call the images

workbook.close()

# Creating csv file to store scraped content
# csv_file = open("carousell_scrape.csv", "w", encoding = "UTF-8")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["Description", "Price", "URL"])

    # # Scraping descriptions 
    # descs = containers[x].find("p", attrs = {"class": "_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv"}).text
    # print(descs)
    # descs = get_descs(containers[x])
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
    # CSV's can't store images, lol....
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
