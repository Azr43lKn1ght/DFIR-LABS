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

    # ----- ask qns here -----
    askQn(
        "1",
        "who asked Carmine falcon to contact someone and who is falcone disguised as?",
        "disguse-name_person-contacted (all lowercase)",
    )

    askQn(
        "2",
        "what is the hash of the file that he sent him to contact",
        "sha1sum",
    )
    
    askQn(
        "3",
        "what is the password of his password manager",
        "password_manager_name_with_version:md5(password)",
    )
    
    askQn(
        "4",
        "what is the key he stored in his password manager that he deleted?",
        "(format: user_name:key)",
    )

    askQn(
        "5",
        "what is the cryptocurrency wallet installed and when is it installed?",
        "wallet_name-date-time(in format YYYY:MM:DD:HH:MM)",
    )
    
    askQn(
        "6",
        "what is the malware that wants to steal the cryptocurrency wallet and ip it's trying to send to with port number?",
        "malware_ip:port)",
    )

    askQn(
        "7",
        "Eventhough Falcone's Network Moniter blockked the file sent, falcone made sure to zip with a password and noted it down temproarily in his screen and sent it to a detective for analysis.what is the password of the zip file?",
        "md5(password)",
    )
    
    askQn(
        "8",
        "what is the hash of the original files in the zip file before the stealer modified them?",
        "sha1sum:sha1sum",
    )
      
    askQn(
        "9",
        "what is the password that Carmine Falcone protected the wallet with",
        "md5(password)",
    )

    askQn(
        "10",
        "who did Carmine falcone recive money from?",
        "name_person:curreny_used(3 or 4 letter significance):amount(in dollars with precision of 2 decimal places):transaction_id",
    )

    askQn(
        "11",
        "who did Carmine falcone send money to?",
        "name_person:curreny_used(3 or 4 letter significance):amount(in dollars with precision of 2 decimal places):addres",
    )     
    
    askQn(
        "12",
        "what is the name and client private key that Salvatore asked for contact verification?",
        "infobreakage_dbkey:client_email",
    )
    
    askQn(
        "13",
        "what is the information interpreted further from previous question",
        "name_client:private_key",
    )
    
    askQn(
        "14",
        "what is the userkey of the encrypted dbx database?",
        "userkey",
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
