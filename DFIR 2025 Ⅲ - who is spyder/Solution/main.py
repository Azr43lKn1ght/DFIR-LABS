import sys, json, hashlib
from random import randint


banner = """                                                                                                                                                                
▄▄▌ ▐ ▄▌ ▄ .▄          ▪  .▄▄ ·     .▄▄ ·  ▄▄▄· ▄· ▄▌·▄▄▄▄  ▄▄▄ .▄▄▄  
██· █▌▐███▪▐█▪         ██ ▐█ ▀.     ▐█ ▀. ▐█ ▄█▐█▪██▌██▪ ██ ▀▄.▀·▀▄ █·
██▪▐█▐▐▌██▀▐█ ▄█▀▄     ▐█·▄▀▀▀█▄    ▄▀▀▀█▄ ██▀·▐█▌▐█▪▐█· ▐█▌▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌██▌▐▀▐█▌.▐▌    ▐█▌▐█▄▪▐█    ▐█▄▪▐█▐█▪·• ▐█▀·.██. ██ ▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪▀▀▀ · ▀█▄▀▪    ▀▀▀ ▀▀▀▀      ▀▀▀▀ .▀     ▀ • ▀▀▀▀▀•  ▀▀▀ .▀  ▀                                                                                                                                                                                                                                            
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
                "Submit the PIDs of all malicious processes and hacked processes, sorted in ascending numerical order and concatenated with underscores ('_').",
                "123_456",
    )
    askQn(
         "2",
                "What is the host used by the encrypted channel?",
                "192.168.128.155",
    )
    askQn(
         "3",
                "What are the encryption algorithm, encryption mode, key, and iv used in the encrypted channel?",
                "des_cfb_d7366d6d6d9676e6_782d6d732d6d6574",
    )
    askQn(
        "4",
                "What was the file name of the content that the attacker finally attempted to obtain?",
                "hello_world",
    )
    askQn(
        "5",
                "What is the C2 infrastructure utilized by attackers to maintain persistent access? (Case-sensitive)",
                "AdaptixC2",
    )
    askQn(
         "6",
                "What is the name of the storage container used by Loki? If there are multiple containers sorted in the order of usage, concatenate them using '_' ",
                "ContainerA_ContainerB ",
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
