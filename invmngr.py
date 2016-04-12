"""InvMngr 0.4

es fehlt:
check config: überprüft ob config vorhanden, wenn nicht wird eine datei erstellt
sie enthält den dateipfad für die json dateien

"""

import os
import json

 

def i_out():
	os.system('clear')

	print("1) Add/Remove Items")
	print("2) Delete Item")
	print("3) Show List")
	print("4) End")
	print("5) Help")

	print("\nInput a single number:")

	try:
		select = int(input("> "))
	except:
		print("\nWrong input!")
		input("")
		i_out()

	if select == 1:
		add()
	elif select == 2:
		delete()
	elif select == 3:
		show()
		i_out()
	elif select == 4:
		end()
	elif select == 5:
		helpinv()
	else:
		print("Wrong input")
		input("")
		i_out()

def delete():
	print("Put in ID you want to delete")
	try:
		ident = str(input("> "))
	except:
		print("Wrong input!")
		input("")
		i_out()

	if ident in key_list:
		print("Sure? Y/n")
		if choice(str(input("> "))):
			del(schrank[ident])
			key_list.remove(ident)
			fileexport(filename)
			show()
			print("Deleted!")
			input("")
			i_out()
		else:
			i_out()
	else:
		print("ID does not exist")
		input("")
		i_out()



def show():
	global schrank
	global key_list
	key_list.sort()

	os.system('clear')
	print("ID\t\tName\t\tAmount\n")
	for key in key_list:
		
		print(key + "\t\t" + str(schrank[key][0]) + "\t\t" + str(schrank[key][1]))

	input()

def choice(yes):
	if yes.upper() == 'Y':
		return 1
	else:
		return 0

def helpinv():
	print("This Programm is managing a simple python-dictionary. You can use it to manage your inventory.")
	print("1) Add/Remove")
	print("First put in ID, if it is existing you can change the Amount of it. ")
	print("The value you put in gets added to the Amount (use negative numbers to decrease it)")
	print("2) Delete - Put in ID to delete the whole thing")
	print("3) Show list - Shows the Dictionary")

	input("")
	i_out()


def end():
	print("Realy want to quist?")
	print("Y/n")
	if choice(str(input("> "))):
		exit(1)
	else:
		i_out()

	exit(1)
def add():
	global schrank 

	os.system('clear')
	print("ID eingeben:")
	ident = str(input("> "))

	if ident in schrank:
		try:
			print("Anzahl ändern: ")
			i = int(input("> "))
			schrank[ident][1] += i
			save = False
			show()
		except:
			print("Wrong input!")
			input("")
		
	elif ident not in schrank:
		print("Add new Item? Y/n")
		if choice(str(input("> "))):
			print("Name eingeben:")
			schrank[ident] = ["", 0]
			schrank[ident][0] = str(input("> "))
			key_list.append(ident)
			save = False

			print("Anzahl eingeben:")
			schrank[ident][1] += int(input("> "))
			show()
			print("Vorgang Abgeschlossen")

	fileexport(filename)
	i_out()

def configfile():
	print("####################")
	



def fileimport(filename):
	global schrank
	try:
		with open(filename) as outfile:
		    schrank = json.load(outfile)
		    for key in schrank:
		    	key_list.append(key)
	except:
		print("No *.json file to load Dictionary. The File 'inv' will be created when adding the first item")
		
		input("")
		
	    	
def fileexport(filename):
	global schrank
	try:
		with open(str(filename), 'w') as outfile:
	   		json.dump(schrank, outfile)
	except:
		print("Can not save Dictionary to " + str(filename))

schrank = {}
key_list = []
save = True
filename = "inv"

fileimport(filename)
print(schrank)
i_out()








