import pandas as pd
from utils.cell_cleaners import stage_transform, parse_year, parse_city, parse_district, clean_address

# Загружаем данные
aprtmnts_data = pd.read_csv('apartments.csv')

# Преобразуем столбцы с датой
aprtmnts_data['Создано']= pd.to_datetime(aprtmnts_data['Создано'], format="%d-%m-%Y")
aprtmnts_data['Обновлено']= pd.to_datetime(aprtmnts_data['Обновлено'], format="%d-%m-%Y")

# Добавляем столбец со стоимостью 1 кв.м.
aprtmnts_data['Стоимость 1 кв.м.'] = aprtmnts_data['Стоимость'] / aprtmnts_data['Площадь']

# Работаем со столбцами, содержащими года постройки дома
aprtmnts_data['Стадия строительства'] = aprtmnts_data['Стадия строительства'].apply(stage_transform)

aprtmnts_data[['Вторичное жилье']].fillna('нет данных', inplace=True)
aprtmnts_data['Вторичное жилье'] = aprtmnts_data['Вторичное жилье'].apply(str)
aprtmnts_data['Вторичное жилье'] = aprtmnts_data['Вторичное жилье'].apply(parse_year)

aprtmnts_data[['Дата сдачи']].fillna('нет данных', inplace=True)
aprtmnts_data['Дата сдачи'] = aprtmnts_data['Дата сдачи'].apply(str)
aprtmnts_data['Дата сдачи'] = aprtmnts_data['Дата сдачи'].apply(parse_year)

# Работаем со столбцом адреса
aprtmnts_data['Город'] = aprtmnts_data['Адрес'].apply(parse_city)
aprtmnts_data['Район'] = aprtmnts_data['Адрес'].apply(parse_district)
aprtmnts_data['Адрес кр'] = aprtmnts_data['Адрес'].apply(clean_address)

# Получаем координаты по адресу

# Сохраняем обработанные данные в файл
aprtmnts_data.to_csv('apartments_prep.csv', index=None, header=True)