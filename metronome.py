#!/usr/bin/env python
from sys import argv
from tempfile import NamedTemporaryFile
import subprocess

bpm = float(argv[1])
time = 60000 / bpm

#Would rather use paranthesis: str = ("..." "...")
str = "Step s => ZeroX z => dac; \n10.0 => float v; \n\nwhile (true) { \
	\n\tv=> s.next; \n\t" + str(time) + "::ms => now; \n} \n"

f = NamedTemporaryFile (delete = False)
print (f.name)
f.write(str)

subprocess.call (['chuck', f.name])


#
#Sample program for simplicity
#

#Step s => ZeroX z => dac; //Step gen, zero crossing detector, DAC
#10.0 => float v;
#
#while( true )
#{
#    v => s.next;	//Set step value
#    -v => v;		//Change step value
#    500::ms => now;	//bpm = 60000 / value
#}
