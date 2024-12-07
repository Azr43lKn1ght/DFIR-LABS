import sys, json, hashlib
from random import randint


banner = """
 ▄▄ •       ▄▄▄▄▄ ▄ .▄ ▄▄▄· • ▌ ▄ ·.     ▄• ▄▌ ▐ ▄ ·▄▄▄▄  ▄▄▄ .▄▄▄   ▄▄ • ▄▄▄        ▄• ▄▌ ▐ ▄ ·▄▄▄▄  
▐█ ▀ ▪▪     •██  ██▪▐█▐█ ▀█ ·██ ▐███▪    █▪██▌•█▌▐███▪ ██ ▀▄.▀·▀▄ █·▐█ ▀ ▪▀▄ █·▪     █▪██▌•█▌▐███▪ ██ 
▄█ ▀█▄ ▄█▀▄  ▐█.▪██▀▐█▄█▀▀█ ▐█ ▌▐▌▐█·    █▌▐█▌▐█▐▐▌▐█· ▐█▌▐▀▀▪▄▐▀▀▄ ▄█ ▀█▄▐▀▀▄  ▄█▀▄ █▌▐█▌▐█▐▐▌▐█· ▐█▌
▐█▄▪▐█▐█▌.▐▌ ▐█▌·██▌▐▀▐█ ▪▐▌██ ██▌▐█▌    ▐█▄█▌██▐█▌██. ██ ▐█▄▄▌▐█•█▌▐█▄▪▐█▐█•█▌▐█▌.▐▌▐█▄█▌██▐█▌██. ██ 
·▀▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀▀ · ▀  ▀ ▀▀  █▪▀▀▀     ▀▀▀ ▀▀ █▪▀▀▀▀▀•  ▀▀▀ .▀  ▀·▀▀▀▀ .▀  ▀ ▀█▄▀▪ ▀▀▀ ▀▀ █▪▀▀▀▀▀• 
                                                                     
"""


with open("answers.json", "r") as ansFile:
    answers = json.load(ansFile)

scoreboard = []

print(banner)


def sanitize(inpString):
    inpString = str(inpString).strip()
    return inpString


def askQn(number, question, format):
    global scoreboard

    print(f"Q{number}) {question}")
    
    print(f"Format: {format}")

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
    
    print("""For each answer:
    - Separate values using an underscore (_).
    - Arrange them in alphabetical order.
    - Follow the specified flag format.
""")

    # ----- ask qns here -----
    askQn(
        "1",
        "Which files were normally deleted?",
        "file_file",
    )

    askQn(
        "2",
        "Which files were permanently deleted?",
        "file_file",
    )
    
    askQn(
        "3",
        "Identify the files that were renamed, along with their new names.",
        "originalFile1_newNameFile1_originalFile2_newNameFile2",
    )
    

        
    # ----- end qns -----

    printFlag = True
    for i in scoreboard:
        printFlag and i


    if printFlag:
        print(answers["flag"])


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Something went wrong!\nExiting...")
        sys.exit()
