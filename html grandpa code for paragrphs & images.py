def para(x):
	print("p"+str(x)+"= input ('enter paragraph no"+str(x)+" ')")
	print("font_fam_p"+str(x)+"= input ('enter font family for paragraph no"+str(x)+" ')")
def printpara(x):
	print ("print ('<p>')")
	print ("print (p"+str(x)+")")
	print ("print ('</p>')")
def img(x):
	print ("imag"+str(x)+"= input ('enter the src for img"+str(x)+"')")
	print ("imag"+str(x)+"= input ('enter the src for img"+str(x)+"')")
def printimg(x):
	print ("""print('<img src="'+imag"""+str(x)+"""+'"/>')""")
i = int(input('no of paragrphs required '))
j = int(input('no of images required '))
title = input('enter the title of page ')
x=1
a=1
b=1
c=1
while x<=i:
	y=x
	def numpara(i):
		return(para(i))
	numpara(y)
	x=x+1
while b<=j:
	def numpara(i):
		return(img(i))
	numpara(b)
	b=b+1
print ("title='"+title+"'")
print ("print ('<html>')")
print ("print ('<head>')")
print ("print ('<title>',title, '</title>')")
print ("print('</head>')")
print ("print ('<body>')")
while a<=i:
	z=a
	def numpara(i):
		return(printpara(i))
	numpara(z)
	a=a+1
while c<=j:
	def numpara(i):
		return(printimg(i))
	numpara(c)
	c=c+1
print ("print ('</body>')")
print ("print ('</html>')")
