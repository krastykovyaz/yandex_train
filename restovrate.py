def replace_pos(text):
	i = 1
	words = text.split()
	if words[0] != 'По':
		new_string = ''
	else:
		new_string = words[0]
	f = False
	f2 = False
	while i < len(words):
		f2 = False
		if words[i-1] == 'по' and words[i].startswith('ссылк'):
			new_string += 'посылки'
			f = True
		elif  words[i-1] == 'По'  and words[i].startswith('ссылк'):
			new_string += 'Посылки'
			f = True
		else:
			new_string += words[i-1]
			f2 = True
		i += 1
	if f2:
		new_string += words[i-1]
	return 	new_string if f else None

if __name__=='__main__':
	import pandas as pd
	# df = pd.read_excel('check_dataset_logistic_2.xlsx')
	# df['replace_pos'] = df.input_text.apply(replace_pos)
	# df.to_excel(out.xlsx, index=False)
	print(replace_pos('По ссылке пуаыф'))
