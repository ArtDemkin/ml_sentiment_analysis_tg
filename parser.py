from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
import csv
api_id = 123 #вводим свои данные
api_hash = '123' #вводим свои данные
phone = '+123' #вводим свои данные

client = TelegramClient(phone, api_id, api_hash)

client.start()
 
chats = []
last_date = None
chunk_size = 200
groups = []
result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash = 0
        ))
chats.extend(result.chats)
for chat in chats:
   try:
       if chat.megagroup== True:
           groups.append(chat)
   except:
       continue
print("Выберите группу для парсинга сообщений и членов группы:")
i=0
for g in groups:
   print(str(i) + "- " + g.title)
   i+=1
g_index = 0
target_group=groups[int(g_index)]
print("Узнаём пользователей...")

 
offset_id = 0
limit = 100
all_messages = []
total_messages = 100        #количество спаршенных сообщений если 0, то все
total_count_limit = 100     #количество спаршенных сообщений если 0, то все
 
while True:
   history = client(GetHistoryRequest(
       peer=target_group,
       offset_id=offset_id,
       offset_date=None,
       add_offset=0,
       limit=limit,
       max_id=0,
       min_id=0,
       hash=0
   ))
   if not history.messages:
       break
   messages = history.messages
   for message in messages:
       all_messages.append(message.message)
   offset_id = messages[len(messages) - 1].id
   if total_count_limit != 0 and total_messages >= total_count_limit:
       break
  
print("Сохраняем данные в файл...")
with open("chats.csv", "w", encoding="UTF-8", newline='\n') as f:
   writer = csv.writer(f, delimiter=",", lineterminator="\n")
   for message in all_messages:
       writer.writerow([message])  
print('Парсинг сообщений группы успешно выполнен.')