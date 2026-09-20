import sys, json, hashlib

with open("answers.json", "r") as f:
    answers = json.load(f)

scoreboard = []


def sanitize(s):
    return str(s).strip()


def askQn(number, question, fmt):
    global scoreboard
    print(f"Q{number}) {question}")
    print(f"Format: {fmt}\n")
    answer = sanitize(input("Answer: "))

    expected = answers[number]
    if isinstance(expected, list):
        correct = any(
            hashlib.md5(answer.lower().encode()).hexdigest() ==
            hashlib.md5(e.lower().encode()).hexdigest()
            for e in expected
        )
    else:
        correct = (
            hashlib.md5(answer.lower().encode()).hexdigest() ==
            hashlib.md5(expected.lower().encode()).hexdigest()
        )

    if correct:
        print("Correct!\n")
        scoreboard.append(True)
    else:
        print("Wrong answer!\nExiting...")
        sys.exit()


def main():
    askQn("1", "What is the password of Natsume's Windows account?",
          "password")

    askQn("2", "What is the name of the malicious executable found on Natsume's machine?",
          "filename.exe")

    askQn("3", "What password did Natsume use to extract the tool sent by the attacker?",
          "password")

    askQn("4", "What is the master encryption key used by ModCollabTool?",
          "key")

    askQn("5", "What MITRE ATT&CK technique does ModCollabTool use? (obfuscation or encryption for impact)",
          "TXXXX")

    askQn("6", "What map contains the attacker's planted artifact? (evidence.7z password: s0und_0f_a_s0ul)",
          "mXX_XX_XX_XX")

    askQn("7",
          "The attacker planted something in Gwyn's boss room. Find the collision mesh ID, "
          "boss room BGM ThinkParamID, XYZ coordinates of the model, and the map piece ID.",
          "{mesh:XXXXXX|ThinkParamID:XXXXXX|pos:X,X,X|map:mXX_XX_XX_XX}")

    if all(scoreboard):
        print(answers["flag"])
    else:
        print("Try again!\nExiting...")
        sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except Exception:
        print("Something went wrong!\nExiting...")
        sys.exit()
