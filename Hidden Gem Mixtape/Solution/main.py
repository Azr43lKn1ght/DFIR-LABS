import sys, json, hashlib
from random import randint


banner = """

██╗  ██╗██╗██████╗ ██████╗ ███████╗███╗   ██╗     ██████╗ ███████╗███╗   ███╗        ███╗   ███╗██╗██╗  ██╗████████╗ █████╗ ██████╗ ███████╗
██║  ██║██║██╔══██╗██╔══██╗██╔════╝████╗  ██║    ██╔════╝ ██╔════╝████╗ ████║        ████╗ ████║██║╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
███████║██║██║  ██║██║  ██║█████╗  ██╔██╗ ██║    ██║  ███╗█████╗  ██╔████╔██║        ██╔████╔██║██║ ╚███╔╝    ██║   ███████║██████╔╝█████╗  
██╔══██║██║██║  ██║██║  ██║██╔══╝  ██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╔╝██║        ██║╚██╔╝██║██║ ██╔██╗    ██║   ██╔══██║██╔═══╝ ██╔══╝  
██║  ██║██║██████╔╝██████╔╝███████╗██║ ╚████║    ╚██████╔╝███████╗██║ ╚═╝ ██║        ██║ ╚═╝ ██║██║██╔╝ ██╗   ██║   ██║  ██║██║     ███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝     ╚═╝        ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚══════╝                                                           
 
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
        "We managed to do a logical acquisition of data from his hard drive. However, when we open the document file, it looks empty, can you analyze what it contains?",
        "idek{...}",
    )
    askQn(
        "2",
        "We suspect multiple accounts were compromised. The attacker moved laterally. Therefore, the credentials that he used to move laterally must have leaked. Let's analyze the sequence of actions taken by the attacker and tell us what he has obtained for later purposes? Note: The flag is wrapped and divided into 2 parts",
        "idek{...}",
    )
    askQn(
        "3",
        "We tried to collect more network data for analysis, but because of the late approach, we only had data for a short period of time before we detected the attack and performed a shutdown of all machine at about 19:00 UTC. However I hope it can help you to answer the question whether the attacker has access to our important data?",
        "idek{...}",
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
