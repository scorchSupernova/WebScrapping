from bs4 import BeautifulSoup as bs  ## HTML-Structure
from urllib.request import urlopen as url  ##web-client

##Url for scrapping from this page/link
page="https://www.newegg.com/p/pl?d=GTX&N=-1&IsNodeId=1&bop=And&Page=1&PageSize=36&order=BESTMATCH"

##opening the connection and downloads html page 
client=url(page)

##parses html into a bs4 data structure
page_bs= bs(client.read(),"html.parser")
client.close()

##For finding each things from the page/link using regex
contains=page_bs.findAll("div",{"class":"item-container"})


##Name of the output file we want to store in

file_name="store.csv"

##All headers of the csv file
head="Brand,Product_Name,Shipping\n"

##For opening file and writing header's names
ff=open(file_name,'w')
ff.write(head)

##for grabing attributes of each product using for loop
for contain in contains:
    ##Find all anchor tags from first div
    val=contain.div.select('a')
    
    ##For grabbing the titles/brand from the image title attributes and doing proper casting using .title()
    brand=val[0].img['title'].title()
    
    ##for grabbing the product_name from the second anchor tag for html structure
    product_name=contain.div.select('a')[2].text
    
    
    ##for finding the price of shipping from list-class "price-shipping"
    ship=contain.findAll("li",{"class":"price-ship"})[0].text.strip().replace("$","").replace(" Shipping","")
   # print(product_name+"\n")
    if ship=="Free" or ship=="Special":
       ship="0"
    ff.write(brand+", "+product_name.replace(",","|")+", "+ship+"\n")

ff.close()
    
