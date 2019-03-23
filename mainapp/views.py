from django.shortcuts import render


PAGE_TITLE = 'page_title'


def index(request):
    context = {PAGE_TITLE: 'Шпунтик и Транзистор'}
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    context = {PAGE_TITLE: 'каталог',
               'items': [{'item_name': 'INTEL core i9 7960X',
                          'item_pic': ''},
                         {}]}
    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    context = {PAGE_TITLE: 'контакты'}
    return render(request, 'mainapp/contacts.html', context)


def item(request):
    return render(request, 'mainapp/item_goods.html')
