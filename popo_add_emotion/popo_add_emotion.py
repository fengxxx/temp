from  xml.etree.ElementTree import*
import time
import os ,sys
import shutil
import win32clipboard as w
import win32con
#tFilePath="C:\\Program Files (x86)\\Netease\\POPO\\users\\hzzengjf@corp.netease.com\\emoticon\\cusemot.xml"


ROOT_DIR=os.getcwd()



def emotionElement(d,n,p):
	n+="_fengx"
	item = Element("Emoticon", {'id' : d, 'tag' : ' ','text' : n,"file":p})
	return item

def indent(elem, level=0):
	i = "\n" + level*"  "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		for e in elem:
			indent(e, level+1)
		if not e.tail or not e.tail.strip():
			e.tail = i
	if level and (not elem.tail or not elem.tail.strip()):
		elem.tail = i
	return elem

def getText():
	w.OpenClipboard()
	d=""
	try:
		d = w.GetClipboardData(win32con.CF_TEXT)
	except:
		d=" "#(w.GetClipboardData(win32con.CF_HDROP))[2]
	w.CloseClipboard()
	return d


def getFilePath():
	w.OpenClipboard()
	d=[]
	'''
	try:
		#w.GetClipboardData(win32con.CF_TEXT)
		d.append(w.GetClipboardData(win32con.CF_TEXT))
	except:
		print "no clip text"
	'''
	try:
		#w.GetClipboardData(win32con.CF_HDROP)
		a=w.GetClipboardData(win32con.CF_HDROP)
		for s in w.GetClipboardData(win32con.CF_HDROP):
			#print s
			#print s[2:]
			d.append(str(s))
	except:
		print "no clip files"

	w.CloseClipboard()
	#print d
	return d

def getDragFIles():
	fs=[]
	if len(sys.argv)>1:
		fs=sys.argv[1:]
	return fs
def addEmoticon(xmlPath,files):
	ID=int(time.time())
	print  xmlPath, files
	fs=files#os.listdir(ROOT_DIR)
	mainXML=ElementTree(file=xmlPath)
	mainRoot=mainXML.getroot()
	haveOn=False
	mainData=mainRoot.find("Catalog")
	'''
	for s in mainRoot.findall("Catalog"):
		if s.get("Title")=="fengx":
			haveOn=True
			#mainData=s
			mainData=mainRoot.find("Catalog")
	if haveOn==False:
		mainData=Element("Catalog", {'id' : "ID_fengx", 'Path' : ' ', "Title":"fengx"})
	
	print haveOn
	'''
	if len(fs)!=0:
		i=1
		for f in fs:
			fileType=os.path.splitext(os.path.split(f)[1])[1] 
			name=os.path.splitext(os.path.split(f)[1])[0]
			if fileType==".jpg" or fileType==".png" or fileType==".bmp" or fileType==".JPG" or fileType==".PNG" or fileType==".GIF" or fileType==".gif":  
				n=name+str(i)
				print n
				print ID
				ID+=1
				print ID
				fileName=n+fileType

				tPath=os.path.split(xmlPath)[0]+"\\"+fileName 		
				shutil.copy(f,  tPath)

				#copyFiles(f, tPath)

				#os.system ("xcopy /s %s %s" % (f, tPath))
				item=emotionElement(str(ID),n,fileName)
				i+=1
				mainData.append(item)
		#if haveOn==False:
		#	mainRoot.append(mainData)
		mainXML._setroot(indent(mainRoot))
		mainXML.write(xmlPath,"utf-8")







#ems=getFilePath()
ems=getDragFIles()
#print ems
if len(ems)!=0:
	#ton=False
	clp=getText()+"\\POPO\\users\\"
	xmlPs=[clp,"C:\\Program Files (x86)\\Netease\\POPO\\users\\","D:\\Program Files (x86)\\Netease\\POPO\\users\\"]
	for xmlP in xmlPs:
		try:
			clpFlies=os.listdir(xmlP)
			for f in clpFlies:
				fName=xmlP+f+"\\emoticon\\cusemot.xml"
				print fName
				if os.path.isfile(fName):
					addEmoticon(fName,ems)
					#ton=True

		except:
			print "x1"


#raw_input("don't click me ! dray file up me ! ")