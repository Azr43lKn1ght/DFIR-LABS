import sys, json, hashlib
from random import randint


banner = """                                                                                                                                                                
    ░████            ░██                                                                        
   ░██               ░██                                                                        
░████████  ░██████   ░██    ░██ ░███████     ░████████   ░███████  ░██    ░██    ░██  ░███████  
   ░██          ░██  ░██   ░██ ░██    ░██    ░██    ░██ ░██    ░██ ░██    ░██    ░██ ░██        
   ░██     ░███████  ░███████  ░█████████    ░██    ░██ ░█████████  ░██  ░████  ░██   ░███████  
   ░██    ░██   ░██  ░██   ░██ ░██           ░██    ░██ ░██          ░██░██ ░██░██          ░██ 
   ░██     ░█████░██ ░██    ░██ ░███████     ░██    ░██  ░███████     ░███   ░███     ░███████                                                                                                                                                                                                                                               
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
                "What is the download link of the malware?",
                "https://google.com",
    )
    askQn(
         "2",
                "What is the md5 value of the command executed by the first stage payload of the malware?",
                "12ccb49db8dd65c66ba3d4d52b25923a",
    )
    askQn(
         "3",
                "What is the function that executes the second stage malicious payload?",
                "Function",
    )
    askQn(
        "4",
                "What is the MITRE ATT&CK ID of the technology used in the third stage?",
                "T1000.000",
    )
    askQn(
        "5",
                "What is the function that executes the third stage malicious payload?",
                "Function",
    )
    askQn(
         "6",
                "What is the algorithm and key used to decrypt the third-stage malicious payload?",
                "des_ecb_1520a0462516f96e41b2da773e209042",
    )
    askQn(
         "7",
                "What is the IP port of the malicious program to connect back to C2?",
                "127.0.0.1:1337",
    )
    askQn(
          "8",
                "What is the algorithm and key used to decrypt the traffic?",
                "des_ecb_e3db6576de86854ab3e2bebf2338c5d7b36990103069b180330f4ef2aefd1b56",
    )
    askQn(
         "9",
                "What is the md5 value of the executed powershell code?",
                "12ccb49db8dd65c66ba3d4d52b25923a",
    )
    askQn(
         "10",
                "What is the name of the scheduled task created by the attacker?",
                "AutoShutdown",
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
