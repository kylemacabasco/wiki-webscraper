from bs4 import BeautifulSoup
import requests
import string

# open the state.txt file and reads the state
f = open('state.txt', 'r')
enter_input = f.readline()
ui = string.capwords(str(enter_input))
lists = ui.split()
word = "_".join(lists)

# clear the state info file
g = open('state_info.txt', 'w')
g.close()

# this will get the link for the informatikon
url = "https://en.wikipedia.org/wiki/" + word

def wikiscraper(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    details = soup('table', {'class': 'infobox'})
    for i in details:                  # get all the "tr in the infobox"
        info = i.find_all('tr')
        for j in info:
            heading = j.find_all('th')  # get the first keyword
            detail = j.find_all('td')   # get the second keyword that relates to the first
            if heading is not None and detail is not None:
                for x, y in zip(heading, detail):
                    with open('state_info.txt','a+') as file_object:       # writes it into the state info file
                        file_object.seek(0)
                        data = file_object.read(100)
                        if len(data) > 0:
                            file_object.write("\n")
                        file_object.write("{}: {}".format(x.text, y.text))


wikiscraper(url)