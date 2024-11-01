from math import *
import mido
import json
from pathlib import Path

def midi_read(midi):
	inp = []
	try:
		mid = mido.MidiFile('midi/'+midi+'.mid')
	except:
		return 'Midi didn`t been found. Maybe, you just typed midi name wrong -_-'
	for string in mid.play():
		tmp = {}
		print(string)
		try:
			tmp['note'] = string.note
			tmp['time'] = string.time
			tmp['type'] = string.type
			tmp['channel'] = string.channel
			inp.append(tmp)
			print(tmp)
		except:
			print('-_-')
			
	with open('.cache/'+midi+'.json', "w") as fp:
		json.dump(inp, fp)
		
	print(inp)
	return 'Decoded sucsessfuly (i hope so)'


def write(midi, channel=0):
	#try:
	with open('.cache/'+midi+'.json', "r") as fp:
		inp = json.load(fp)
	#except:
	#	return 'Decoded midi didn`t been found. Maybe, you just typed midi name wrong -_-'
	
	Path('result/' + midi).mkdir(parents=True, exist_ok=True)
	file_name_out = 'result/' + midi + '/channel_' + str(channel) 
	out = open(file_name_out, 'w')
	strs = 0
	for i in inp:
		if i['channel'] == channel and i['type'] == 'note_on':
			octave = floor(i['note'] / 12)
			letter = i['note']%12
			k = octave + letter/100 - 1
			k = round(k, 2)
			out.write('control config block1 ' + str(k) + ' 0 0 0\n')
			strs += 1
			if strs%999 == 0:
				out.write('write ' + str(strs//999+1) + ' cell1 0')
				out.close()
				cpu+=1
				file_name_out = 'result/' + midi + '/channel' + str(channel) + '_cpu' + str(cpu)
				out = open(file_name_out, 'w')
		if i['time'] != 0:
			out.write('wait ' + str(i['time']) + '\n')
			strs += 1
			if strs%999 == 0:
				out.write('write ' + str(strs//999+1) + ' cell1 0')
				out.close()
				cpu+=1
				file_name_out = 'result/' + midi + '/channel' + str(channel) + '_cpu' + str(cpu)
				out = open(file_name_out, 'w')
	out.write('write 1 cell1 0')
	out.close()
	return 'Wroten ' + str(strs) + ' strings sucsessfully!'

if __name__ == '__main__':
	Path('result').mkdir(parents=True, exist_ok=True)
	Path('.cache').mkdir(parents=True, exist_ok=True)
	Path('midi').mkdir(parents=True, exist_ok=True)
	while(True):
		ac = input('Type action (1 for decode, 2 for write): ')
		if ac == '1':
			midi = input('Type name of midi (without .mid): ')
			print(midi_read(midi))
		elif ac == '2':
			midi = input('Type name of decoded midi (without .mid): ')
			channel = int(input('Type name of channel to use: '))
			print(write(midi, channel))
		else:
			print('What did you just wrote?')
			
