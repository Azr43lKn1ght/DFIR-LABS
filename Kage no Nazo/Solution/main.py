import sys, json, hashlib
from random import randint

banner = """
██╗  ██╗ █████╗  ██████╗ ███████╗    ███╗   ██╗ ██████╗     ███╗   ██╗ █████╗ ███████╗ ██████╗ 
██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝    ████╗  ██║██╔═══██╗    ████╗  ██║██╔══██╗╚══███╔╝██╔═══██╗
█████╔╝ ███████║██║  ███╗█████╗      ██╔██╗ ██║██║   ██║    ██╔██╗ ██║███████║  ███╔╝ ██║   ██║
██╔═██╗ ██╔══██║██║   ██║██╔══╝      ██║╚██╗██║██║   ██║    ██║╚██╗██║██╔══██║ ███╔╝  ██║   ██║
██║  ██╗██║  ██║╚██████╔╝███████╗    ██║ ╚████║╚██████╔╝    ██║ ╚████║██║  ██║███████╗╚██████╔╝
"""


with open("answers.json", "r") as ansFile:
    answers = json.load(ansFile)

scoreboard = []
finalAnswer = ""

print(banner)

def sanitize(inpString):
    inpString = str(inpString).strip().upper()
    inpString = inpString.replace(" ", "")
    return inpString

def askQn(number, question, format):
    global scoreboard, finalAnswer
    print(f"Q{number}) {question}")
    print(f"Format: {format}\n")
    answer = input("Answer: ").strip()
    method = answers[number]["method"]
    
    if method == "md5":
        correct_answer = answers[number]["answer"]
        sanitized_answer = sanitize(answer)
        if hashlib.md5(sanitized_answer.encode()).hexdigest() == hashlib.md5(correct_answer.encode()).hexdigest():
            finalAnswer += sanitized_answer
            scoreboard.append(True)
            print("Correct!\n")
        else:
            print("Wrong answer!\nExiting...")
            sys.exit()
    elif method == "mitre":
        allowed_ids = set(answers[number]["allowed_ids"])
        ids = [id.strip().upper() for id in answer.split(":")]
        if len(set(ids)) == 7 and all(id in allowed_ids for id in ids):
            finalAnswer += ":".join(ids)
            scoreboard.append(True)
            print("Correct!\n")
        else:
            print("Wrong answer! Provide 7 unique IDs.\nExiting...")
            sys.exit()
    elif method == "artifacts":
        required_words = set(answers[number]["required_words"])
        words = set(word.strip().upper() for word in answer.split(":"))
        if required_words.issubset(words):
            finalAnswer += ":".join(words)
            scoreboard.append(True)
            print("Correct!\n")
        else:
            print("Wrong answer! Must include EVENTLOGS, PREFETCH, and DEFENDER.\nExiting...")
            sys.exit()

def main():
    askQn("1", "Which link did the user use to download the malicious executable ?", "https://link")
    askQn("2", "What are the malware hashes ? (file1:file2:......) where file1, file2, ... are the hashes of the files that were downloaded from the link in Q1.", "md5(file1):md5(file2):...")
    askQn("3", "Where is the attacker sending the data to?", "ip:port")
    askQn("4", "Which installed third-party applications are targeted by the script for data extraction?", "app_1:app_2:app_3")
    askQn("5", "During the analysis of the other malware, identify the corresponding MITRE ATT&CK techniques. Use the format: Txxxx or Txxxx.xxx, including both high-level and sub-techniques as applicable.", "ID1:ID2:ID3:ID4:ID5:ID6:ID7  # any 7 will do")
    askQn("6", "Which tool did he use to get access to the system?", "tool_name")
    askQn("7", "What system traces or artifacts did the attacker attempt to clear or neutralize?", "artifact1:artifact2......")
    askQn("8", "What is the SHA1 hash of the file that was used to diable windwows defender?", "sha1_of_file")
    askQn("9", "What are the md5sum of the decrypted  confidential.pdf  and flag.png?", "md5sum_of_confidential.pdf:md5sum_of_flag.png")
    
    if all(scoreboard):
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