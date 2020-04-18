# importing Scraperwiki and lxml.html, useful for scraping
import scraperwiki
import lxml.html

# setting url to the url for our desired site to scrape (in this case, the NEWS event list for IAEA, with incidents/page = 100)
url = "https://www-news.iaea.org/EventList.aspx?ps=100&pno=0"

# Read in a page
html = scraperwiki.scrape(url)

# Find something on the page using css selectors
root = lxml.html.fromstring(html)
for row in root.cssselect("#tblEvents tr"):
  link_in_header = row.cssselect("h4 a").pop()
  event_title = link_in_header.text
  print(event_title)

# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
# 
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")
# 
# # You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
