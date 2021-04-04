#1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы,
# например:
import pickle, json
my_favourite_group = {
'name': 'Пионерлагерь пыльная радуга',
'tracks': ['Картинки', 'Тяжело и медленно'],
'Albums': [{'name': 'Хлам', 'year': 2013},
{'name': 'правда о потерянном времени', 'year': 2015}]}

pickle_group = pickle.dumps(my_favourite_group)
print(pickle_group)

json_group = json.dumps(my_favourite_group)
print(json_group)

#С помощью модулей json и pickle
#сериализовать данный словарь в json и в байты
#, вывести результаты в терминал. Записать результаты
#в файлы group.json, group.pickle соответственно.
#В файле group.json указать кодировку utf-8.

with open('group.pickle', 'wb') as f:
   pickle.dump(my_favourite_group, f)
with open('group.json', 'w', encoding='utf-8') as f:
   json.dump(my_favourite_group, f)