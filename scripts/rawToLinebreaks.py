import sys
import re
from bitstring import BitArray

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
        #print(bytes_diff_str.replace(" ", ""))
        print(split_line[2].replace(" ", ""))
        previous_split_line = split_line
