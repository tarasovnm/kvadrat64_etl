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

