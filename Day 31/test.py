import html


# with open("nk.txt",'r') as data:
# 	new_data=data.readlines()

# 	# ko=[item.split(',')[0].strip() for item in new_data if "to" not in item]
# 	# for i in ko:
# 	# 	print(i)

# 	# nw=[item.split(' ') for item in new_data ]
# 	# # ks=[item for item in nw]
# 	# print(nw)


# mok=[['oncle', 'uncle\n'], ['\n'], ['prix', 'price\n'], ['\n'], ['retard', 'delay\n'], ['\n'], ['cadeau', 'presen\n'], ['\n'], ['face', 'face\n'], ['\n'], ['gueule', 'mouth\n'], ['\n'], ['chemin', 'path\n'], ['\n'], ['vivant', 'vibrant\n'], ['\n'], ['gÃƒÂ©nÃƒÂ©ral', 'general\n'], ['\n'], ['bateau', 'boat\n'], ['\n'], ['million', 'million', 'noun\n'], ['\n'], ['sac', 'bag\n'], ['\n'], ['impossible', 'impossible', 'adjective\n'], ['\n'], ['seconde', 'second\n'], ['\n'], ['bÃƒÂªte', 'stupid\n'], ['\n'], ['erreur', 'error\n'], ['\n'], ['soleil', 'sun\n'], ['\n'], ['voyage', 'trip\n'], ['\n'], ['clair', 'clear\n'], ['\n'], ['faux', 'wrong\n'], ['\n'], ['balle', 'ball\n'], ['\n'], ['cheveu', 'hair\n'], ['\n'], ['papier', 'paper\n'], ['\n'], ['prÃƒÂ©sent', 'present\n'], ['\n'], ['tranquille', 'quiet\n'], ['\n'], ['neuf', 'nine;', 'new\n'], ['\n'], ['blanc', 'white\n'], ['\n'], ['table', 'table\n'], ['\n'], ['dix', 'ten\n'], ['\n'], ['clÃƒÂ©', 'key\n'], ['\n'], ['agent', 'officer\n'], ['\n'], ['sens', 'direction\n'], ['\n'], ['six', 'six', 'numerical', 'adjective\n'], ['\n'], ['message', 'message', 'noun\n'], ['\n'], ['salle', 'room\n'], ['\n'], ['effet', 'effect\n'], ['\n'], ['espÃƒÂ¨ce', 'species\n'], ['\n'], ['bois', 'wood\n'], ['\n'], ['camp', 'camp', '\n'], ['\n'], ['sorte', 'sort\n'], ['\n'], ['hÃƒÂ´tel', 'hotel\n']]
# french=[]
# english=[]
# for k in mok :
# 	if k !=['\n']:
# 		french.append(k[0])
# 		english.append(k[1].strip())
# print(french)


french=['oncle', 'prix', 'retard', 'cadeau', 'face', 'gueule', 'chemin', 'vivant', 'gÃƒÂ©nÃƒÂ©ral', 'bateau', 'million', 'sac', 'impossible', 'seconde', 'bÃƒÂªte', 'erreur', 'soleil', 'voyage', 'clair', 'faux', 'balle', 'cheveu', 'papier', 'prÃƒÂ©sent', 'tranquille', 'neuf', 'blanc', 'table', 'dix', 'clÃƒÂ©', 'agent', 'sens', 'six', 'message', 'salle', 'effet', 'espÃƒÂ¨ce', 'bois', 'camp', 'sorte', 'hÃƒÂ´tel']

english=['uncle', 'price', 'delay', 'presen', 'face', 'mouth', 'path', 'vibrant', 'general', 'boat', 'million', 'bag', 'impossible', 'second', 'stupid', 'error', 'sun', 'trip', 'clear', 'wrong', 'ball', 'hair', 'paper', 'present', 'quiet', 'nine;', 'white', 'table', 'ten', 'key', 'officer', 'direction', 'six', 'message', 'room', 'effect', 'species', 'wood', 'camp', 'sort', 'hotel']


new_dict={
	'French':french,
	'English':english
}

import pandas


dt=pandas.DataFrame(new_dict)
dt.to_csv('french_to_eng.csv')


