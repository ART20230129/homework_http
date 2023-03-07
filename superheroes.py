import requests
import json
import pprint


url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"

response = requests.get(url)
group_heroes = response.json()
##print(group_heroes )


heroes_list = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}

heroes_dict = {}

for hero in heroes_list:
    for men in group_heroes:
        if men['name'] == hero:
            intelligence_dict[hero] = men['powerstats']['intelligence']
##print(intelligence_dict)
print(f'Супергерой с максимальным интелектом: {max(intelligence_dict, key=intelligence_dict.get)} - {max(intelligence_dict.values())}')


