from requests import get
from bs4 import BeautifulSoup

# Lists to store scraped web data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# URL from which we will extract HTML file

release_date = raw_input('Enter a Year: ')
if release_date.isdigit() is False:
  print "Please try again and correctly enter a year."
  exit()

if release_date <= 1830 or release_date <= 2018:
  print "Enter a year from 1881 to 2018!"
  exit()


url1 = 'http://www.imdb.com/search/title?release_date='
url2 = '&sort=num_votes,desc&page=1'

url = url1 + release_date + url2
response = get(url)

# Parsing the HTML file that was acquired from the URL
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

# Data that will be extracted about the movies from the parsed HTML file
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')


# Extract data from individual movie container
for container in movie_containers:
  
  if container.find('div', class_ = 'ratings-metascore') is not None:
                    print "-------------------------"
                    # Store the name
                    name = container.h3.a.text
                    names.append(name)
                    print "Name: " + name
                    
                    # Store the year
                    year = container.h3.find('span', class_ = 'lister-item-year').text
                    years.append(year)
                    print "Year: " + year
                    
                    # Store the IMDB rating
                    imdb = float(container.strong.text)
                    imdb_ratings.append(imdb)
                    print "IMDB_RATING: " + str(imdb)
                    
                    # Store the Metascore
                    m_score = container.find('span', class_ = 'metascore').text
                    metascores.append(m_score)
                    print "Metascore: " + m_score
                    
                    # Store the number of votes
                    vote = container.find('span', attrs = {'name':'nv'})['data-value']
                    votes.append(int(vote))
                    print "Number of Votes: " + vote

