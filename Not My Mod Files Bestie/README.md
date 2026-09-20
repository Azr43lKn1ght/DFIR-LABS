# Not My Mod Files Bestie 

## Difficulty: `Hard`

```
%      ,
%     /|/\    _ _|_                             _   _|     |\ o |\  _  ,     |)   _  , _|_ o  _
%      |  |  / \_|     /|/|/|  |  |    /|/|/|  / \_/ |     |/ | |/ |/ / \_   |/\_|/ / \_|  | |/
%      |  |_/\_/ |_/    | | |_/ \/|/    | | |_/\_/ \/|_/   |_/|/|_/|_/ \/     \/ |_/ \/ |_/|/|_/
%                                (|                        |)
```

## Description

Natsume downloaded a malicious game-modding tool that encrypted her files. Investigate the supplied email, memory dump, and evidence archive, then answer the seven questions to recover the flag.

## Handout

- [Primary Download](https://drive.google.com/file/d/1pvRB_Lt2mK7CHPvAe6zhWVcwu9W-mBD-/view?usp=sharing)

- [Secondary Download](https://mega.nz/file/EmE1GRTS#c9yFch4NM6wKPhxvs_UBw8oVxqgscEQRAEIiHLj1WEU)

The handout contains:

- `memdump.raw`
- `natsume.eml`
- `evidence.7z`



### Questions

You can answer the questions directly or run the challenge script from the `solution` folder:

```bash
cd Solution
python challenge.py
```

```
Q1) What is the password of Natsume's Windows account?
Format: password

Q2) What is the name of the malicious executable found on Natsume's machine?
Format: filename.exe

Q3) What password did Natsume use to extract the tool sent by the attacker?
Format: password

Q4) What is the master encryption key used by ModCollabTool?
Format: key

Q5) What MITRE ATT&CK technique does ModCollabTool use? (obfuscation or encryption for impact)
Format: TXXXX

Q6) What map contains the attacker's planted artifact?(`evidence.7z password: s0und_0f_a_s0ul`)
Format: mXX_XX_XX_XX

Q7) The attacker planted something in Gwyn's boss room. Find the collision mesh ID,
boss room BGM ThinkParamID, XYZ coordinates of the model, and the map piece ID.
Format: {mesh:XXXXXX|ThinkParamID:XXXXXX|pos:X,X,X|map:mXX_XX_XX_XX}
```

## Author

- [mooofinnn](https://x.com/mooofinnn)

### Solution

The solution as well as the flag can be found in the same folder, but it's advised to finish all the questions before checking the solution.

### Contact

[Azr43lKn1ght](https://twitter.com/Azr43lKn1ght)

Chief Maintainer and Author

DFIR Labs
