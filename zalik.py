f = open("data.txt", "rt")

begin = 0

end = 0

data1=[] #-- по рядкам
data2=[] #-- по абзацам





for i in f:
	data1.append(i)
	data2.append("") # -- пусті елементи щоб було все ок в 24 рядку
	
	

i=0
k=0
while(i<len(data1)):

	data2[k]=data2[k]+data1[i]

	if (not data1[i].strip()):
		k+=1
	i+=1


#i=0
#lendata2=0
#while(i<len(data2)):
#		if (not data2[i].strip()):
#			lendata2=i                   # -- визначення правильної довжини 
#			break
#		i+=1

x=0

while(True):
	
	print("введіть слово")
	tag = input()
	
	if(tag=="stop"):
		break
		
	#if(len(tag)==1):
	#	print("слово повинно складатись мінімун з двох символів")
	#	continue
		
	if(not tag.find(" ")==-1):
		print("це не слово тут пробіл")
		continue
		

		
	i=0
	for i in range(0,len(data2)):
		#	print("i",i)
			if(not data2[i].find(tag)==-1):
				
					if( data2[i].find(tag)==0 or data2[i][data2[i].find(tag)-1]==" "):
					#	print("oppa2")
						x=0
						for j in range (data2[i].find(tag),len(data2[i])):
							#print("j",j)
							if(data2[i][j]==" "):
								#print("oppa4",data2[i][data2[i].find(tag,x)-1])
								try:
									#print("oppa5",x)
									z=tag[j-data2[i].find(tag,x)-1]  # щоб була якась дія
									if(data2[i][data2[i].find(tag,x)-1]==" "):
										print(data2[i])
								except IndexError:
									x=j 
									#print("oppa6") 
