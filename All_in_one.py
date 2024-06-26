import os,shutil,os.path,os,subprocess,math,datetime,pathlib
from datetime import datetime
from colorama import Fore,init
init(convert=True)


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
def banner():
  banner_st = r'''  ____ _     _          ____ ____        ___  ____    ___ 
 /    | |   | |        |    |    \      /   \|    \  /  _]
|  o  | |   | |         |  ||  _  |    |     |  _  |/  [_ 
|     | |___| |___      |  ||  |  |    |  O  |  |  |    _]
|  _  |     |     |     |  ||  |  |    |     |  |  |   [_ 
|  |  |     |     |     |  ||  |  |    |     |  |  |     |
|__|__|_____|_____|    |____|__|__|     \___/|__|__|_____|
                                                          '''
  print(Fore.RED + banner_st + Fore.RESET)
def rename_sort_add_counter_to_beginning(folder):

  to_sort_counter = 0
  sort_number = 1

  formats_to_sort = input('What File Formats You Want To Sort?\n')

  if not '.' in formats_to_sort :
    formats_to_sort = '.'+formats_to_sort

  for file in os.listdir(folder):
    if os.path.splitext(file)[1] == formats_to_sort :
      print('-' * len(file))
      print(file)
      to_sort_counter += 1

  pre_output = f'{to_sort_counter} Files To Sort By Number.\n'
  print('-' * len(pre_output))
  print(pre_output)

  sure = input('Enter Y To Start Sorting..\n')
  if sure == 'Y':
    for file in os.listdir(folder):
      if os.path.splitext(file)[1] == formats_to_sort:
        full_path = folder + file
        new_name = folder + str(sort_number) + f' {file}'
        os.rename(full_path,new_name)
        print(f'Renamed "{file}" ==> "{str(sort_number) + f' {file}'}"')
        sort_number +=1

  else:
    print('Nothing Were Renamed..')

def show_all_files(folder):
  found_files = 0
  found_folders = 0
  file_index = 1

  for item in os.listdir(folder):
    full_path = os.path.join(folder, item)
    file_size = os.path.getsize(full_path)

    if os.path.isfile(full_path):
      result = f'{file_index} | {item} | {full_path} | {convert_size(file_size)}'
      print(Fore.YELLOW + result + Fore.RESET)
      print('-' * len(result))
      found_files += 1
      file_index += 1

    elif os.path.isdir(full_path):
      result = f'{file_index} | {item} [ Folder ] | {full_path} | {get_inside_folder_files_size_formated(full_path)}'
      print(Fore.CYAN + result + Fore.RESET)
      print('-' * len(result))
      found_folders += 1
      file_index += 1

  if found_folders or found_files > 0:
    print('Showing:')
  if found_files > 0:
    print(f'{found_files} Matched Files.')
  if found_folders > 0:
    print(f'{found_folders} Matched Folders.')
  if found_folders + found_files == 0:
    print('No Matching Item.')

  result = fr"* Showing All {len(os.listdir(folder))} Files\Folders."
  print(result)
  print('-' * len(result))


def delete_certain_files(folder):
  show_all_files(folder)
  try:
    what_to_remove = input('What File Types You Want To Delete?\nRemember This Will Delete All Matching Files.(NO RECOVERY!)\nExample: "mp3"\n')
  except KeyboardInterrupt:
    exit('User Exited..')

  if not '.' in what_to_remove :
    what_to_remove = '.' + what_to_remove

  to_remove_counter = 0
  to_remove_list = []
  removed_counter = 0

  for file in os.listdir(folder):
    full_file_path = folder + file
    file_extension = os.path.splitext(file)[1]
    if os.path.isfile(full_file_path):
      if file_extension == what_to_remove :
        file_size = convert_size(os.path.getsize(full_file_path))
        to_remove_counter +=1
        to_remove_list.append(full_file_path)
        out_put = f'{file} | {file_size}'
        print(out_put)
        print('-' * len(out_put))

  if not to_remove_counter > 0:
    print('No Matching Files Were Found.')

  if to_remove_counter > 0 :
    print(f'Found {to_remove_counter} Matching Files.\n')

    try:
      sure = input('Enter y To Confirm Deletion.\n')
    except KeyboardInterrupt:
      exit('User Exited..')

    if sure == 'y':
      for file in to_remove_list:
        os.remove(file)
        removed_counter +=1
    else:
      print('No Files Were Removed.')

  if removed_counter > 1:
    print(f"{removed_counter} Files Were Removed.")
  elif removed_counter == 1:
    print('One File Removed')
