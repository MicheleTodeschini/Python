# dictionary = a collection of {key:value} pairs ordered and changeable. no duplicates

capitals = {'USA': 'Washington D.C',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals.get('USA'))  # PRENDE CAPITALE AMERICANA



""" capitals.update({'Germany': 'Berlin'}) """

""" capitals.pop('China') """
""" capitals.popitem()  remove the last item 
 """
""" print(capitals) """

""" for value in capitals.values():
    print(value) """ 

for key, value in capitals.items():
    print(f'{key}: {value}')