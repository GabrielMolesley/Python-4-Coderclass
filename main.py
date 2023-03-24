import os
import sys
import random

woordjes = []
max_lengte= 40
menu = '''
---------------------------------------------------------
|           Welkom bij het overhoorprogramma!            |
|                                                        |
| (B)ekijk een woordenlijst                              |
| (M)aak een woordenlijst                                |
| (S)tart de overhoring                                  |
| (V)erwijder woorden uit een woordenlijst               |
| (Q)uit                                                 |
|                                                        |
---------------------------------------------------------   
'''


def main():
    print(menu)
    menu_optie = input('Kies een optie: ')
    
    if menu_optie == 'B':
        wrd_files = [file for file in os.listdir() if file.endswith('.wrd')]
        
        if len(wrd_files) == 0:
            print('Geen .wrd bestanden gevonden in de directory')
            return
        

        print('Beschikbare .wrd bestanden:')
        for i, file in enumerate(wrd_files):
            print(f'{i+1}. {file}')
        
        
        file_num = int(input('Kies een bestand (1-{}): '.format(len(wrd_files))))
        
        try:
            with open(wrd_files[file_num-1], 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line.strip())
        except IndexError:
            print('Ongeldige keuze')
        except FileNotFoundError:
            print('Bestand niet gevonden')

    elif menu_optie == 'M':


        file_name = input('Geef de naam van het bestand (zonder.wrd): ')


        words = []
        while True:
            word = input('Voer een woord in (of stop om te stoppen): ')
            if word == 'stop':
                break
            elif len(word) > max_lengte:
                print(f'Het woord mag niet langer zijn dan {max_lengte} tekens')
            else:
                translation = input(f'Voer de vertaling van "{word}" in: ')
                words.append(f'{word}={translation}')


        with open(file_name + '.wrd', 'a') as f:
            f.write('\n'.join(words))

        print(f'{len(words)} woorden toegevoegd aan {file_name}.wrd')
    
    elif menu_optie == 'S':
  
        wrd_files = [file for file in os.listdir() if file.endswith('.wrd')]

        print('Beschikbare .wrd bestanden:')
        for i, file in enumerate(wrd_files):
            print(f'{i+1}. {file}')

        file_num = int(input('Kies een bestand (1-{}): '.format(len(wrd_files))))

        file_name = wrd_files[file_num-1]

        with open(file_name) as f:
            words = f.read().splitlines()

        random.shuffle(words)

        correct = 0
        incorrect = 0
        for word in words:
            original_word, translation = word.split('=')
           
            user_translation = input(f'Wat is de vertaling van "{original_word}"? ')

            if user_translation == translation:
                print('Goed zo!')
                correct += 1
            else:
                print(f'Fout! Het juiste antwoord is "{translation}".')
                incorrect += 1

        print(f'Je score is {correct} van de {correct + incorrect} woorden.')
        doorgaan = input('Doorgaan? (ja/nee): ')
        if doorgaan == 'ja':
            main()
        else:
            print("Tot de volgende keer!")
            sys.exit()
    elif menu_optie == 'V':
        wrd_files = [file for file in os.listdir() if file.endswith('.wrd')]

        print('Beschikbare .wrd bestanden:')
        for i, file in enumerate(wrd_files):
            print(f'{i+1}. {file}')

        file_num = int(input('Kies een bestand (1-{}): '.format(len(wrd_files))))
        file_name = wrd_files[file_num-1]

        with open(file_name) as f:
            words = f.read().splitlines()

        print('Woordenlijst:')
        for i, word in enumerate(words):
            print(f'{i+1}. {word}')

        remove_word = input('Voer het nummer in van het woord dat je wilt verwijderen: ')
        try:
            remove_word = int(remove_word)
            if remove_word < 1 or remove_word > len(words):
                raise ValueError
        except ValueError:
            print('Ongeldige keuze')
            return

        words.pop(remove_word-1)

        with open(file_name, 'w') as f:
            f.write('\n'.join(words))

        print(f'Woord verwijderd uit {file_name}')

        doorgaan = input('Doorgaan? (ja/nee): ')
        if doorgaan == 'ja':
            main()
        else:
            print("Tot de volgende keer!")
            sys.exit()

    elif menu_optie == 'Q':
        print('Tot de volgende keer!')
        sys.exit()



main()
