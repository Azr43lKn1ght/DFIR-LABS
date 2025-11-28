import sys, json, hashlib
from random import randint


banner = """                                                                                                                                                                
██╗      ██████╗ ███████╗████████╗    ██╗███╗   ██╗    ██████╗  ██████╗ ██╗   ██╗████████╗███████╗██████╗ 
██║     ██╔═══██╗██╔════╝╚══██╔══╝    ██║████╗  ██║    ██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║███████╗   ██║       ██║██╔██╗ ██║    ██████╔╝██║   ██║██║   ██║   ██║   █████╗  ██████╔╝
██║     ██║   ██║╚════██║   ██║       ██║██║╚██╗██║    ██╔══██╗██║   ██║██║   ██║   ██║   ██╔══╝  ██╔══██╗
███████╗╚██████╔╝███████║   ██║       ██║██║ ╚████║    ██║  ██║╚██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║
╚══════╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                             
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
                "What is the OS version of the router?  ",
                "24.10.2",
    )
    askQn(
         "2",
                "What is the IP address of the attacker's machine?",
                "114.51.41.91",
    )
    askQn(
        "3",
                "What is the CVE number of the vulnerability exploited by the attacker?",
                "CVE‑2025‑32463",
    )
    askQn(
       "4",
                "What program's configuration was modify by the attacker to do persistence?",
                "rsyncd",
    )
    askQn(
        "5",
                "What is the host hijacked by the attacker?",
                "dashboard.company.com",
    )
    askQn(
        "6",
                "What host did the attacker use to host malicious artifacts? ",
                "foo-bar-deadbe.varcel.app",
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