def keep_certain_files(folder):

  show_all_files(folder)

  while True:

    try:
      what_to_keep = input('What File Types You Want To Keep?\n')
    except KeyboardInterrupt:
      exit('User Exited..')

    if what_to_keep == '':
      print('You Should Enter a Format Type !!!')
      print('All Files That Doesn\'t Have the Entered File Type Will Be Removed.')
      continue

    if not '.' in what_to_keep:
      what_to_keep = '.' + what_to_keep

    match_counter = 0
    file_list = []
    for file in os.listdir(folder):
      full_file_path = folder + file
      file_list.append(full_file_path)

    for file in file_list:
      if os.path.isfile(file):
        if os.path.splitext(file)[1] != what_to_keep:
          file_name = Fore.YELLOW + os.path.basename(file) + Fore.RESET
          print(file_name)
          os.remove(file)
          match_counter += 1

    if match_counter == 0:
      print('No Files Were Removed.')

    elif match_counter > 0:
      print("Files Shown Above Were Removed.")

    break

def replace_letters(folder):

  show_all_files(folder)

  try:
    letters_to_remove = input('What Do You Want To Remove to Replace From File Names ?\n')
  except KeyboardInterrupt:
    exit("User Exited..")

  to_rename = 0
  renamed_files = 0
  to_rename_list = []

  for file in os.listdir(folder):
    full_path = os.path.join(folder,file)
    if letters_to_remove in os.path.basename(full_path):
      to_rename += 1
      print(Fore.YELLOW + file +Fore.RESET)
      to_rename_list.append(full_path)
  print(f'{to_rename} Files To Replace letters.')

  if to_rename > 0 :

    try:
      letter_to_replace = input("What Do You Want To Replace The Words With ?\n")
      rename = input('Rename ? (y) to Continue.\n')
    except KeyboardInterrupt:
      exit('User Exited..')

    if rename.lower() == 'y':
      for file in to_rename_list:
        new_file_name = os.path.basename(file).replace(letters_to_remove, letter_to_replace)
        new_full_path = os.path.join(folder,new_file_name)
        os.rename(file, new_full_path)

        if os.path.isdir(new_full_path):
          result = f'Renamed Folder: {os.path.basename(file)} --> {new_file_name}'
          print(Fore.CYAN + result + Fore.RESET)
          renamed_files += 1
        elif os.path.isfile(new_full_path):
          result = f'Renamed File: {os.path.basename(file)} --> {new_file_name}'
          print(Fore.YELLOW + result + Fore.RESET)
          renamed_files += 1
    else:
      print("No Files Were Renamed..")

    if renamed_files > 1 :
      print(f'{renamed_files} Files/Folders Been Renamed.')
    elif renamed_files == 1:
      print('File/Folder Was Rename Successfully..')


def remove_letters(folder):

  show_all_files(folder)
  try:
    letters_to_remove = input('What Do You Want To Remove From File Names ?\n')
  except KeyboardInterrupt:
    exit('User Exited..')

  to_rename = 0
  renamed_files = 0
  to_rename_list = []
  for file in os.listdir(folder):
    if letters_to_remove in os.path.splitext(file)[0]:
      to_rename += 1
      print(file)
      to_rename_list.append(os.path.join(folder,file))

  print(f'{to_rename} Files To Rename.')

  if to_rename > 0 :

    try:
      rename = input('Rename ? (y) to Continue.\n')
    except KeyboardInterrupt:
      exit('User Exited..')

    if rename.lower() == 'y':
      for file in to_rename_list:
          new_file_name = os.path.basename(file).replace(letters_to_remove, '')
          new_full_path = os.path.join(folder, new_file_name)
          os.rename(file, new_full_path)
          out = f'Renamed: {os.path.basename(file)} --> {os.path.basename(new_file_name)}'
          print(Fore.YELLOW + out + Fore.RESET)
          renamed_files += 1
      print(f'{renamed_files} Files Been Renamed.')
    else:
      print("No Files Were Renamed..")
def convert_size(size_bytes):
  if size_bytes == 0:
    return "0B"
  size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
  try:
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
  except Exception as err:
    print(Fore.RED + 'Could Not Calculate the Size; Revise Code to Fix the Issue.' + Fore.RESET)
