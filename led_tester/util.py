import urllib
import requests
import re

def parsefile(input):

    if input.startswith('http'):
        N, instructions = None, []
#         input_open = urllib.request.urlopen(input)
#         input_coords=input_open.read().decode('utf-8')
        r = requests.get(input)
        lines = r.text.split('\n')
        N = int(lines[0])
        for i in range(1, len(lines)):
            if(lines[i] is not ''):
                line = lines[i].strip()
                pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
                m = pat.match(line)
                print(m.groups())
                instructions.append(line)
        return N, instructions
    else:
        # read the disk
        N, instructions = None, []
        with open(input,'r') as f:
            # Cast the first line as an int because this will become the size of the array
            N = int(f.readline())
            print("Grid size is %d" %(N))
            for line in f.readlines():
                line = line.strip()
                pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
                m = pat.match(line)
                print(m.groups())
                instructions.append(line)
        # No code yet
        return  N, instructions
    return
