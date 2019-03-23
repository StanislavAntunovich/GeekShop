import re

from django.shortcuts import render

ITEM_PATTERN = '\/item\/(.*)'

SMALL_IMG_PATH = 'img/small/'
IMG_PATH = 'img/'

PAGE_TITLE = 'page_title'

ITEM_NAME = 'item_name'
ITEM_PIC = 'item_pic'
ITEM_LINK = 'item_link'


def index(request):
    context = {PAGE_TITLE: 'Шпунтик и Транзистор'}
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    context = {
        PAGE_TITLE: 'каталог',
        'items': [
            {ITEM_NAME: 'INTEL core i9 7960X',
             ITEM_PIC: SMALL_IMG_PATH + 'intel_i9_7960_300X300.jpg',
             ITEM_LINK: 'i9_7960x'},
            {ITEM_NAME: 'AMD A6 9500',
             ITEM_PIC: SMALL_IMG_PATH + 'amd_a6_9500.jpg',
             ITEM_LINK: 'amd_a6_9500'}
        ]
    }

    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    context = {PAGE_TITLE: 'контакты'}
    return render(request, 'mainapp/contacts.html', context)


def item(request):
    item = re.search(ITEM_PATTERN, request.path)

    context = {
        'i9_7960x': {
            PAGE_TITLE: 'Intel i9 7960',
            'item_img': IMG_PATH + 'intel_i9_7960.jpg',
            'full_name': 'Процессор INTEL Core i9 7960X, LGA 2066 BOX',
            'description': """
                Сокет LGA 2066, ядро Skylake-X, ядер — 16, потоков — 32, L3 кэш 22Мб, Turbo 3.0 — 4.4ГГц,
                частота 2.8 ГГц и 4.2 ГГц в режиме Turbo, техпроцесс 14нм, поддержка памяти DDR4 до 128 ГБ,
                каналов памяти — 4, множитель не заблокирован, контроллер PCI Express 3.0, поставка BOX без кулера.
                """,
            'full_description': """
                Intel Core i9 7960x удивляют своими способностями. Они более чем в 2 раза быстрее «отрисовывают» изображения в Corona 1.3 Benchmark по сравнению с моделями Core i7-8700K,
                которые обладают 6 ядрами. Сотрудники компании Интел, выяснили, что не основная масса покупателей — энтузиасты, которые используют мощности процессоров Core X в индивидуальных целях.
                Большая часть покупателей — разработчики контента.
            """,
            'characteristics': {
                'core': 'Skylake-X',
                'socket': 'LGA 2066',
                'cores_count': '16',
                'threads_count': '32',
                'frequency': '2.8 ГГц и 4.2 ГГц в режиме Turbo',
                'l1_cache': '32×64 КБ',
                'l2_cache': '32×1024 КБ',
                'l3_cache': '22 Мб',
                'discharge': '64 bit',
                'heat': '165 ВТ',
                'max_temp': '98 °С',
                'pci_version': 'PCI Express 3.0',
                'pci_channels_count': '44',
                'guaranty': '36 мес',
                'manufacture_link': 'www.intel.ru'
            }
        },

        'amd_a6_9500': {
            PAGE_TITLE: 'AMD A6 9500',
            'item_img': IMG_PATH + 'amd_a6_9500.jpg',
            'full_name': 'Процессор AMD A6 9500, SocketAM4 OEM',
            'description': """
                    сокет SocketAM4, ядро Excavator, ядер — 2, потоков — 2, частота 3.5 ГГц и 3.8 ГГц в режиме Turbo, техпроцесс 28нм, поддержка памяти DDR4 каналов памяти — 2, контроллер PCI Express 3.0, графическое ядро AMD Radeon R5, поставка OEM
                    """,
            'full_description': """
                    AMD A6-9500 - 2-ядерный процессор с тактовой частотой 3500 MHz и кэшем 2-го уровня 1024 KB. Процессор предназначен для настольных компьютеров, разъем - Socket AM4. Имеет встроенный контроллер оперативной памяти (2 канала, DDR4-2400) и контроллер PCI Express 3.0 (количество линий - 8).
                """,
            'characteristics': {
                'core': 'Excavator',
                'socket': 'SocketAM4',
                'cores_count': '2',
                'threads_count': '2',
                'frequency': '3.5 ГГц и 3.8 ГГц в режиме Turbo',
                'l1_cache': '2х 32 КБ',
                'l2_cache': '1024 КБ',
                'l3_cache': '-',
                'discharge': '64 bit',
                'heat': '65 ВТ',
                'max_temp': '90 °С',
                'pci_version': 'PCI Express 3.0',
                'pci_channels_count': '2',
                'guaranty': '12 мес',
                'manufacture_link': 'www.amd.com/ru-ru'
            }
        }
    }

    return render(request, 'mainapp/item_goods.html', context[item.group(1)])
