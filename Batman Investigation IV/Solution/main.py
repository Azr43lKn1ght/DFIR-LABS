import sys, json, hashlib
from random import randint


banner = """
▄▄▄█████▓ ██░ ██ ▓█████     ██▓    ▄▄▄        ██████ ▄▄▄█████▓    ▄▄▄██▀▀▀▒█████   ██ ▄█▀▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒   ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒      ▒██  ▒██▒  ██▒ ██▄█▒ ▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░   ▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░      ░██  ▒██░  ██▒▓███▄░ ▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██░   ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░    ▓██▄██▓ ▒██   ██░▓██ █▄ ▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░██████▒▓█   ▓██▒▒██████▒▒  ▒██▒ ░     ▓███▒  ░ ████▓▒░▒██▒ █▄░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░       ▒▓▒▒░  ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░    ░        ▒ ░▒░    ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░
  ░       ░  ░░ ░   ░        ░ ░    ░   ▒   ░  ░  ░    ░          ░ ░ ░  ░ ░ ░ ▒  ░ ░░ ░    ░   
          ░  ░  ░   ░  ░       ░  ░     ░  ░      ░               ░   ░      ░ ░  ░  ░      ░  ░
"""

with open("answers.json", "r") as ansFile:
    answers = json.load(ansFile)

scoreboard = []

print(banner)


def sanitize(inpString):
    inpString = str(inpString).strip()
    inpString = inpString.replace(" ", "")
    return inpString


def askQn(number, question, format):
    global scoreboard

    print(f"Q{number}) {question}")

    print(f"Format: {format}\n")

    answer = sanitize(input("Answer: "))

    if (
        hashlib.md5(answer.encode()).hexdigest()
        == hashlib.md5(answers[number].encode()).hexdigest()
    ):
        print("Correct!\n")
        scoreboard.append(True)
    else:
        print("Wrong answer!\nExiting...")
        sys.exit()


def main():
    global scoreboard

    # ----- ask qns here -----
    askQn(
        "1",
        "What is the day and time that the infection was started?",
        "yyyy:mm:dd_hh:mm",
    )
    askQn(
        "2",
        "There are encrypted files, what is the algorithm used to encrypt them and what files store the decryption vectors?",
        "algorithm-used_filename",
    )
    askQn(
        "3",
        "what is the file that initialsed the infection?",
        "filename_md5(file)",
    )
    askQn(
        "4",
        "what is the file that further spreads the infection and what is it packed with?",
        "filename_md5(file)_packer-name(all-lowercase)",
    )
    askQn(
        "5",
        "Given a string TH8r463H0D8O0C6enNPC, use the same algorithm of the above file that it used on the urls and give the hash?",
        "md5(answer)",
    )
    askQn(
        "6",
        "How is the further spreading done, give the technique, the file that does it and file that does further infection?",
        "malware-technique(all-lowercase)_md5(file-that-does-it)_md5(file-that-does-further-infection)",
    )
    askQn(
        "7",
        "What all files are dropped by the infector?",
        "md5(files) seperated by underscores",
    )
    askQn(
        "8",
        "Where is the credit card information that gets stolen sent (isn't the cat cute?)?",
        "ip:port",
    )
    askQn(
        "9",
        "What is the file that had to set up persistence and what is the secret string that does through encryption?",
        "filename_md5(file)_md5(decrypted-secret-string)",
    )
    askQn(
        "10",
        "What is the C2 framework used, and what is the file name of the executable, what is the sleep technique used?",
        "C2-framework(all-lowercase)_executable-name_sleep-technique(case-sensitive)",
    )

    # ----- end qns -----

    printFlag = True
    for i in scoreboard:
        printFlag and i

    if printFlag:
        print(answers["flag"])
    else:
        print("Try again!\nExiting...")
        sys.exit()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Something went wrong!\nExiting...")
        sys.exit()
