import sys
import face
import savemgr
print("Them by Alan")
while True:
	print("Commands: \"new\" \"load\" \"about\" \"exit\"")
	cmd=input("><>")
	if cmd=="load":
		pass
	elif cmd=="about":
		print("A face made of Unicode characters")
		print("wants something... but what?")
	elif cmd=="exit":
		sys.exit()
	elif cmd=="new":
		break
	else:
		print("Command not found")
save=savemgr.Save()
while True:
	if save.location=="new":
		print(face.osh+" helo")
		print("")
		print("                  i am face.")
		input("(press enter...)")
		print("\n???:what do you want?\n")
		print(face.glasses+"  oh.... i donno.....")
		print(face.smug+"   you'll find out i guess\n\n")
		print("at the moment i want your name...")
		while True:
			print("Enter a name:")
			name=input("><>")
			if len(name)<3:
				print("Name must be at least 3 characters")
			if len(name)>16:
				print("Name must be shorter than 16 characters")
			if name.lower()=="alan" or name.lower()=="nathan":
				print(face.veryExcited+" Hey hey! You must be a playtester!")
				break
			else:
				break
		save.name=name
		print("\n"+face.dollar+"\n"+face.verySuprized+" You wern't supposed to see that")
		
