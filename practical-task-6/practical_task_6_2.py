# 2: Создать модуль music_deserialize.py. В этом модуле открыть
# файлы group.json и group.pickle, прочитать из них информацию. И получить объект: словарь из предыдущего задания.
import json, pickle

with open('group.json', 'r', encoding='utf-8') as f:
    json_group = json.load(f)
print(json_group)

with open('group.pickle', 'rb') as f:
    pickle_group = pickle.load(f)
print(pickle_group)