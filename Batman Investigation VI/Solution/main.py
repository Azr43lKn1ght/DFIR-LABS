import sys, json, hashlib
from random import randint


banner = """                                                                                                                                                                
██████╗ ███████╗ █████╗ ████████╗██╗  ██╗    ████████╗ ██████╗      █████╗ ███████╗██████╗  █████╗ ███████╗██╗     
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗╚══███╔╝██╔══██╗██╔══██╗██╔════╝██║     
██║  ██║█████╗  ███████║   ██║   ███████║       ██║   ██║   ██║    ███████║  ███╔╝ ██████╔╝███████║█████╗  ██║     
██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║       ██║   ██║   ██║    ██╔══██║ ███╔╝  ██╔══██╗██╔══██║██╔══╝  ██║     
██████╔╝███████╗██║  ██║   ██║   ██║  ██║       ██║   ╚██████╔╝    ██║  ██║███████╗██║  ██║██║  ██║███████╗███████╗
╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝       ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝     


Note: Use hex lowercase for all hex values and no spaces in between unless specified otherwise.                                                                                                                                                                         
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
        "What is th pid of netd service and inode of the file rt_tables and laberl for its routing table number 1010? ",
        "pid-inode-label",
    )
    askQn(
        "2",
        "What is the inode, content encryption mode(int), name encryption mode(int) of DCIM folder?",
        "inode-contentmode(int)-filenamemode(int)",
    )
    askQn(
        "3",
        "What is the folder modified UTC time(yyyy-mm-dd_hh:mm:ss), File based encryption key descriptor(hex) and nonce(hex) of DCIM folder (hex all caps no space)?",
        "time(yyyy-mm-dd_hh:mm:ss)-keydescriptor(hex)-nonce(hex)",
    )
    askQn(
        "4",
        "give all the File Based Encryption masterkeys in the order of most hits",
        "descriptor1keypart1:descriptor1keypart2-descriptor2keypart1:descriptor2keypart2-....",
    )
    askQn(
        "5",
        "what is the Derived Encryption Key(DEK) after Key Decryption function for decryption of DCIM folder name?",
        "key(hex)",
    )
    askQn(
        "6",
        "Which are/is the unedited image file(s) in the DCIM folder? also give md5sum of the file(s).",
        "name1_md5sum1-name2_md5sum2-...",
    )
    askQn(
        "7",
        "What is the 7th tweak value passed as IV for decryption of the above mentioned file's content decryption?",
        "tweak(hex)",
    )
    askQn(
        "8",
        "What is the saved contact name, number and email address?",
        "name_number(only numbers)_email",
    )
    askQn(
        "9",
        "What is the important message code sent to the contact?",
        "code",
    )
    askQn(
        "10",
        "What is the private messenger used, its database decryption key and user address?",
        "messenger(primary name only)-decryptionkey(hex)-address",
    )
    askQn(
        "11",
        "What is the user address who was contacted in the private messenger and what was the important code sent?",
        "address_code",
    )
    askQn(
        "12",
        "What is the first and second visited sites in browser(add https and omit the last '/' and google)?",
        "site1-site2",
    )
    askQn(
        "13",
        "What is the malware package name and its apk md5 hash?",
        "packagename(com.example.malware)-md5(apk)",
    )
    askQn(
        "14",
        "Identify malware family label and its version code.",
        "Family.Label-versioncode",
    )
    askQn(
        "15",
        "when was the malware installed? time in UTC",
        "time(yyyy-mm-dd_hh:mm:ss)",
    )
    askQn(
        "16",
        "What is the malware client name, host, port and key?",
        "clientname-host-port-key",
    )
    askQn(
        "17",
        "The attacker made a call from the device. What is the phone number, time and duration of the call?",
        "number-time(yyyy-mm-dd_hh:mm:ss)-duration(seconds)",
    )
    askQn(
        "18",
        "what is the name of the dropped ransomware, its md5 hash and when was it installed(time in UTC)?",
        "packagename(com.example.ransomware)_md5hash_time(yyyy-mm-dd_hh:mm:ss)",
    )
    askQn(
        "19",
        "what is the ransomware key file name and key?",
        "keyfile(keyfilename)-key",
    )
    askQn(
        "20",
        "what is the decrypted hash contained in one of the files (note: The ransomware was run twice, so you need to decrypt the file twice)?",
        "filename-filecontent",
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
