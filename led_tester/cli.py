# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
from led_tester import led_tester
import click
import pprint
import util


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input",input)
    N, instructions = None, []
    N, instructions = util.parsefile(input)
    
    test = led_tester(N)
    
    
    for line in instructions:
        sp1 = int(line[1])
        sp2 = int(line[2])
        ep1 = int(line[3])
        ep2 = int(line[4])
        if line[0] == 'turn on':
            test.turn_on(sp1, sp2, ep1, ep2)
        elif line[0] == 'turn off':
            test.turn_off(sp1, sp2, ep1, ep2)
        elif line[0] == 'switch':
            test.switch(sp1, sp2, ep1, ep2)
        else:
            pass
            
        
    
    
    
    return 0

if __name__ == "__main__":
    sys.exit(main())