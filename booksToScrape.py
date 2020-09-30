url = "http://books.toscrape.com/"

# Change scrapeBook to scrapeBooks
    
def scrapeBooks(url,count=1,urlNum=1):
    bookInfo = requests.get(url)
    soup2 = BeautifulSoup(bookInfo.content)
    anotherSoup = soup2.findAll("li",attrs={"class", "col-xs-6 col-sm-4 col-md-3 col-lg-3"})        
    for i in range(len(anotherSoup)):
        with open ("Scraped.txt",'a') as f:
                f.write(str(count)+')'+ 'Title: '+  anotherSoup[i].h3.a['title']+'\n')
                f.write( 'Price:'+anotherSoup[i].find('p',attrs='price_color').text+'\n\n')
                
                
        print(count,')', 'Title: ',  anotherSoup[i].h3.a['title'])
        print('    Price:',anotherSoup[i].find('p',attrs='price_color').text)
        print()
        count+=1
    if(len(soup2.findAll('li',attrs={'class','next'}))==1):
        if urlNum>1:
            url="http://books.toscrape.com/catalogue/"+soup2.findAll('li',attrs={'class','next'})[0].a['href']
            print('---- URL Being Scraped ---- ')
            print(url)
            print('--------------------------')
            print()
            scrapeBooks(url,count,urlNum)
        else:
            url="http://books.toscrape.com/"+soup2.findAll('li',attrs={'class','next'})[0].a['href']
            print('---- URL Being Scraped ---- ')
            print(url)
            print('---------------------------')
            print()
            urlNum+=1
            scrapeBooks(url,count,urlNum)

        
           
scrapeBooks(url)


