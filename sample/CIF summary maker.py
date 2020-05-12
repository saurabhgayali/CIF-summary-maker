#filepath="../proteins/cif/6lu7.cif"

import pathlib
import os

path=pathlib.Path().absolute()

proteinfolder='./cif/'

protein_filelist=os.listdir(proteinfolder)
#print(protein_filelist[0])


from IPython.core.display import display, HTML
#display(HTML(getsize(filepath)["html"]))
import re

def getsize(filepath):
	out={}
	n=filepath.split('/')
	out['name']=n[-1:][0]
	f=open(filepath,'r')
	g=f.read().split('\n')
	
	x_array=[]
	y_array=[]
	z_array=[]
	for text in g:
		if text[0:6]=="      ":
			text=re.sub(' +', ' ', text)
			#print(text)
			x_array.append(float(text.split(" ")[3]))
			y_array.append(float(text.split(" ")[4]))
			z_array.append(float(text.split(" ")[5]))
			#print(x_array)
	x_size=max(x_array)-min(x_array)
	y_size=max(y_array)-min(y_array)
	z_size=max(z_array)-min(z_array)
	out["path"]=(filepath)
	out["x"]=round(x_size,2)
	out["y"]=round(y_size,2)
	out["z"]=round(z_size,2)
	#print(x_size)
	#size_array=dict({'x'=x_size})
	return out
header='<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n<div class".bg-info" style="background-color:#17a2b8;padding:10px;"><h1>\nHTML Summary of Protein Structures\n</h1></div>\n'


detail_section='\n\n\n\n<h3>Individual Box sizes</h3><table class="table">\n<tbody>\n<tr><th>Name</th><th>Size(X)</th><th>Size(Y)</th><th>Size(Z)</th></tr>\n'
i=0
max_x_array=[]
max_y_array=[]
max_z_array=[]
for protein in protein_filelist:
	o=getsize(proteinfolder+protein)
	#print(o)
	get='<tr><th>'+str(o['name'])+'</th><td>'+str(o['x'])+'</td><td>'+str(o['y'])+'</td><td>'+str(o['z'])+'</td></tr>\n'
	max_x_array.append(o['x'])
	max_y_array.append(o['y'])
	max_z_array.append(o['z'])
	#print(get)
	detail_section+=get
	i+=1

detail_section+='</tbody>\n</table>\n</div>'
summary_section='<div class="container">\n<table class="table">\n<tbody>\n'+'<tr><th colspan=2><h3>Summary of the search</h3></th></tr>\n'+'<tr><th>Folder Path</th><td>Folder Path</td></tr>\n'+'<tr><th>Number of CIFs found</th><td>'+str(i)+'</td></tr>\n'+'<tr><th colspan=2><h3>Max Bounding box size</h3></th></tr>\n'+'<tr><th>Max Size_X</th><td>'+str(max(max_x_array))+'</td></tr>\n<tr><th>Max Size_Y</th><td>'+str(max(max_y_array))+'</td></tr>\n'+'<tr><th>Max Size_Z</th><td>'+str(max(max_z_array))+'</td></tr>\n</tbody>\n</table>'

graph='\n<br>\n<div class="text-center">\n<img src="distribution.png" style="width:100%;max-width:800px" class="img-fluid img-thumbnail"></img>\n</div>\n<br>\n'

footer='<div class="footer mt-auto py-3 .bg-secondary" style="background-color:#6c757d;padding:10px">\nReport generated using pyton script\n</div>\n'
html=header+summary_section+detail_section+footer
html2=header+summary_section+detail_section+graph+footer
	

display(HTML(html))
p=open('PDB-cif-summary.html','w+')
p.write(html2)
p.close()




import matplotlib.pyplot as plt
#%matplotlib inline

fig, axs = plt.subplots(3)
fig.suptitle('Distribution of Box size',y=1.05,fontsize=20)
fig.tight_layout(pad=1.0)
plt.ylabel='Frequency'
axs[0].hist(max_x_array, bins = int(180/10),color = 'red', edgecolor = 'black')
axs[0].set_title('Size (X-axis)')
axs[1].hist(max_y_array, bins = int(180/10),color = 'blue', edgecolor = 'black')
axs[1].set_title('Size (Y-axis)')
axs[2].hist(max_z_array, bins = int(180/10),color = 'green', edgecolor = 'black')
axs[2].set_title('Size (Z-axis)')

plt.tight_layout()
#bbox_inches='tight'
plt.subplots_adjust(top=0.88)

plt.savefig('distribution.png',dpi=300)
plt.show()



