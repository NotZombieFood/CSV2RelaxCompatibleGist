from PythonGists import PythonGists
from optparse import OptionParser
import string, random
import csv
parser = OptionParser()
parser.add_option("-n", "--name", dest="name",
                  help="Escoge el nombre de tu base de datos", metavar="NAME")
parser.add_option("-f", "--files", dest="files",
                  help="Escribe los archivos que convertimos separados de comas (obligatorio)")

(options, args) = parser.parse_args()
if options.files is not None:
	if options.name is None:
		print('No se ha proporcionado un nombre, se usará uno aleatorio')
		nouns = ("puppy", "car", "rabbit", "parrot", "monkey")
		verbs = ("runs", "hits", "jumps", "drives", "barfs") 
		adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
		adj = ("adorable", "clueless", "dirty", "odd", "stupid")
		num = random.randrange(0,5)		
		nombre = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
	else:
		nombre = options.name
	archivos = options.files.split(',')
	texto = 'group: ' + nombre
	texto += '\n description[[ the data for this dataset was generated using pythonConv by notZombieFood]] \n\n'
	for i in range(len(archivos)):
		try:
			texto += archivos[i] + ' = {'
			filename = archivos[i]+'.csv'
			with open(filename, 'rt') as csvfile:
				csvRows = csv.reader(csvfile, delimiter=' ', quotechar='|')
				for row in csvRows:
					textorow = ''.join(row)
					texto += textorow.replace('/', '-').replace(',','-') + '\n'
			texto += '}\n\n'
		except:
			print(archivos[i] + '.csv no se ha encontrado')
	link = PythonGists.Gist(description='Gist creado automaticamente',content=texto,name=nombre)
	url_split = link.split('com/')
	print('Copia y pega lo siguiente en el sitio web')
	print (url_split[1])
else:
	print('No incluiste algun archivo, para ver la lista de parametros puedes usar --help')