import os
import csv
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def scrape(url):
    content = requests.get(url)
    return BeautifulSoup(content.text, 'html.parser')

def dict_of_all_presidents():#maps dict of list of presidents to id_number
    all_presidents_url = 'https://www.presidency.ucsb.edu/presidents'
    soup = scrape(all_presidents_url)
    soup.prettify().encode('utf8')
    texts = soup.findAll(text=True)
    start_index = texts.index('Donald J. Trump')
    end_index = texts.index('George Washington')
    texts = texts[start_index: end_index+1]
    dict_all_prezs = dict()
    count = 45
    for elem in texts:
        if not elem.isdigit() and elem != ' to ' and elem != ' ' and elem != '\n':
            dict_all_prezs[elem] = count
            count -= 1
    # print(dict_all_prezs)
    return dict_all_prezs

def create_pages(url, page_count):
    items_per_page = 'items_per_page=10'
    page_lst = []
    page_lst.append(url + "?" + items_per_page)
    for i in range(1,(page_count-1)//10):
        page = "page=" + str(i)
        page_lst.append(url + "?" + page + "&" + items_per_page)
    return page_lst

def get_links(url): #opens each individual speech
    soup = scrape(url)
    soup.prettify().encode('utf8')
    content = soup.find_all("div", {"class": "field-title"})
    all_links = []
    for i in content:
        link = "https://www.presidency.ucsb.edu/" + str(i.find("a").get("href"))
        all_links.append(link)
    return all_links

def write_txt(name, scraped_list): #doesn't work
    title = df['title']
    date = df['date']
    file_name = '/Users/Andey/Desktop/Fall2020/CIRP_Lab/'+name+'/'+title+"_"+date+".csv"
    df.to_csv(file_name)
    print("Finished writing " + file_name)

def get_speech(url, dict_all_prezs): 
    soup = scrape(url)
    soup.prettify().encode('utf8')
    #title
    if soup.find("div", {"class": "field-ds-doc-title"}) == None:
        title = "None"
    else:
        title = soup.find("div", {"class": "field-ds-doc-title"}).get_text().strip() 
    #content
    if soup.find("div", {"class": "field-docs-content"}) == None:
        content = "None"
    else:
        content = soup.find("div", {"class": "field-docs-content"}).get_text().strip()
    #date
    if soup.find("span", {"class": "date-display-single"}) == None:
        date = "None"
    else:
        date = soup.find("span", {"class": "date-display-single"}).get_text().strip()
    #president
    if soup.find("div", {"class": "field-title"}) == None:
        president = "None"
    else: 
        president = soup.find("div", {"class": "field-title"}).get_text().strip()
    #removes non president speeches
    if president not in dict_all_prezs: 
        return None
    president_id = dict_all_prezs[president]
    #url to the direct website 
    if soup.find("div", {"class": "field-prez-document-citation"}) == None:
        link2site = "None"
    else:
        link2site = soup.find("div", {"class": "field-prez-document-citation"}).get_text().strip()
        link2site_index = link2site.find('https')
        link2site = link2site[link2site_index:]
    #footnotes
    if soup.find("div", {"class": "field-docs-footnote"}) == None:
        footnote = "None"
    else:
        footnote = soup.find("div", {"class": "field-docs-footnote"}).get_text().strip()
    year = date.strip()[:-5:-1][::-1]
    df = pd.DataFrame({'title': [title],
                   'date': [date],
                   'year': [year],
                   'president': [president],
                   'president_id': [president_id],
                   'content': [content],
                   'url': [link2site],
                   'footnote': [footnote]
                   })
    # print(content)
    return df #[title, date, year, president, president_id, content, link2site, footnote]

def feed_urls(count, name, url, dict_all_prezs):
    print('Starting scrape for ' + name)
    pages = create_pages(url, count)
    all_speeches = []
    count = 1
    for each_page in pages:
        for i in get_links(each_page):
            spch = get_speech(i, dict_all_prezs)
            spch.to_csv('/Users/Andey/Desktop/Fall2020/CIRP_Lab/all_csv_files/test.csv')
            break
            count += 1
            print(count)
            if spch != None:
                print('NOT APPENDED')
                all_speeches.append(spch)
        break
    col_names = ['title', 'date', 'year', 'president', 'president_id', 'content', 'url', 'footnote']
    df = pd.DataFrame(all_speeches, columns=col_names)
    # print(df)
    # df.to_csv('/Users/Andey/Desktop/Fall2020/CIRP_Lab/all/test.csv')
    # df.to_csv('/Users/Andey/Desktop/Fall2020/CIRP_Lab/all/'+name+'_all.csv')
    print('Finished scraping' + name, '\n', df)

def scrape_all():
    csv_file = '/Users/Andey/Desktop/Fall2020/CIRP_Lab/list_to_scrape.csv'
    dict_all_prezs = dict_of_all_presidents()
    df = pd.read_csv(csv_file)
    for i in range(len(df)):
        count = df.iloc[i]['count']
        name = df.iloc[i]['name']
        url = df.iloc[i]['url']
        feed_urls(count, name, url, dict_all_prezs)
    return None

def make_one_csv():
    path = '/Users/Andey/Desktop/Fall2020/CIRP_Lab/all_csv_files'
    col_names = ['title', 'date', 'year', 'president', 'president_id', 'content', 'url', 'footnote']
    frames = []
    for filename in os.listdir(path):
        speech_type = filename[:-8]
        file = path + "/" + filename
        df = pd.read_csv(file)
        # print(len(df), speech_type)
        df['speech_type'] = speech_type
        frames.append(df)
    # print(frames)
    result = pd.concat(frames, ignore_index=True)
    result.drop_duplicates(subset=['content'])
    print(len(result))
    new_path = '/Users/Andey/Desktop/Fall2020/CIRP_Lab/all_csv_files/all_presidential_speeches.csv'
    keep_col =  ['title', 'date', 'year', 'president', 'president_id', 'content', 'url', 'footnote', 'speech_type']
    new_f = result[keep_col]
    new_f.to_csv(new_path, index=True)

if __name__ == "__main__":
    scrape_all()
    # make_one_csv()
    pass