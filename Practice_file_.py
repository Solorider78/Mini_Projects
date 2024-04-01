personal = {
    'name': 'amir',
    'last_name': 'ajvad',
    'age': 23,
    'job': 'sales,programming',
    'interests': 'Not sure',


}


info = f'Name: {personal["name"]}\nLast Name: {personal["last_name"]}\nAge: {personal["age"]}\nJob: {personal["job"]}\nInterests: {personal["interests"]}'

# print(info)


# import requests
# from bs4 import BeautifulSoup
# links = []
# respond = requests.get(r'https://musiceto.com/music-shade-ghadimi/')
#
# soup = BeautifulSoup(respond.text,'html.parser')
#

# links.append()


# for item in soup.select('a[rel=nofollow]'):
#   links.append(item)
# with open('result.txt','w') as f:
#     for i in links:
#         f.write(str(i))
#
#     print('done')

# with open('result.txt') as f:
#     text = f.read()
#
# if ' ' in text:
#     new_text = text.replace(' ','\n')
#     print('done')
#
# with open('new_result.txt','w') as nf:
#     nf.write(new_text)

# with open('final_result.txt') as f:
#     text = f.read()
#     new_text = text.replace('"','')
#     print('done fixing')
# with open('final_result2.txt','w') as nf:
#     nf.write(new_text)
#     print('done writing..')

# with open(r'F:\Codings\Solorider78\final_result2.txt') as f:
#     new_links = []
#     links = f.readlines()
#     for link in links:
#         link = '"'+link+'"'
#         new_links += link + ','
#
# with open('hope_full_results.txt','w') as nf:
#     nf.writelines(new_links)
#     print('done')