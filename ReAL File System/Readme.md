# ReAL File System
## Difficulty: `Hard`
```
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ _ _ __ _ _ _ _ _ _
|   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   |
|  |                                                                                         |  |
|  |       ______      ___   _       ______ _ _          _____           _                   |  |
|  |       | ___ \    / _ \ | |      |  ___(_) |        /  ___|         | |                  |  |
|  |       | |_/ /___/ /_\ \| |      | |_   _| | ___    \ `--. _   _ ___| |_ ___ _ __ ___    |  |
|  |       |    // _ \  _  || |      |  _| | | |/ _ \    `--. \ | | / __| __/ _ \ '_ ` _ \   |  |
|  |       | |\ \  __/ | | || |____  | |   | | |  __/   /\__/ / |_| \__ \ ||  __/ | | | | |  |  |
|  |       \_| \_\___\_| |_/\_____/  \_|   |_|_|\___|   \____/ \__, |___/\__\___|_| |_| |_|  |  |
|  |                                                           __/ |                         |  |
|  |                                                           |___/                         |  |
|  | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |  |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
```

## Description
In a desperate bid to synchronize my PC clock, I unwittingly downloaded an application that promised a quick fix but instead wrought havoc by encrypting all my important files. Turning to my DFIR friend for help, his attempts to decipher the encrypted mess only worsened the situation, leaving the filesystem corrupted. My friend told me that only a DFIR expert can help recover my files. I'm filled with hope for their assistance in fixing my computer catastrophe.

## Handout

- [Primary Link](https://drive.google.com/file/d/1XvBsf_DRKGTFhJaplfwKShbaDgMWn_f4/view?usp=sharing)
- [Mirror Link ](https://mega.nz/file/pzUhBYRS#6XiIuFce2YnFIhdtuAzUMg33KmUdacOR4H5B3zlJCHQ)

`md5hash : 3652018eef0bece67b7a8c8fa6e1a232`

## Author
- [5h4rrK](https://www.twitter.com/5h4rrK)

### Questions

you can either directly answer it or you can solve the challenge by running main.py in Solution folder and answering it.

```
Q1)List all directories that have been renamed, including their original names and the timestamps of when they were renamed.
  TimeZone - UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]
  Format - [ ['OriginalDirName', 'RenamedDirName', 'TimeStamp'] , .. ]

Q2)Name all the deleted directories with deletion timestamps.
 TimeZone : UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]
 Format - [ ['DirectoryName' , 'TimeStamp'] , .. ]

Q3)List all directories with their creation times, including originals if any that have been renamed or deleted.
 TimeZone : UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]
 Format - [ ['DirectoryName' , 'CreatedTime'] , .... ]

Q4)Recover the files that have been deleted, and provide the md5sum of each recovered file.
 Format - [ ['file1hash'] , ['file2hash'], ... ]  

Q5)Identify all files that have been deleted (Simple + Permanent), including their deletion timestamps.
 TimeZone : UTC(+05:30) [YYYY-MM-DD HH:MM:SS.XX]
 Format - [ [ 'filename' , 'TimeStamp' , 'Simple/Permanent' ] ,... ]

Q6)Restore all encrypted files, decrypt them, and provide the md5sum of each decrypted file after removing any extra bytes before computing the hash.
 Format - [ ['hash1'] , ['hash2'],....]
```

### Solution

The solution as well as the flag can be found in the same folder, but it's advised to finish all the questions before checking the solution.

### Contact

[Azr43lKn1ght](https://twitter.com/Azr43lKn1ght)

Chief Maintainer and Author

DFIR Labs