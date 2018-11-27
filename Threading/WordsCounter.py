import requests
from bs4 import BeautifulSoup
import operator


#scrap website
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for post_text in soup.findAll('a', {'class ': 'index_singleListingTitles'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


#remove symbols from words
def clean_up_list(word_list):
    clean_word_list = []
    symbols = "!@#$%^&*()_+\"<>?,./:'[]-={}"
    for word in word_list:
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


#create a dictionary of words and their number of appearence
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('https://buckysroom.org/tops.php?type=text&period=this-month')