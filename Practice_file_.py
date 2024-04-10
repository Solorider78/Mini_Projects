import requests,socket,validators
from colorama import Fore,init

init(convert=True)

def validate_url(url):
  val = validators.url(url)
  if val == True:
    if 'https://' in url:
      shot_url = url[8:]
      check = socket.gethostbyname(shot_url)

      return (True,check)

    elif 'http://' in url:
      short_url = url[7:]
      check = socket.gethostbyname(short_url)

      return (True,check)
  else:
    print('Invalid URL.')


try:

  get_url = input('Enter a URL: ')
  check_url = validate_url(get_url)

  if check_url[0] == True:
    out = f'IP: {check_url[1]}'
    print(Fore.YELLOW + out + Fore.RESET)

except socket.gaierror:
  print('URL Not Found.')

except KeyboardInterrupt:
  print('Uesr Exited.')

except TypeError:
  pass

