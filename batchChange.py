import os
import Image






m=Image.new('RGB',(410,410))





tarPath="E:\\mf_pangu\\tw2\\res\\universes\\eg\\ycdg"

ns=os.listdir(tarPath)
zoneNum=0
cNum=0

eachCount=[]




for n in ns:

	nsp=os.path.splitext(n)
	if nsp[1]==".chunk":


		pos=[0,0]
		posM=[80,98]
		posM=[100,100]
		x=int(nsp[0][0:3],16)
		y=int(nsp[0][4:7],16)
		#print "xy" ,x ,y
		if x>100 and y>100:
			#up down
			x-=(4087)#+9)+1
			y-=(4090)#+5)+1

			
		elif x>100 and y<100:
			x-=(4087)#+8)-10

		elif x<100 and y>100:
			y-=(4090)#+6)
			#x+=1

		
		else: 
			#up down
			#y+=1
			()
			#y=(y-2)
		#if sx>
		'''
		if x>100 and y>100:
			#up down
			x-=(4087+9)
			y-=(4090+4)
			pos[0]=x*16+int(nsp[0][3:4],16)+posM[0]
			pos[1]=y*16-int(nsp[0][7:8],16)+posM[1]-1
			
		elif x>100 and y<100:
			x-=(4087+7)
			pos[0]=x*16-int(nsp[0][3:4],16)+posM[0]-1
			pos[1]=y*16+int(nsp[0][7:8],16)+posM[1]
		elif x<100 and y>100:
			y-=(4090+6)
			pos[0]=x*16-int(nsp[0][3:4],16)+posM[0]-1
			pos[1]=y*16+int(nsp[0][7:8],16)+posM[1]		
		
		else:
			#up down
			#y=-y
			#print x,y
			#y=(y-2)
			pos[0]=x*16+int(nsp[0][3:4],16)+posM[0]
			pos[1]=y*16-int(nsp[0][7:8],16)+posM[1]-1

		if nsp[0]=="00000000o":
			print "ssssssssss",x,y

		'''
		#print "big",x,y
		pos[0]=(x)*16+int(nsp[0][3:4],16)+80
		pos[1]=(y+1)*16-int(nsp[0][7:8],16)+98-1
		#print "big", pos 

		#color=(225,0,1)
		color=(pos[0],pos[1],1)
		if nsp[0]=="00000000o":
			color=(225,225,225)
			print pos

		if nsp[0]=="000f000fo":

			color=(100,100,100)
		if nsp[0]=="ffffffffo":
			color=(0,225,0)
		if nsp[0]=="fff0fff0o":
			color=(0,160,0)

		if nsp[0]=="ffff0000o":
			color=(0,0,225)
		if nsp[0]=="fff0000fo":
			color=(0,0,160)

		if nsp[0]=="0000ffffo":
			color=(225,0,0)
		if nsp[0]=="000ffff0o":
			color=(160,0,0)		
		
		try:
			m.putpixel((pos[0],pos[1]),color)
		except :
			()
		cNum+=1
		
	elif nsp[1]=="" and len(n)==8:#len(nsp[0])==8:
		fpos=[0,0]

		#print nsp[0]
		x=int(nsp[0][0:3],16)
		y=int(nsp[0][4:7],16)




		fpos[0]=x
		fpos[1]=y
		#print "big",x,y

		#fpos[0]=int(nsp[0][0:3],16)
		#fpos[1]=int(nsp[0][4:7],16)
		#zoneNum+=1

		#color=(fpos[0]*2,fpos[1]*2,0)
		color=(225,0,1)
		#print fpos
		#print color


		#print zoneNum,  fpos
		#print os.path.splitext(n)
		#print os.path.split(n)
		#print (tarPath+"\\"+nsp[0]+"\\")
		nss=os.listdir(tarPath+"\\"+nsp[0]+"\\sep\\")
		tempNum=0
		for n in nss: 
			nssp=os.path.splitext(n)
			if nssp[1]==".chunk":
				pos=[0,0]
				x=int(nssp[0][0:3],16)
				y=int(nssp[0][4:7],16)
				#print "xy" ,x ,y
				posM=[100,100]
				if x>100 and y>100:
					#up down
					x-=(4087)#+9)+1
					y-=(4090)#+5)+1

					
				elif x>100 and y<100:
					x-=(4087)#+8)-10

				elif x<100 and y>100:
					y-=(4090)#+6)
					#x+=1

				
				else: 
					#up down
					#y+=1
					()
					#y=(y-2)

				#print "small", x,y				
				pos[0]=x*16+int(nssp[0][3:4],16)+80
				pos[1]=y*16+int(nssp[0][7:8],16)+98

				#print "small", pos 
				tempNum+=1
				#print nssp[0]
				


				color=(x*40,y*40,0)
				#color=(int(pos[0]*1.5),int(tempNum),int(pos[1]*1.4))
				if nssp[0]=="0010ffefo":
					color=(225,0,0) 
				if nssp[0]=="001fffe0o":
					color=(225,225,225)		
				#color=(pos[0],pos[1],1)
				
				try:
					m.putpixel((pos[0],pos[1]),color)
				except :
					()
				
				cNum+=1
				

		#eachCount.append(tempNum)
	else:
		()
print "chunk cont", cNum
#print "eachCount ", eachCount
#print ns
m.save("d:/fengxx.png")
#print  len(eachCount)
#m=Image.new('RGB',(65536,65536))
#m=Image.new('RGB',(6553,6553))
#m.save("d:/fengx.png")
#print ns