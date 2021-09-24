import json

"""
------------------------------------------> JSON STRING  
"""

people_string = '''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "655-345-1128",
            "emails" : ["smith@tcd.ie", "smithj@microsoft.ie"],
            "hasLicense" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "243-567-6492",
            "emails" : null,
            "hasLicense" : true
        }
    ]
}
'''

# data = json.loads(people_string)

# print(type(data))

# print(type(data['people']))

# for person in data['people']:
#     print(person['name'])

# print()

# for person in data['people']:
#     del person['phone']

# newString = json.dumps(data, indent=2, sort_keys=False)
# print(newString)
# print()

"""
------------------------------------------> JSON FILE  
"""

# with open('example_2.json') as f:
#     data = json.load(f)

# for subject in data['quiz']:
#     print(subject, end = ' ')
#     for question in data['quiz'][str(subject)]:
#         print(question, end = ' ')
#         print( data['quiz'][str(subject)][str(question)]['question'], ' Answer: ', data['quiz'][str(subject)][str(question)]['answer'] , end = ' ')

#     print('')

# for subject in data['quiz']:
#     for question in data['quiz'][subject]:
#         del data['quiz'][subject][question]['options']

# with open('newExample2.json', 'w') as f:
#     json.dump(data, f, indent=2)


"""
------------------------------------------> JSON URL  
"""

from urllib.request import urlopen

with urlopen("https://free.currconv.com/api/v7/convert?q=EUR_INR&compact=ultra&apiKey=156658e17a9a75eefd70") as response:
    source = response.read()

encoding = 'utf-8'
print(source.decode(encoding))
