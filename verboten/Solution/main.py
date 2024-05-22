import sys, json, hashlib
from random import randint


banner = """
██╗   ██╗███████╗██████╗ ██████╗  ██████╗ ████████╗███████╗███╗   ██╗
██║   ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝████╗  ██║
██║   ██║█████╗  ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██╔██╗ ██║
╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██║╚██╗██║
 ╚████╔╝ ███████╗██║  ██║██████╔╝╚██████╔╝   ██║   ███████╗██║ ╚████║
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═══╝
                                                                     
"""



with open("answers.json", "r") as ansFile:
    answers = json.load(ansFile)

scoreboard = []
finalAnswer = ""

print(banner)


def sanitize(inpString):
    inpString = str(inpString).strip()
    inpString = inpString.replace(" ", "")
    return inpString


def askQn(number, question, format):
    global scoreboard, finalAnswer

    print(f"Q{number}) {question}")

    print(f"Format: {format}\n")

    answer = sanitize(input("Answer: "))

    if (
        hashlib.md5(answer.encode()).hexdigest()
        == hashlib.md5(answers[number].encode()).hexdigest()
    ):
        finalAnswer += answer
        print("Correct!\n")
        scoreboard.append(True)
    else:
        print("Wrong answer!\nExiting...")
        sys.exit()


def main():
    global scoreboard, finalAnswer

    # ----- ask qns here -----
    askQn(
        "1",
        "What is the serial number of the sandisk usb that he plugged into the system? And when did he plug it into the system?",
        "verboten{serial_number:YYYY-MM-DD-HH-MM-SS}",
    )
    askQn(
        "2",
        "What is the hash of the url from which the executable in the usb downloaded the malware from?",
        "verboten{md5(url)}",
    )
    askQn(
        "3",
        "What is the hash of the malware that the executable in the usb downloaded which persisted even after the efforts to remove the malware?",
        "verboten{md5{malware_executable)}",
    )
    askQn(
        "4",
        "What is the hash of the zip file and the invite address of the remote desktop that was sent through slack?",
        "verboten{md5(zip_file):invite_address}",
    )
    askQn(
        "5",
        "What is the hash of all the files that were synced to Google Drive before it was shredded?",
        "verboten{md5 of each file separated by ':'}",
    )
    askQn(
        "6",
        "What is time of the incoming connection on AnyDesk? And what is the ID of user from which the connection is requested?",
        "verboten{YYYY-MM-DD-HH-MM-SS:user_id}",
    )
    askQn(
        "7",
        "When was the shredder executed?",
        "verboten{YYYY-MM-DD-HH-MM-SS}",
    )
    askQn(
        "8",
        "What are the answers of the backup questions for resetting the windows password?",
        "verboten{answer_1:answer_2:answer_3}",
    )
    askQn(
        "9",
        "What is the single use code that he copied into the clipboard and when did he copy it?",
        "verboten{single_use_code:YYYY-MM-DD-HH-MM-SS}",
    )

    # ----- end qns -----

    printFlag = True
    for i in scoreboard:
        printFlag and i


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Something went wrong!\nExiting...")
        sys.exit()
