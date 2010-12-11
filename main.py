
import glob,re,codecs, chardet
from  _natsort import natsorted

sutras = {}

max_lines = []

for f in glob.glob("original_txt/*"):
    source = f[13:len(f)-4] # this depends on line above
    c = 0
    #print "\n=====%s====\n"%f
    for l in codecs.open(f,encoding='cp1251',mode='r'):
        l = l.replace("\r\n","")
        
        m = re.search("  (\d+)\. \(([1-4])\)",l)
        if m:
            key = "%s.%s" % ( m.group(2) , m.group(1) )
            l = re.sub("  \d+\. \([1-4]\) ","",l)
            #print key ,l
            
            if key not in sutras:
                sutras[key]=[]
            sutras[key].append([l,source])
                
            c=c+1
        else:
            if l != '':
                #print l
                pass
    max_lines.append([f,c])
    


template = "".join(file('template.html', 'r').readlines())
content = ""

for s in natsorted(sutras.keys()):
    key = s
    content += "<h4>%s</h4>\n"%key
    for s in sutras[key]:
        content += "<span class=\"source_%s\">%s</span><br/>\n" % (s[1],s[0])

template = template % content

fp = codecs.open('out.html',encoding='cp1251',mode='w')
fp.write(template)
fp.close()

print "out.txt generated"