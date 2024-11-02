# <img src="img/img1.PNG" /> => ![img1](/labX/img/img1.PNG)

starting_dir = "pages"


import re
import sys
import os

def convert_img_tags(file_path, folder_name):
    # Odczytujemy zawartość pliku
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Wyrażenie regularne do znajdowania tagów <img src="..."/>
    pattern = r'<img src="([^"]+)"\s*/?>'
    
    # Funkcja do zamiany <img> na Markdown
    def replace_img_tag(match):
        img_path = match.group(1)  # Pobieramy ścieżkę do obrazka, np. img/img1.PNG
        img_name = os.path.basename(img_path)  # Pobieramy nazwę pliku, np. img1.PNG
        img_base_name, _ = os.path.splitext(img_name)  # Usuwamy rozszerzenie z nazwy, np. img1
        # Tworzymy nowy format: ![img1](/{folder_name}/img/img1.PNG)
        return f'![{img_base_name}](/' + folder_name + '/' + "img/" + img_base_name + ".webp" + ')'
    
    # Zamieniamy wszystkie dopasowania w zawartości
    new_content = re.sub(pattern, replace_img_tag, content)
    
    # Zapisujemy zmienioną zawartość z powrotem do pliku
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f'Plik {file_path} został przetworzony.')

if __name__ == "__main__":
    file_path = input("Podaj ścieżkę do pliku: ")
    file_path = os.path.join(starting_dir, file_path)
    folder_name = input("Podaj nazwę folderu (np. 'labX'): ")
    convert_img_tags(file_path, folder_name)
