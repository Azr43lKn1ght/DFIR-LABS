from ans import Answers
import hashlib 



MAX_POINTS = 6

questions = [
"Question 1 : List all directories that have been renamed, including their original names and the timestamps of when they were renamed.\nTimeZone - UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]\n \
Format - [ ['OriginalDirName', 'RenamedDirName', 'TimeStamp'] , .. ]"
,

"Question 2 : Name all the deleted directories with deletion timestamps.\nTimeZone : UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]\n Format - [ ['DirectoryName' , 'TimeStamp'] , .. ]"
,

"Question 3 : List all directories with their creation times, including originals if any that has been renamed or deleted. (Note : If a directory was renamed, include its original name and creation time.)\nTimeZone : UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]\n Format - [ ['DirectoryName' , 'CreatedTime'] , .... ]"
,

"Question 4 : Recover the files that have been deleted, and provide the md5sum of each recovered file.\nFormat - [ ['filehash1'] , ['filehash2'], ... ]"
,

"Question 5 : Identify all files that have been deleted (Simple + Permanent), including their deletion timestamps.\nTimeZone : UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]\nFormat - [ [ 'filename' , 'TimeStamp' , 'Simple/Permanent' ] , .. ]"
,

"Question 6: Restore all encrypted files, decrypt them, and provide the md5sum of each decrypted file after removing any extra bytes before computing the hash.\n Format - [ ['hash1'] , ['hash2'], ',..] "

]

Answers = Answers.hashes

def isAllAnsweredCorrectly(i, score_board):
    if i==MAX_POINTS:
        for _ in score_board:
            if _ == False: return False
        return True 
    else:
        return False

def checkAns(ans, i):
    if Answers[i] == ans:
        return True 
    return False

def getflag():
    return "Flag: bi0sctf{ReAL_1_w0nd3r_wHa7_t1m3_is_17_14dbc653fdb414c1d}"

def check_ans(question, i):
    final_hashes = []
    question.sort()
    for sublist in question:
        sublist.sort()
        concatenated_string = ''.join(sublist)
        hashed_result = hashlib.sha256(concatenated_string.encode()).hexdigest()
        final_hashes.append(hashed_result)
    final_hashes.sort()
    concatenated_hashes = ''.join(final_hashes)
    final_hash = hashlib.sha256(concatenated_hashes.encode()).hexdigest()
    status = checkAns(final_hash, i)
    return status


def run():
    score_board = [False] * 6 
    count = 0
    while(count<6):
        print(questions[count])
        inp_ans = input("-> ")
        try:
            ans = eval(inp_ans)
            if (isinstance(ans, list) and (all(isinstance(item, list) for item in ans ))):
                res = check_ans(ans, count)
                if res:
                    print(f"Correct :) \n")
                    score_board[count] = True 
                    count+=1
                    check = isAllAnsweredCorrectly(count, score_board)
                    if check:
                        print("." *70)
                        print(getflag())
                        print("." *70)
                        break
                else:
                    print("Wrong Answer!!\n")
                    break
        except Exception :
            print("Wrong Format!!\n")
            break


if __name__ == "__main__":
    run()