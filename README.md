This project is on stage 6 where we are able to extract complete information of given url, along with this if some tag or keyword is provided
then also it works.
Along with this dumping of images inside a folder functionality being added. 

Note:Code is inside master branch thanks for visiting...

Usage:
For URL functionality(functionality number one):-
1. py app.py
2. open any REST client.
3. http://localhost:5000/scrap
4. for URL feature:-
4. {
  "url":"https://www.flipkart.com",
   "keywords":[],
  "tags":[]
}
5. The scraper will return information scraped in form of json.


For URL+Keywords functionality(functionality number two):-
1. py app.py
2. open any REST client.
3. http://localhost:5000/scrap
4. for URL feature:-
4. {
  "url":"https://www.flipkart.com",
   "keywords":["sports shoes"],
  "tags":[]
}
5. The scraper will return information scraped in form of json.

For URL+Tags functionality(functionality number three):-
1. py app.py
2. open any REST client.
3. http://localhost:5000/scrap
4. for URL feature:-
4. {
  "url":"https://www.flipkart.com",
   "keywords":[],
  "tags":["p","a"]
}
5. The scraper will return information scraped in form of json.

For Keywords functionality(functionality number four):-
1. py app.py
2. open any REST client.
3. http://localhost:5000/scrap
4. for URL feature:-
4. {
  "url":"",
   "keywords":["best mobile in range 10000"],
  "tags":[]
}
5. The scraper will return information scraped in form of json.
