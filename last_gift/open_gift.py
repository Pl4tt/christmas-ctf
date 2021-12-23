import os
from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm


HOME_DIR = Path(__file__).resolve().parent


def brute_force_dict(dictionary, zip_file):
    """brute forces all words in the dictionary until it
    finds the right password for the zip_file"""
    with (
        ZipFile(zip_file) as gift,
        open(dictionary, "rb") as wordlist
        ):

        wordlen = len(list(open(dictionary, "rb")))
        print(f"Total words in wordlist: {wordlen}")
            

        for word in tqdm(wordlist, total=wordlen, unit="word"):
            try:
                gift.extractall(path=HOME_DIR, pwd=word.strip())
                print(f"\n[!] password found: {word.decode().strip()}")
                break
            except Exception:
                continue

def logical_dict_attack(dictionary, zip_file):
    """filters out all passwords in the dictionary that have a
    length of 96 (because we know the length of the password is 96)
    and unpacks the zip_file by trying all of that passwords"""

    words = list(open(dictionary, "rb"))
    words = list(filter(lambda word: len(word) == 97, words))  # 97 because of \n at end of line
    words = list(map(lambda word: word.strip(), words))

    print(f"Total Words with length 96: {len(words)}")
    
    with ZipFile(zip_file) as gift:
        for word in tqdm(words, total=len(words), unit="word"):
            try:
                gift.extractall(path=HOME_DIR, pwd=word.strip())
                print(f"\n[!] password found: {word.decode().strip()}")
                break
            except Exception:
                continue


if __name__ == "__main__":
    word_list = os.path.join(HOME_DIR, "rockyou.txt")
    zip_file = os.path.join(HOME_DIR, "geschenk.zip")

    logical_dict_attack(word_list, zip_file)