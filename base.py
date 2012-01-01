#!/usr/bin/python2

from array import array
from collections import deque

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def major(root):
	start = notes.index(root)
	return [notes[i] for i in ((0 + start)%12, (2 + start)%12, (4 +   \
		start)%12, (5 + start)%12, (7 + start)%12, (9 + start)%12,\
		(11 + start)%12, (12 + start)%12)]

def minor(root):
	start = notes.index(root)
	return [notes[i] for i in ((0 + start)%12, (2 + start)%12, (3 +   \
		start)%12, (5 + start)%12, (7 + start)%12, (8 + start)%12,\
		(10 + start)%12, (12 + start)%12)]

def maj_penta(root):
	return [major(root)[i] for i in (0, 1, 2, 4, 5, 7)]

def min_penta(root):
	return [minor(root)[i] for i in (0, 2, 3, 5, 6, 7)]

def blues(root):
	ret = min_penta(root)
	ret.insert(3, notes[(notes.index(root) + 6) % 12])
	return ret
