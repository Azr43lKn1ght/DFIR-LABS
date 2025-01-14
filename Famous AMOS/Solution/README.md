# Solution

- Extract several HTTP objects from the PCAP file (DMG file, PNG file, docx)
- One of the HTTP object is the Apple DMG file, which can be extracted to obtain the malicious Mach-O binary (lobsterstealer)
- Analyzing the Mach-O binary, a long hex payload can be decrypted using a hardcoded RC4 hex key in the same binary
- The payload shows that the flag is encoded with the MD5 hash of the PNG file and sent to the C2 server. Since the encoded flag was sent to the C2 server, it can be extracted from the PCAP also.
- Just decrypt the flag file with the MD5 hash
