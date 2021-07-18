from urlextract import URLExtract
import requests
from bs4 import BeautifulSoup
import re
from progress.bar import IncrementalBar
import time
import rainbowtext 

validos=[]
linksDeMega = []
extractor = URLExtract()
f = open("links.txt", "r",encoding='cp932', errors='ignore')
lista = []


def banner():
    print(rainbowtext.text('\n\necho con <3 por Verduxo, con el apoyo de !Hacking Of The World'))
    print(rainbowtext.text('''

  ._.  ___ ___  ________   ___________ __      __ 
  | | /   |   \ \_____  \  \__    ___//  \    /  \
      
  | |/    ~    \ /   |   \   |    |   \   \/\/   /
   \|\    Y    //    |    \  |    |    \        / 
   __ \___|_  / \_______  /  |____|     \__/\  /  
   \/       \/          \/                   \/   
\n\n\n                
'''))
def sacarURl():
    for linea in f:
        urls = extractor.find_urls(linea)
        urls_str = str(urls)[2:-2]
        if urls_str.startswith('https://mega.nz'):
            lista.append(urls_str) 
    f.close()   


def requestUrl(bar1):
    for url in lista:
        try:
            if requests.get(url):
                linksDeMega.append(url)
            
        except requests.exceptions.InvalidSchema:
            print('no se ha podido determinar si este link existe o no\n')
            pass
    
        except IndexError:
            bar1.finish()
            break
        
        except requests.exceptions.ConnectionError:
            print('\u001b[31m'+'\nerror de conexión'+'\u001b[0m'+'\ncompruebe su conexión a internet')
            break
        
        
def Validez(bar1):
    for link in linksDeMega:
        r=requests.get(link)
    
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        count = 0
        Dic = {}
        
        for content in soup.find_all('meta'):
            metaContent = (content.get('content'))
            count += 1
            
            Dic[count]=metaContent
                
        try:
            MGB = (Dic[1].split(' '))
            
        except AttributeError:
            print('none')
            pass
        
        if 'MB' in MGB or 'GB' in MGB:
            bar1.next()
            
            validos.append(link)
            v = open("validos.txt","a")
            v.write(link+'\n')
            v.close()

        else:
            bar1.next()

def terminar(bar1):
    print('\u001B[0m\nse han guardado los links en el archivo \u001b[32m\u001B[4mvalidos.txt \u001B[0m:) \nhay \u001b[32m'+str(len(validos))+'\u001B[0m links validos')
    bar1.finish()  
    
    
    
banner()
sacarURl()
bar1 = IncrementalBar(rainbowtext.text('Procesando:')+'\u001b[32m', max=len(lista))        
requestUrl(bar1)
Validez(bar1)
terminar(bar1)
