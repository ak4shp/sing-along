from save_file import saveToFile
from many_links import getAllLinks


def writeLyrics(choice):
    try:
        choice = int(choice)
    except ValueError:
        print("PLEASE ENTER INTEGER ONLY !!")

    if choice == 1:
        url = input("Enter URL :  ")
        saveToFile(url)
    
    elif choice == 2:
        urls = getAllLinks()
        for url in urls:
            if url:
                saveToFile(url.strip())
    else:
        print("Please choose either  1  or  2  only !!")


if __name__ == "__main__":
    source = input("Lyrics source - (1) Gaana.com\n\t\t(2) Lyricsgram -> ")
    choice = input("\n\t(1) Direct link\n\t(2) 'links.txt' file -->  ")
    writeLyrics(choice)
    print("\n**** PROCESS COMPLETED ****")

    



