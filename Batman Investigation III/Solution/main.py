import sys, json, hashlib
from random import randint


banner = """
 ███████████ █████                   █████████                                         █████                ██████       █████████                                           ████ 
░█░░░███░░░█░░███                   ███░░░░░███                                       ░░███                ███░░███     ███░░░░░███                                         ░░███ 
░   ░███  ░  ░███████    ██████    ░███    ░░░  █████ ███ █████  ██████  ████████   ███████      ██████   ░███ ░░░     ░███    ░███   █████████ ████████   ██████    ██████  ░███ 
    ░███     ░███░░███  ███░░███   ░░█████████ ░░███ ░███░░███  ███░░███░░███░░███ ███░░███     ███░░███ ███████       ░███████████  ░█░░░░███ ░░███░░███ ░░░░░███  ███░░███ ░███ 
    ░███     ░███ ░███ ░███████     ░░░░░░░░███ ░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███    ░███ ░███░░░███░        ░███░░░░░███  ░   ███░   ░███ ░░░   ███████ ░███████  ░███ 
    ░███     ░███ ░███ ░███░░░      ███    ░███ ░░███████████  ░███ ░███ ░███     ░███ ░███    ░███ ░███  ░███         ░███    ░███    ███░   █ ░███      ███░░███ ░███░░░   ░███ 
    █████    ████ █████░░██████    ░░█████████   ░░████░████   ░░██████  █████    ░░████████   ░░██████   █████        █████   █████  █████████ █████    ░░████████░░██████  █████
   ░░░░░    ░░░░ ░░░░░  ░░░░░░      ░░░░░░░░░     ░░░░ ░░░░     ░░░░░░  ░░░░░      ░░░░░░░░     ░░░░░░   ░░░░░        ░░░░░   ░░░░░  ░░░░░░░░░ ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░░                             
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
        "What is the PC name and timezone?",
        "PC-name_Time-Zone-info",
    )
    askQn(
        "2",
        "What is the name and hash of the initial infection file that drops the main malware?",
        "Name_md5(file)",
    )
    askQn(
        "3",
        "What is the name and hash of the main infection file?",
        "Name_md5(file)",
    )
    askQn(
        "4",
        "When did the main infection file run?",
        "DD-MM-YYYY-HH-MM",
    )
    askQn(
        "5",
        "What is the ip and port the malware is sending the decryption essential to?",
        "ip:port",
    )
    askQn(
        "6",
        "What is the nonce required to decrypt all the files affected by the ransomware?",
        "md5(nonce)",
    )
    askQn(
        "7",
        "What is the password noted down of the site he tried to access and what is stored in the site?",
        "md5(password)_md5(data-in-the-site)",
    )
    askQn(
        "8",
        "What is the email and password for his traboda login?",
        "email_password",
    )
    askQn(
        "9",
        "What is the suspicious hidden text in the QR?",
        "md5(text)",
    )
    askQn(
        "10",
        "What is the hidden text in the MP4?",
        "md5(text)",
    )
    askQn(
        "11",
        "What is the hidden text in the AVI file?",
        "md5(text)",
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
