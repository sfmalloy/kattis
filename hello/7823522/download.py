# import os
# import sys
# import requests
# import bs4
# import configparser
# import time

# from collections import defaultdict

# class Kattis:
#     def __init__(self) -> None:
#         path: str = ''
#         if os.path.exists(os.path.expanduser(os.path.join('~','.kattisrc'))):
#             path = os.path.expanduser(os.path.join('~','.kattisrc'))
#         elif os.path.exists('.kattisrc'):
#             path = '.kattisrc'

#         self.config = configparser.ConfigParser()
#         self.config.read(path)

#         self.data: dict[str] = {'script': 'true'}
#         # TODO uncomment after testing
#         # session = requests.session()
#         # self.auth = session.post(self.config['kattis']['loginurl'],
#         #                          cookies={'username': self.config['user']['username'], 'password': self.config['user']['token']},
#         #                          data=self.data)
        
#         # if self.auth.status_code != 200:
#         #     raise Exception(f'Login failed: {self.auth.status_code} - {self.auth.reason}')
        
#         self.solved_ids = set()
#         page = 0
#         while True:
#             print(f'Gathering names from page {page}...')
#             solved = self.get_solved_ids(page)
#             if len(solved) == 0:
#                 break
#             self.solved_ids |= set(solved)
#             page += 1

#     def get_solved_ids(self, page=0) -> set[str]:
#         options = {'page': page,
#                   'order': 'difficulty',
#                   'show_solved': 'on',
#                   'show_tried': 'off',
#                   'show_untried': 'off',
#                   'script': 'true'}

#         response = requests.get(url=f'https://{self.config["kattis"]["hostname"]}/users/sfmalloy', 
#                                 cookies={'EduSiteCookie': '81a1e563-b30b-4b40-abdc-0330b9691573'}, 
#                                 params=options)

#         soup = bs4.BeautifulSoup(response.text ,'lxml')
#         rows = soup.find('tbody').find_all('tr')

#         solved = []
#         for row in rows:
#             status = row.find('span')
#             print(status)
#             # solved.append(name.find('a').get('href').split('/')[-1])
#         print(solved[:5])
#         return solved

# def main():
#     try:
#         kattis = Kattis()

#     except Exception as e:
#         print(e.args)

# if __name__ == '__main__':
#     main()
print('Hello World!')