from ctypes import sizeof
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import mysql.connector




nome3=[]
cidade=[]
j=''
cb=[]
primeiro= True 
item=0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}


options = Options()
    # options.add_argument('--headless')
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

navegador.get('WEBSITE')

sleep(2)

id = "signin-link"


input_place = navegador.find_element_by_id("signin-link")
input_place.click()

usuario = navegador.find_element_by_xpath("//*[@name='username']")
usuario.send_keys('YOUR EMAIL')
usuario = navegador.find_element_by_xpath("//*[@name='password']")
usuario.send_keys('YOUR PASSWORD')
enviar = navegador.find_element_by_xpath("//*[@type='submit']")
enviar.click()


page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

pessoas = site.find('div', attrs={'id': 'aViews'})
a=pessoas.find_all('div', attrs={'class':'user_info nobreak'})


for b in a:
    nome=b.find('a')
    nome2=str(nome)
        
        
        #print(nome2)
    if "female" in nome2:
        nommme = nome.get_text()
        nome7=b.find('div').get_text()     
        for k in nome7:
            if k == 'n' and j=='/':
                k=''
            if k=='\n':
                j=k
                k=''
            cb.append(k)
            
        nome55=''.join(cb)
            
            
            
            
            #print(nome55)
            #print(type(nommme))
        nome3.append(nommme)
        cidade.append(nome55)
        nome55=''
        cb=[]
            
            

            
messages= site.find('span',attrs={'id':'pmNewCnt'}).get_text()

bmk=[]
for mk in messages:
    if mk=='(' or mk==')' or mk =='+':
        mk=''
    bmk.append(mk)
cmk=''.join(bmk)
ccmk=int(cmk)



print(nome3[0])
print(cidade[0])









banco = mysql.connector.connect(
    host="IP DB",
    user="USER DB",
    passwd="PASSWORD DB",
    database="DATABASE NAME"
    
)


cursor = banco.cursor()







    

    
comandd = "UPDATE interpalsMSG  set msg=%s"
cursor.execute(comandd,(ccmk,))
banco.commit()

    


comando_SQLdel = "DELETE FROM interpals"

        

cursor.execute(comando_SQLdel)


banco.commit()  
    
    
while item < len(nome3):
    comando_SQL = "INSERT INTO interpals (nome,cidade) VALUES (%s,%s)"
    dados= (nome3[item],cidade[item])
        

    cursor.execute(comando_SQL,dados)


    banco.commit()
    item=item+1