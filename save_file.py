from lyrics import fetchLyrics
import os


def makeFolder():
    ...

def makeDIR():
    current_dir = os.getcwd()
    new_dir = os.path.join(current_dir, r"Lyrics_data")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)


def saveToFile(url):
    makeDIR()
    title, lyrics_text = fetchLyrics(url)

    cd = os.getcwd()
    text_file = open(f"{cd}\\Lyrics_data\\{title}.txt", "w", encoding = "utf-8")
    text_file.write(lyrics_text)
    text_file.close()
    
    print("Creating file ... ")
    print(f"Lyrics file <<{title}>> Successfully created !!")
