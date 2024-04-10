import getpass, os ,time ,requests,webbrowser,clipboard,subprocess
from  colorama import Fore,init
from bs4 import BeautifulSoup

init(convert=True)

TEXT_FILE = 'Handpicked Hacker News Links.txt'

def banner():
  return r'''  _    _               _                _   _                         _____                                      
 | |  | |             | |              | \ | |                       / ____|                                     
 | |__| |  __ _   ___ | | __ ___  _ __ |  \| |  ___ __      __ ___  | (___    ___  _ __  __ _  _ __    ___  _ __ 
 |  __  | / _` | / __|| |/ // _ \| '__|| . ` | / _ \\ \ /\ / // __|  \___ \  / __|| '__|/ _` || '_ \  / _ \| '__|
 | |  | || (_| || (__ |   <|  __/| |   | |\  ||  __/ \ V  V / \__ \  ____) || (__ | |  | (_| || |_) ||  __/| |   
 |_|  |_| \__,_| \___||_|\_\\___||_|   |_| \_| \___|  \_/\_/  |___/ |_____/  \___||_|   \__,_|| .__/  \___||_|   
                                                                                              | |                
                                                                                              |_|                '''
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def save_in_file(story):
  with open(TEXT_FILE, 'a+') as f :
    f.write(f'Title : {story['Title']}, Link : {story['Link']}\n')
    print(Fore.GREEN + "Data saved in text file." + Fore.RESET)

# Takes a URL and retrives Contents of Titles, Links and Votes as Subtexts with CSS selectors
def scraper(*urls):
  links = []
  subtext = []
  for url in urls:
    try:
      response = requests.get(url)

    except requests.exceptions.ConnectTimeout:
      exit('Network Error..\nCheck Your Internet Connection....')

    soup = BeautifulSoup(response.text, 'html.parser')
    links += soup.select('.titleline')
    subtext += soup.select('.subtext')
  return links, subtext

# Sorts the list of News grabed from 'create_custom_hn' Function
def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key=lambda k: k['points'], reverse=True)

# Returns a list of dictionaries containing Title,Link and number of Votes of every single News if the News has More than 100 votes
def create_custom_hn(links, subtext):
  hn = []
  for index, item in enumerate(links):
    title = links[index].getText()
    href = links[index].find('a').get('href', None)
    vote = subtext[index].select('.score')
    if vote:
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'Title': title, 'Link': href, 'points': points})
  return sort_stories_by_votes(hn)

def main():
  clear_screen()
  print(Fore.RED + banner() + Fore.RESET)
  links, subtext = scraper('https://news.ycombinator.com/','https://news.ycombinator.com/?p=2')
  custom_news = create_custom_hn(links, subtext)  # *create_custom_hn* Function is ran and saved in a variable

  # Outputs an indexed news Titles and number of Votes It has
  for counter, story in enumerate(custom_news, 1):
    time.sleep(.2)

    print(Fore.YELLOW + str(counter) + Fore.RESET, story['Title'], f"{story['points']} Votes.")

  # Takes an input as News Indexer to return the link to that news
  while True:

    try:

      to_get_story = input( Fore.YELLOW +"==> Enter News Number To Get It's Link or 'x' to exit: " + Fore.RESET)
      if to_get_story == 'x':
        clear_screen()
        print(Fore.RED + banner() + Fore.RESET)
        exit(Fore.GREEN + 'Bye!' + Fore.RESET)
        break

      to_get_story = int(to_get_story) - 1
      if 0 <= to_get_story < len(custom_news):  # Controls the input to be within the Range of News
        selected_story = custom_news[to_get_story]
        browse = input(Fore.YELLOW + "Open in Browser [b] or copy link to Clipboard [c] or save to text file [t] ?  " + Fore.RESET)

        if browse == "b":
          webbrowser.open(selected_story['Link'])
          print(Fore.GREEN +"Opened in a Browser.." + Fore.RESET)

        elif browse == 'c':
          clipboard.copy(selected_story['Link'])
          print(Fore.GREEN +"Link copied to clipboard. " + Fore.RESET)

        elif browse == 't':
          save_in_file(selected_story)

        else:
          print(Fore.RED +'Invalid Entry.' + Fore.RESET)
        continue

      else:
        print(Fore.RED + "Invalid input. Please enter a valid news number." + Fore.RESET)

    except ValueError:
      print(Fore.RED + 'Invalid Entry.' + Fore.RESET)
      continue




if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print(Fore.RED + '\nExited By User...' + Fore.RESET)

