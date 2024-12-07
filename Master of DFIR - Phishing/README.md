# Master of DFIR - Phishing(🎣)

## Difficulty: `Hard`

```
  _____  _     _     _     _             
 |  __ \| |   (_)   | |   (_)            
 | |__) | |__  _ ___| |__  _ _ __   __ _ 
 |  ___/| '_ \| / __| '_ \| | '_ \ / _` |
 | |    | | | | \__ \ | | | | | | | (_| |
 |_|    |_| |_|_|___/_| |_|_|_| |_|\__, |
                                    __/ |
                                   |___/ 

```

### Challenge Description

饥渴C猫是一个刚刚入职的员工，但是最近他发现自己的电脑变得越来越奇怪。可能由于是之前他接受的一封奇怪的邮件，于是饥渴C猫找到了你,他希望你作为取证-应急响应大师可以帮忙。你可以完成调查到底发生了什么并且填写相关的调查报告。

GeekCmore is a new employee who recently noticed that his computer has been acting strangely. It might be due to a strange email he received earlier, so GeekCmore turned to you for help. He hopes that, as a forensics and incident response expert, you can assist him in investigating what happened and completing the related investigation report.


**Challenge File**:

handout.zip 

**MD5 Hash**: 

`257aba697f91196d06dfd80c29138a9d  handout.zip`

### Author

- [crazyman](https://github.com/crazymanarmy)
- [F0rest](https://github.com/silence-forest-sf)
- [yuro](https://github.com/yurogod)

### Questions 

you can either directly answer it or you can solve the challenge by running main.py in Solution folder and answering it.

```
task1:
(1).What is the attacker's email address? (Note: MD5 (attacker's email address) is based on cyberchef's) Example: 9b04d152845ec0a378394003c96da594
(2).What is the victim's email address? (Note: MD5 (victim's email address) is based on cyberchef's) Example: 9b04d152845ec0a378394003c96da594

task2:
(1).What is the md5 of the file dropped by the attacker? (Note: the result of md5sum shall prevail) Example: 33ec9f546665aec46947dca16646d48e
(2).What is the password of the file dropped by the attacker? Example: 000nb

task3:
(1). What is the suffix of the attack payload used by the attacker? Example: lnk
(2). What is the full name of the default way to open the attack payload file used by the attacker? Example: Microsoft Windows Based Scripting Host

task4:
On which line of the attack payload file is the initial execution statement of the sample dropped by the attacker? Example: 20

task5:
After the initial execution, what language is used by the attacker to load the second payload? Example: javascript

task6:
(1). Where does the attacker store the second part of the payload? (Note: You need to provide the parameters of the s*******s  function of the second part of the payload after deobfuscation) Submission requires MD5 (parameter content) Subject to the Cyberchef result Example: 9b04d152845ec0a378394003c96da594
(2). Where does the attacker store the black DLL in the second part of the payload? (Note: You need to provide the parameters of the s*******s function of the second part of the payload after deobfuscation) Submission requires MD5 (parameter content) Subject to the Cyberchef result Example: 9b04d152845ec0a378394003c96da594

task7:
What is the MITRE ATT&CK ID for the signed EXE used by the attacker to load the mal DLL? (Note: Please note that the example prompts that you only need to submit the general category without breaking it down into sub-items) Example: T1000

task8:
Which function of the original DLL does the mal DLL used by the attacker hijack? Example: main

task9:
(1).What is the algorithm used by the mal DLL used by the attacker to decrypt the next stage payload? Example: chacha20
(2). What is the key used by the mal DLL used by the attacker to decrypt the next stage payload? (Note: Please submit a lowercase hexadecimal string) Example: 1122334455

task10:
What is the C2 connection back to the next stage payload used by the attacker? (Note: You need to provide the IP address: port format) Example: 127.0.0.1:5100

task11:
What encryption algorithm is used by the attacker to send the final stage payload? Example: DES

task12:
What is the MD5 of the key used by the attacker in the final stage payload(RAT)? (Note: MD5 (key content), subject to cyberchef) Example: 9b04d152845ec0a378394003c96da594

task13:
What family of C2 did the attacker use? Example: PoshC2 
```

### Author

- [crazyman](https://github.com/crazymanarmy)
- [F0rest](https://github.com/silence-forest-sf)
- [yuro](https://github.com/yurogod)

### Solution

The solution as well as the flag can be found in the same folder, but it's advised to finish all the questions before checking the solution.

### Contact

[Azr43lKn1ght](https://twitter.com/Azr43lKn1ght)

Chief Maintainer and Author

DFIR Labs