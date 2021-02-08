def gen_scale(s):
	steps = [1,1,0.5,1,1,1,0.5]
	notes = [s]
	for step in steps:
		s += step
		notes.append(s % 6)
	return notes

scale_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
num_map = {}

num = 0
for name in scale_names:
	num_map[name] = num
	num += 0.5

N = int(input())
song = set(i for i in input().split())
valid_scales = []

for note in scale_names:
	temp = gen_scale(num_map[note])
	valid = True

	for s in song:
		if num_map[s] not in temp:
			valid = False
			break
	
	if valid:
		valid_scales.append(note)

if len(valid_scales) == 0:
	print('none')
else:
	for v in valid_scales:
		print(v, end=' ')
	print('')
