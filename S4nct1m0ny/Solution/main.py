import sys, json, hashlib
from random import randint


banner = """

░██████╗░░██╗██╗███╗░░██╗░█████╗░████████╗░░███╗░░███╗░░░███╗░█████╗░███╗░░██╗██╗░░░██╗
██╔════╝░██╔╝██║████╗░██║██╔══██╗╚══██╔══╝░████║░░████╗░████║██╔══██╗████╗░██║╚██╗░██╔╝
╚█████╗░██╔╝░██║██╔██╗██║██║░░╚═╝░░░██║░░░██╔██║░░██╔████╔██║██║░░██║██╔██╗██║░╚████╔╝░
░╚═══██╗███████║██║╚████║██║░░██╗░░░██║░░░╚═╝██║░░██║╚██╔╝██║██║░░██║██║╚████║░░╚██╔╝░░
██████╔╝╚════██║██║░╚███║╚█████╔╝░░░██║░░░███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║░░░██║░░░
╚═════╝░░░░░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░                                                                                                                                  
                                                                                                                                   
"""


with open("answers.json", "r") as ansFile:
    answers = json.load(ansFile)
    print(answers)

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

    if number == "1/15":
        if (
        (hashlib.md5(answer.lower().encode()).digest()
        == hashlib.md5(answers[number][0].lower().encode()).digest()) or (hashlib.md5(answer.lower().encode()).digest()
        == hashlib.md5(answers[number][1].lower().encode()).digest())
    ):
            
            print("Correct!\n")
            scoreboard.append(True)
        else:
            print("Wrong answer!\nExiting...")
            sys.exit()

    else:
        if (
            hashlib.md5(answer.lower().encode()).digest()
            == hashlib.md5(answers[number].lower().encode()).digest()
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
        "1/15",
        "What is the OS version of the compromised system?",
        "OS_version_number",
    )
    askQn(
        "2/15",
        "What is the hostname of the compromised system?",
        "hostname",
    )
    askQn(
        "3/15",
        "What is the application responsible for the initial infection of the system?",
        "Appname",
    )
    askQn(
        "4/15",
        "Which application was used to facilitate the download of the malicious application responsible for the infection?",
        "Appname",
    )
    askQn(
        "5/15",
        "What are the username and email address associated with the Flock account that sent the malicious application?",
        "Username_email",
    )
    askQn(
        "6/15",
        "What is the user name and email address of the user who advised Peter Parker to take his laptop for repair, what is the name of the recommended repair service, and in which Flock channel was this advice given?",
        "User-Name_email_Place_Channel:_Name",
    )
    askQn(
        "7/15",
        "What are the login credentials of the compromised system?",
        "username:password",
    )
    askQn(
        "8/15",
        "What is the  email  and password for Peter Parker’s iCloud account?",
        "email:password",
    )
    askQn(
        "9/15",
        "What are the master key, database key, record key, and SSGP label for the keychain record containing Peter Parker’s Gmail account credentials?",
        "masterkey_dbkey_recordkey_SSGP-label",
    )
    askQn(
        "10/15",
        "What is the name of the binary executed by the malicious application, and what is the SHA-256 hash of the binary?",
        "binaryname_binaryhash",
    )
    askQn(
        "11/15",
        "What is the IP address and port number to which the attacker established a connection from the compromised system?",
        "ipaddress:port",
    )
    askQn(
        "12/15",
        "What are the key and initialization vector (IV) used by the malicious application to decrypt its payload, and what compression method was used for the payload ?",
        "key_iv_compression",
    )
    askQn(
        "13/15",
        "At what path does the malicious application write the decrypted payload to, and what is the SHA-256 hash of the decrypted payload?",
        "/binary/path_hash",
    )
    askQn(
        "14/15",
        "What are the names of the files that have been exfiltrated by the attacker from the host?",
        "File names in ascending order, seperated by commas (eg. file_name1,file_name2,...,file_name)",
    )
    askQn(
        "15/15",
        "What is the encryption key used to secure the exfiltrated data, and what port number was used for the exfiltration process?",
        "key:port",
    )
    # ----- end qns -----

    printFlag = True
    for i in scoreboard:
        printFlag and i

    # finalAnswerHash = hashlib.md5(finalAnswer.encode()).hexdigest()
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