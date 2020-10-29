from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import csv
import uuid
import json
from .models import MainUrl
from .models import SecondaryUrl


def home(request):
    url = MainUrl.objects.filter()

    return render(request, 'home.html', {'url': url})


def url_validation(request):
    url = request.POST.get('url')
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')

    links = []
    for link in soup.find_all('a'):
        link_url = link.get('href')

        if link_url is not None and link_url.startswith('http'):
            links.append(link_url)
            # print(links)
    create_file(request, links)
    return redirect('/')


def create_file(request, links):
    filename = uuid.uuid4().hex[:32].upper()
    # print(filename)

    csv_file = open(filename+'.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([links])
    csv_file.close()

    with open(filename+'.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            content = line
            # print(content)
        # f.writelines(links)
        url = request.POST.get('url')
        file = filename
        url = MainUrl.objects.create(url=url, file=file)
        url.save()

    return render(request, 'home.html')


def get_all_links(url):
    for link in url_validation(url):
        get_all_links(link)


# def fornecedoresDelete(request, id):
#     fornecedor = Fornecedor.objects.get(id=id)
#     fornecedor.delete()
#     return redirect('fornecedores')
