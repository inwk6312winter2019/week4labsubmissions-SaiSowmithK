import string

fp=open('mybook.txt')
name=fp.read()

def print_book():
	count = 0
	mydict = dict()
	for line in name.split():
		word=line.strip(string.punctuation)
		myword = word.lower()
		print(myword)
		count = count+1
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1

	print('the total no of words in the book are:',count)
	print(mydict)
	print('the different  no of words in the book are:',len(mydict))
print_book()