def get_inside_folder_files_size_formated(folder):
  if not folder.endswith == '\\':
    folder = folder + ('\\')
  totall_size = 0

  for root, dirs, file in os.walk(folder):
    for item in file:
      full_path = os.path.join(root,item)
      totall_size += os.path.getsize(full_path)
  return convert_size(totall_size)
def deep_search(folder,what_to_search):
  d_found_items = 0
  file_index = 1

  for root, dirs, file in os.walk(folder):
    for item in file :
      full_path = os.path.join(root, item)
      item_size = os.path.getsize(full_path)

      if what_to_search in item:
        file_info = f'{file_index} | {item} | {full_path} | {convert_size(item_size)}'
        print(Fore.YELLOW + file_info + Fore.RESET)
        print('-' * len(file_info))
        file_index += 1
        d_found_items += 1

    for directory in dirs:
      full_path = os.path.join(root,directory)
      item_size = os.path.getsize(full_path)

      if what_to_search in directory:
        result = f'{file_index} | ' + directory + ' [ Folder ]'+ f' | {full_path} | {get_inside_folder_files_size_formated(full_path)}'
        print(Fore.CYAN + result + Fore.RESET)
        print('-' * len(result))
        d_found_items += 1
        file_index += 1

  if d_found_items > 0:
    final_result = 'Items Found In Deep Search.'
    print(final_result)
    print("-" * len(final_result))
  else:
    print('Nothing Was Found.')
def show_match_find(folder,what):
  found_files = 0
  found_folders = 0

  for item in os.listdir(folder):
    full_path = os.path.join(folder,item)

    if what in item and os.path.isfile(full_path):
      print(item)
      print('-' * len(item))
      found_files +=1

    elif what in item and os.path.isdir(full_path):
      print(item + ' [Folder]')
      print('-' * len(item))
      found_folders += 1


  if found_folders or found_files > 0:
    print('Showing:')
  if found_files > 0:
    print(f'{found_files} Matched Files.')
  if found_folders > 0:
    print(f'{found_folders} Matched Folders')
  if found_folders + found_files == 0:
    print('No Matching Item.')
def File_copier():

  while True:
    try:
      path_to_copy = input('Enter File\\Folder Path to Copy. or CTRL + C To Exit..\n')
    except KeyboardInterrupt:
      exit('User Exited..')

    except FileNotFoundError:
      exit('There is No File in Entered Directory.\nTry Again..\n')


    if os.path.isdir(path_to_copy):
      print('Entered Path is a Folder.')
      print(len(os.listdir(path_to_copy)), ' Files Were Found')

      try:
        copy_all = input('Copy All Items Inside The Folder (y)?\n')
      except KeyboardInterrupt:
        exit('\nUser Exited..')

      if copy_all == 'y':

        try:
          where_to_copy = input('Enter Where to Save File... \n')

        except KeyboardInterrupt:
          exit('User Exited..')
        except FileNotFoundError:
          exit('Invalid Directory.\nTry Again..\n')


        iterated_folder = os.listdir(path_to_copy)
        for item in iterated_folder:

          if not path_to_copy.endswith('\\'):
            path_to_copy = path_to_copy + '\\'

          full_path = os.path.join(path_to_copy,item)

          if os.path.isfile(full_path):
            shutil.copy(full_path, where_to_copy)
            out = f'{os.path.basename(full_path)} Copied To {where_to_copy}'
            print(Fore.YELLOW + out + Fore.RESET)

          elif os.path.isdir(full_path):
            folder_name = os.path.basename(full_path)
            where_to_copy = where_to_copy + ('\\') +folder_name
            shutil.copytree(full_path,where_to_copy,dirs_exist_ok=True)
            out = f'{os.path.basename(full_path)} Copied To {where_to_copy}'
            print(Fore.YELLOW + out + Fore.RESET)

      else:
        print('Wrong Command Retry.')
        continue


      exit(f'{len(iterated_folder)} Files Copied :) ')



    elif os.path.isfile(path_to_copy):
      print('Entered Path Is A File')

      try:
        where_to_copy = input('Enter A Path To Copy The File To. \n')
        if where_to_copy:
          shutil.copy(path_to_copy, where_to_copy)
          out = f'{os.path.basename(path_to_copy)} Copied to {where_to_copy}'
          print(Fore.YELLOW + out + Fore.RESET)
          exit("Done :) ")
        else:
          continue

      except FileNotFoundError as err:
        print(err)

    else:
      print('Invalid Entry.')
