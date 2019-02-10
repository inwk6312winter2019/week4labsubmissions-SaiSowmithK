import string 
def remove_pattern(word):
	pun = string.punctuation
	str = ""
	for p in pun:
		str = word.strip()
		str = word.replace(p,'')
	return str

def sed(file1,file2):
	try:
		master = open(file1,"r")
		slave = open(file2,"w")
		for ma in master:
			new = remove_pattern(master)
			slae.write(master)
		print("success")
	except:
		print("!!!!!!!!!!!!!!!!!!")

x =input("enter master file for copy operation")
y = input("enter slave file")
sed(x,y)
