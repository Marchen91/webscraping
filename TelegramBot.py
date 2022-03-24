import telebot
import mysql.connector


banco = mysql.connector.connect(
    host="IP DB",
    user="USER DB",
    passwd="PASSWORD DB",
    database="DATABASE NAME"
    
)


cursor = banco.cursor()



comandd = "SELECT * FROM interpals"
cursor.execute(comandd)
valores = cursor.fetchall()
#print(valores)


fg=0
qmentrou=[]
ondentrou=[]
while fg < len(valores):
    
    Nmmr=valores[fg]
    Nmmr2=Nmmr[0]
    Nmmr3=Nmmr[1]
    
    qmentrou.append(Nmmr2)
    ondentrou.append(Nmmr3)
    fg=fg+1




comandd2 = "SELECT * FROM interpalsMSG"
cursor.execute(comandd2)
valores2 = cursor.fetchall()
#print(valores2)

Nmr = valores2[0]
Nmr2= Nmr[0]




API_TOKEN="TELEGRAM BOT TOKEN"



bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['quem'])
def responderQuem(message):
    #cid= message.chat.id
    i=0
    tamanho = len(qmentrou)/2
    if len(qmentrou)%2 ==1:
        tamanho = tamanho+1
    while i < tamanho:
        print(i)
        print((len(qmentrou)/2))
        msg= bot.send_message(message.chat.id,qmentrou[i] + "entrou, local: " + ondentrou[i])
        i=i+1

@bot.message_handler(commands=['mensagens'])
def responderMsg(message):
    #cid= message.chat.id
    msg= bot.reply_to(message,"Numero de Mensagens :" + str(Nmr2))


bot.polling()
 

    banco.commit()
    item=item+1