def File_remover():
  while True:

    try:
      to_delete = input('Enter a File or Folder Path to Remove. \n')
    except KeyboardInterrupt:
      exit('Uesr Exited..')

    if len(to_delete) != 0:

      if os.path.isfile(to_delete):

        try:
          agree_to_remove = input('Entered Path is a File.\nContinue To Delete ?! \n(BE CAUTIOUS ! PERMENANT REMOVAL !)\nyes to remove: ')
        except KeyboardInterrupt:
          exit('User Exited..')

        if agree_to_remove.lower() == 'yes':
          os.remove(to_delete)
          print(f'{to_delete} Were Removed. :) ')
          break
        else:
          print('No File Was Removed. ')
          break


      elif os.path.isdir(to_delete):

        agree_to_remove = input('Entered Path is a Folder.\nContinue To Delete ?! \n(BE CAUTIOUS ! PERMENANT REMOVAL !)\nyes or no: ')

        if agree_to_remove.lower() == 'yes':
          shutil.rmtree(to_delete)
          print('Folder Removed. :) ')
          break
        else:
          print('No Folder Was Removed. ')
          break
      else:
        print("Enter A Valid Path..")
        continue
    else:
      print('No Path Was Entered..')
      continue
def File_editor():
  while True :

    try:
      folder = input('Enter Folder Path to Rename or Arrange..\n')
    except KeyboardInterrupt:
      exit('User Exited..')

    if not os.path.isdir(folder):
      print('Invalid Directory.')
      continue

    if not folder.endswith('\\'):
      folder = folder + '\\'

    print(f'{len(os.listdir(folder))} Files Detected (Including Subfolders).')

    try:
      what_to_do = input('What Do You Want To Do With The Files ?\n1. To Rename Files \n2. To Remove File\n')
    except KeyboardInterrupt:
      exit('User Exited..')

    if what_to_do == '1':

      try:
        rename_by = input('How Do You Want To Rename Your Files ?\n1. remove letters \n2. replace letters \n3. Add a Counter to File Name\n')
      except KeyboardInterrupt:
        exit('User Exited..')

      if rename_by.lower() == '1':
        remove_letters(folder)
        break

      elif rename_by.lower() == '2':
        replace_letters(folder)
        break

      elif rename_by.lower() == '3':
        rename_sort_add_counter_to_beginning(folder)
        break

    elif what_to_do == '2':

      try:
        how_to_remove = input("Keep or Delete Certain Types of Files\n1. keep \n2. delete\n")
      except KeyboardInterrupt:
        exit('User Exited..')

      if how_to_remove == "1":
          keep_certain_files(folder)
          break

      elif how_to_remove == "2":
          delete_certain_files(folder)
          break

    else:
      print("Invalid Entry.\n:")
  else:
    print("Wrong Entry!\n:")
def File_finder():
  try:
    folder = input(Fore.LIGHTYELLOW_EX + "Enter The Path You Want To Search Through..\n" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + f'{len(os.listdir(folder))} Items Found.' + Fore.RESET)
  except FileNotFoundError:
    exit('Need to Enter a Valid Directory.\nEx: D:\\Folder\\folder')
  except KeyboardInterrupt:
    exit('User Exit..')

  try:
    what_to_search = input(Fore.LIGHTYELLOW_EX + 'What Do You Want To Find ? (Press ENTER to Show All Files)\n' + Fore.RESET)
    print("-" * len(what_to_search))
  except KeyboardInterrupt:
    exit("User Exit..")

  if what_to_search != '' :
    show_match_find(folder,what_to_search)
  elif what_to_search == '':
    show_all_files(folder)

  try:
    deeper = input(Fore.RED +'Go Deeper ?  y/n\n' + Fore.RESET)
  except KeyboardInterrupt:
    exit('User Exited..')

  if deeper == 'y':
    deep_search(folder,what_to_search)

  else:
    print('OK. Bye!')
