#Importing libraries
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd
import os
import pathlib
urlretrieve('https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v4', './book_info.xlsx')
book_info = pd.read_excel('book_info.xlsx')
path = './Springer Books'
os.mkdir(path)
for index, row in book_info.iterrows():
    print(row['Book Title'])
    if(pathlib.Path(path+'/'+row['English Package Name']).exists()):
        url = row['OpenURL']
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        try:
            book_file = soup.find(class_ = 'c-button c-button--blue c-button__icon-right test-download-book-options test-bookpdf-link').get('href')
        except AttributeError:
            book_file = soup.find(class_ = 'c-button c-button--blue c-button__icon-right test-bookpdf-link').get('href')
        urlretrieve('https://link.springer.com/' + book_file, path+ '/'+row['English Package Name']+'/'+row['Book Title']+'.pdf')
    else:
        os.mkdir(path+'/'+row['English Package Name'])
        url = row['OpenURL']
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        try:
            book_file = soup.find(class_ = 'c-button c-button--blue c-button__icon-right test-download-book-options test-bookpdf-link').get('href')
        except AttributeError:
            book_file = soup.find(class_ = 'c-button c-button--blue c-button__icon-right test-bookpdf-link').get('href')
        urlretrieve('https://link.springer.com/' + book_file, path+ '/'+row['English Package Name']+'/'+row['Book Title']+'.pdf')