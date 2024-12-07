import sys, json, hashlib
from random import randint


banner = """
  _____  _     _     _     _             
 |  __ \| |   (_)   | |   (_)            
 | |__) | |__  _ ___| |__  _ _ __   __ _ 
 |  ___/| '_ \| / __| '_ \| | '_ \ / _` |
 | |    | | | | \__ \ | | | | | | | (_| |
 |_|    |_| |_|_|___/_| |_|_|_| |_|\__, |
                                    __/ |
                                   |___/                             
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
        == answers[number]
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
        """(1).What is the attacker's email address? (Note: MD5 (attacker's email address) is based on cyberchef's) Example: 9b04d152845ec0a378394003c96da594
(2).What is the victim's email address? (Note: MD5 (victim's email address) is based on cyberchef's) Example: 9b04d152845ec0a378394003c96da594""",
        "task1_task2",
    )

    askQn(
        "2",
        """(1).What is the md5 of the file dropped by the attacker? (Note: the result of md5sum shall prevail) Example: 33ec9f546665aec46947dca16646d48e
(2).What is the password of the file dropped by the attacker? Example: 000nb""",
        "task1_task2",
    )
    
    askQn(
        "3",
        """(1). What is the suffix of the attack payload used by the attacker? Example: lnk
(2). What is the full name of the default way to open the attack payload file used by the attacker? Example: Microsoft Windows Based Scripting Host""",
        "task1_task 2",
    )
    
    askQn(
        "4",
        "On which line of the attack payload file is the initial execution statement of the sample dropped by the attacker?",
        "Example: 20",
    )

    askQn(
        "5",
        """After the initial execution, what language is used by the attacker to load the second payload?""",
        "Example: javascript",
    )
    
    askQn(
        "6",
        """(1). Where does the attacker store the second part of the payload? (Note: You need to provide the parameters of the s*******s  function of the second part of the payload after deobfuscation) Submission requires MD5 (parameter content) Subject to the Cyberchef result Example: 9b04d152845ec0a378394003c96da594
(2). Where does the attacker store the black DLL in the second part of the payload? (Note: You need to provide the parameters of the s*******s function of the second part of the payload after deobfuscation) Submission requires MD5 (parameter content) Subject to the Cyberchef result Example: 9b04d152845ec0a378394003c96da594""",
        "task1_task2",
    )

    askQn(
        "7",
        """What is the MITRE ATT&CK ID for the signed EXE used by the attacker to load the mal DLL? (Note: Please note that the example prompts that you only need to submit the general category without breaking it down into sub-items)""",
        "Example: T1000",
    )
    
    askQn(
        "8",
        """Which function of the original DLL does the mal DLL used by the attacker hijack?""",
        "Example: main",
    )
      
    askQn(
        "9",
        """(1).What is the algorithm used by the mal DLL used by the attacker to decrypt the next stage payload? Example: chacha20
(2). What is the key used by the mal DLL used by the attacker to decrypt the next stage payload? (Note: Please submit a lowercase hexadecimal string) Example: 1122334455""",
        "task1_task2",
    )
    
    askQn(
        "10",
        """What is the C2 connection back to the next stage payload used by the attacker? (Note: You need to provide the IP address: port format)""",
        "Example: 127.0.0.1:5100",
    )
    
    askQn(
        "11",
        """What encryption algorithm is used by the attacker to send the final stage payload?""",
        "Example: DES",
    )
   
    askQn(
        "12",
        """What is the MD5 of the key used by the attacker in the final stage payload(RAT)? (Note: MD5 (key content), subject to cyberchef)""",
        "Example: 9b04d152845ec0a378394003c96da594",
    ) 
    
    askQn(
        "13",
        """What family of C2 did the attacker use?""",
        "Example: PoshC2",
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