def remove_if_in_filename():
  folder = input("Enter a Path...\n")

  if not folder.endswith('\\'):
    folder = folder + '\\'

  while True:
    if os.path.isdir(folder):
      pass
    else:
      print('No Valid Directory Was Entered. Retry..\n')
      break

    to_remove_list = []
    removed_counter = 0
    to_remove_counter = 0


    word = input('Enter Word or Letters That If In FileName , File To Be Removed.\n')
    print('-' * len(word))

    for file in os.listdir(folder):
      file_fullpath = folder + file

      if word in file:
        to_remove_list.append(file_fullpath)
        to_remove_counter += 1
        print(file)
        print('=' * len(file))

    if to_remove_counter > 1:
      print(f'{to_remove_counter} Files To Remove.')
    elif to_remove_counter == 1:
      print('One File To Remove.')

    if to_remove_counter > 0:
      sure = input('Enter Y To Remove Matching Files.\n: ')

      if sure == 'Y':
        for file in to_remove_list:
          os.remove(file)
          removed_counter += 1

    else:
      print('No Matching Files To Remove.\n')

    if removed_counter > 0:
      print(f'{removed_counter} Files Were Removed.')
    elif removed_counter == 1:
      print('One File Was Removed.')

    re_do = input('Press Any Key To Go Over Again Or (n) To Exit.\n')
    if re_do == 'n':
      print('Bye!')
      break
    else:
      continue
def timestamp_time_converter(timestamp):
  time = datetime.fromtimestamp(timestamp)
  regular_time = time.strftime('%Y/%m/%d %H:%M:%S')
  return regular_time
def files_info(folder):
  count = 0

  #print('*' * len(folder))

  if not folder.endswith('\\'):
    folder = folder + '\\'
  try:
    if not os.path.exists(folder):
      raise FileNotFoundError
  except FileNotFoundError:
    print('\nFolder Not Found.')

  totall_files_size = 0
  indexer = 0
  if os.path.exists(folder):
    for file in os.listdir(folder):
      indexer += 1
      count += 1
      file_fullpath = folder + file
      file_info = os.stat(file_fullpath)

      creation_timestamp = os.path.getctime(file_fullpath)
      modified_timestamp = os.path.getmtime(file_fullpath)

      creation_regular_time = timestamp_time_converter(creation_timestamp)
      modification_regular_time = timestamp_time_converter(modified_timestamp)

      file_size = convert_size(os.stat(file_fullpath)[6])
      file_type = os.path.splitext(file)

      if '.' in  file_type[1]:
        totall_files_size += os.stat(file_fullpath)[6]
        file_extention = file_type[1].replace('.','')
        out_put = f'{indexer} | {file_type[0]}| {file_extention} | Created: {creation_regular_time} | Modified: {modification_regular_time}| {file_size}'
        print(out_put)
        print('-' * len(out_put))


      totall_size = 0
      if os.path.isdir(file_fullpath):
        for root,dirs,items in os.walk(file_fullpath):
          for item in items:
            file_path = root +'\\'+ item
            totall_size += os.path.getsize(file_path)
            totall_files_size += os.path.getsize(file_path)

        outt_put = f'{indexer} | {file} | Folder | Created: {creation_regular_time} | Mofified: {modification_regular_time} | {convert_size(totall_size)}'
        print(outt_put)
        print('=' * len(outt_put))


    print(f'{count} Items.\nTotall Size: {convert_size(totall_files_size)}')
    disclaimer = '"Created" represents the time that file was copied or moved to this directory.\n"Modified" refers to the modification time of the file\'s metadata.'
    print('*'* 78)
    print(disclaimer)
    print('*'* 78)

def main():
  clear_screen()
  banner()
  print(Fore.LIGHTYELLOW_EX + 'Welcome To "All In One" Python Script.\n' + Fore.RESET)
  print( r'1. To Copy File\Folder.')
  print('2. To Delete A File (Completely).')
  print('3. File Manipulations. (Remove - Rename)')
  print('4. Search.')
  print('5. To Delete If A Word In File Name.')
  print('6. To View File Info.' )
  print(Fore.LIGHTYELLOW_EX + 'Enter a Command to continue: ' + Fore.RESET)
  COMMAND = input()

  if COMMAND.lower() == '1':
    File_copier()
  elif COMMAND.lower() == '2':
    File_remover()
  elif COMMAND.lower() == '3':
    File_editor()
  elif COMMAND.lower() == '4':
    File_finder()
  elif COMMAND.lower() == '5':
    remove_if_in_filename()
  elif COMMAND.lower() == '6':
    files_info(folder=input("Enter a Path to Continue: "))
  else:
    print('Wrong Command\nTry Again...')



if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    exit(Fore.RED + '\nUser Exited..' + Fore.RESET)
  except Exception as err :
    exit(f"Error\nDetails: {err}")



