#!/usr/bin/env python

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

#Index to note
def i_to_n(index):
	return notes[index%12]

#Note to index
def n_to_i(note):
	return notes.index(note)

#Major, minor, and other scales.
def major(root):
	return [i_to_n(i + n_to_i(root)) for i in (0, 2, 4, 5, 7, 9, 11)]

def minor(root):
	return [i_to_n(i + n_to_i(root)) for i in (0, 2, 3, 5, 7, 8, 10)]

def maj_penta(root):
	return [major(root)[i] for i in (0, 1, 2, 4, 5)]

def min_penta(root):
	return [minor(root)[i] for i in (0, 2, 3, 5, 6)]

def blues(root):
	ret = min_penta(root)
	ret.insert(3, notes[(notes.index(root) + 6) % 12])
	return ret

print (blues('A'))
