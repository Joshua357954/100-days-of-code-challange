PLACEHOLDER ='[name]'

# The Main letter template 
with open('./letter.txt')as letter:
	letter_body=letter.read()

# Names of the receivers
with open('../Names/name.txt')as name:
	name_list=name.readlines()

	for _name in name_list:

		s_name=_name.strip()

		new_letter=letter_body.replace(PLACEHOLDER,s_name)
		
		# create a new document with the specific name 
		with open(f'../Ready_Mail/Letter_to_{s_name}.docx',mode='w')as l_t_s:

			l_t_s.write(new_letter)