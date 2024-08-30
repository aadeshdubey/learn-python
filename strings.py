# quick helper string methods

str='teststringmethods'
print('str = '+ str)
print('\n')
str.capitalize() #from 3.8 onwards changed to titlecase instead of uppercase
print('str.capitalize() -->',str.capitalize()+' #from 3.8 onwards changed to titlecase instead of uppercase')
print('\n')
str.casefold() #Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".
print('str.casefold() -->',str.casefold()+''' #Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".''')
print('\n')
str.center(20,'|')
print("str.center(20,'|') --> ",str.center(20,'|')+ ' #The original string is returned if width is less than or equal to len(s)')
print(str.count('a'[0:]))
print(str.count('s'[0:]))
print('''str.count('a'[0:]) -->  ''', str.count('a'[0:]) ,' \n')
print('''str.count('s'[0:]) -->  ''', str.count('s'[0:]) ,' \n')