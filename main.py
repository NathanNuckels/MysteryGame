import sys
import face
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

print(face.osh+"helo")

