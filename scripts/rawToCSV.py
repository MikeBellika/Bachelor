import sys
import re
from bitstring import BitArray

def analyse_block2(block2):
    ci = block2[0:2]
    # if ci != "8d":
    #     print(ci)
    #     raise ValueError("We can only parse a CI of 8d but we got " + ci)
    cc = block2[2:4]
    acc = block2[4:6]
    sn = block2[6:14]
    sn_bits = BitArray(hex=sn).bin
    session = sn_bits[0:3]
    time = sn_bits[4:28]
    enc = sn_bits[29:32]
    crc = block2[14:18] # might be wrong
    print("|%s|%s|%s|%s|%s|%s|%s|%s|%s|" % (ci, cc, acc, sn, enc, time, session, crc, ci == "8d"))

def block_diff(previous_block, block):
    previous_block = previous_block.split(" ")
    block = block.split(" ")
    result = []
    for i, _byte in enumerate(block):
        try:
            diff = abs(int(_byte, 16) - int(previous_block[i], 16))
            result.append("{0:02x}".format(diff))
        except ValueError:
            pass
        except IndexError:
            break
    return " ".join(result)

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

filename = sys.argv[1]
print("|block1|block2|time|time_diff|ci|cc|acc|sn|enc|time|session|crc|ci==8D|")
with open(filename, "r") as f:
    previous_split_line = []
    for line in f:
        if line[0] is not "|":
            continue
        split_line = line.split("|")
        split_line[2] = ansi_escape.sub('', split_line[2])
        bytes_diff_str = ""
        time_diff = -1
        if len(previous_split_line) is not 0:
            time_diff = int(split_line[3]) - int(previous_split_line[3])
            bytes = [int(i, 16) for i in split_line[2].split(" ") if i is not ""]
            p_bytes = [int(i, 16) for i in previous_split_line[2].split(" ") if i is not ""]
            bytes_diff_str = block_diff(previous_split_line[2], split_line[2])
        #print(ansi_escape.sub('', line.replace(" ", "")).rstrip() + str(time_diff), end="")
        analyse_block2(split_line[2].replace(" ", ""))
        #print(bytes_diff_str.replace(" ", "|") + "|")
        previous_split_line = split_line
