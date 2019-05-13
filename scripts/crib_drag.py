# cipher1 = 0x53ffc30b
# cipher2 = 0x33fc031d
# cipherXor = cipher1 ^ cipher2
line = "112233ffccdd"
cipherXor = [line[i:i+4] for i in range(0, len(line), 4)]
crib = 0x022b
crib_deviation = 10 # Crib +- this value will be checked
for cribByte in range(crib-10, crib+10):
    for cipherByte in cipherXor:
        print(int(cipherByte, 16) ^ cribByte)
