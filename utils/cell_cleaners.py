import re

def stage_transform(stage_str):
    if stage_str == 'дом сдан':
        return 'сдан'
    elif stage_str == 'дом построен но не сдан':
        return 'не сдан'
    elif stage_str == 'дом еще строится':
        return 'строится'
    else:
        return 'нет данных'

def parse_year(year_string):
    year_pattern = r'\d{4}'
    match = re.search(year_pattern, year_string)
    return int(match[0]) if match else 0

def parse_district(address_string):
    districts_list = ['ОКТЯБРЬСКИЙ', 'ФРУНЗЕНСКИЙ', 'КИРОВСКИЙ', 'ЗАВОДСКОЙ', 'ВОЛЖСКИЙ', 'ЛЕНИНСКИЙ', 'ЭНГЕЛЬС']
    district_pattern = r'\s[А-Я]{4,},' # r'\s[А-Я]+,'
    address_string = str(address_string)
    match = re.search(district_pattern, address_string)
    district = match[0].replace(',','').strip() if match else ''
    district = district if district in districts_list else 'Не указан'

    return district.lower().capitalize()

def clean_address(address_string):
    district_pattern = r'\s[А-Я]{4,},' # r'\s[А-Я]+,'
    address_string = str(address_string)
    match = re.search(district_pattern, address_string)

    clean_addr = address_string[:match.span()[0] - 1].strip() if match else address_string
    if clean_addr[0] == 'в':
        clean_addr = ','.join(clean_addr.split(',')[1:])

    return clean_addr

def parse_city(address_string):
    districts_list = ['ОКТЯБРЬСКИЙ', 'ФРУНЗЕНСКИЙ', 'КИРОВСКИЙ', 'ЗАВОДСКОЙ', 'ВОЛЖСКИЙ', 'ЛЕНИНСКИЙ', 'ЭНГЕЛЬС']
    district_pattern = r'\s[А-Я]{4,},' # r'\s[А-Я]+,'
    address_string = str(address_string)
    match = re.search(district_pattern, address_string)
    district = match[0].replace(',','').strip() if match else ''
    district = district if district in districts_list else 'Не указан'

    if district in districts_list:
        city = 'Энгельс' if district == 'ЭНГЕЛЬС' else 'Саратов'
    else:
        city = 'Не в списке'

    return city

