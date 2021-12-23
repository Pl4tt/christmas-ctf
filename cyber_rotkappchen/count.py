import os
from pathlib import Path


HOME_DIR = Path(__file__).resolve().parent


def read_code(filename, target):
    cybers, ones, zeros = 0, 0, 0

    with open(filename, "r") as file:
        for line in file.readlines():
            for word in line.split(" "):
                if "cyber-" in word.lower():
                    ones += 1
                    cybers += 1
                    append_char(target, 1)
                elif "cyber" in word.lower():
                    zeros += 1
                    cybers += 1
                    append_char(target, 0)
        
    append_char(target, "\n")
    return cybers, ones, zeros

def to_bit_list(txt):
    ret_list = []
    last = 0

    for i in range(len(txt)):
        if i%8 == 0:
            ret_list.append(txt[last:i])
            last = i
    
    ret_list.append(txt[last:len(txt)])

    return ret_list[1:]

def to_ascii(bits):
    result = ""
    
    for bit in bits:
        result += chr(int(bit, 2))

    return result

def append_char(filename, char):
    with open(filename, "a") as file:
        file.write(str(char))

def convert_text(filename, target):
    read_code(filename, target)
    
    with open(target) as file:
        binary = file.readlines()[0].replace("\n", "")
        bits = to_bit_list(binary)
        ascii_chars = to_ascii(bits)
    
    return ascii_chars


if __name__ == "__main__":
    story_file = os.path.join(HOME_DIR, "story.txt")
    target_file = os.path.join(HOME_DIR, "target_code.txt")
    
    code = convert_text(story_file, target_file)
    append_char(f"{HOME_DIR}/target_code.txt", code+"\n")
    