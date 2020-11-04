This project is on stage 5 where we are able to extract complete information of given url, along with this if some tag or keyword is provided
then also it works.
Along with this dumping a image inside a folder functionality being added. 
Usage:

1. py app.py
2. open any REST client.
3. http://localhost:5000/scrap
4. {
  "url":"https://www.google.com/",
   "keywords":[],
  "tags":[]
}
5. The scraper will return information scraped in form of json.
