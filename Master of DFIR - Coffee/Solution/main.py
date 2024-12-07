import sys, json, hashlib
from random import randint


banner = """
   _____       __  __          
  / ____|     / _|/ _|         
 | |     ___ | |_| |_ ___  ___ 
 | |    / _ \|  _|  _/ _ \/ _ \\
 | |___| (_) | | | ||  __/  __/
  \_____\___/|_| |_| \___|\___|
                                                                     
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
        """(1). What is the victim hostname(not server)? Example: DESKTOP-J6QZVBD
(2). What is the victim's operating system version(not server)? Refer to the C2 echo. Example: Microsoft Windows 7 Professional Edition""",
        "task1_task 2",
    )

    askQn(
        "2",
        """(1). What is the ClientId of the control end? Example: c723d01b-5dc1-2601
(2). What is the systemId of the victim host? Example: 1b0679be72ad976ad5d491ad57a5eec0""",
        "task1_task2",
    )
    
    askQn(
        "3",
        """(1). What is the name of the file downloaded by the attacker(using RAT)? Example: flag.txt
(2). What is the name of the cloud service running on the intranet? Example: Kingsoft Cloud""",
        "task1_task 2",
    )
    
    askQn(
        "4",
        "What is the username and password for tomcat?",
        "Example:admin:admin",
    )

    askQn(
        "5",
        """(1). What is the path of the webshell? Example: /memshell/favicon.ico
(2). What is the file name uploaded by the attacker? Example: flag.txt""",
        "task1_task2",
    )
    
    askQn(
        "6",
        """(1). What is the key of the encryption algorithm in webshell? If there are multiple keys, connect them in the encryption order. Example: keya_keyb
(2). What is the webshell management tool used by hackers? (Note: all lowercase) Example: antsword""",
        "task1_task2",
    )

    askQn(
        "7",
        """(1). What is the administrator account and password of the cloud storage service that was stolen by hackers? Example:admin:admin
(2). What is the malicious file that the attacker uploaded through the webshell? Example: malware.exe""",
        "task1_task2",
    )
    
    askQn(
        "8",
        """(1). What is the name of the scheduled task set by the malicious script? Example: Miner
(2). What is the file where the mining program is located? Example: miner.exe""",
        "task 1_task2",
    )
      
    askQn(
        "9",
        "What is the mining pool domain name that the mining program connects back to?",
        "Example: www.baidu.com",
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
