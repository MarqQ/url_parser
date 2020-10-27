from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests


def home(request):
    return render(request, 'home.html')


def url_validation(request):
    if request.method == 'POST':
        url = request.POST['url']
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        for link in soup.find_all('a', href=True):

            first_char = link['href'][:4]

            if "#" not in link['href']:
                if first_char != 'http':
                    final_link = url + link['href']
                    print(final_link)
                else:
                    print(link['href'])

    return render(request, 'home.html')
