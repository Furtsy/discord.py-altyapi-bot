'''
önemli açıklama bu kod Kong tarafından yazılmıştır izin verilmeyen kişiler tarafından paylaşılması kesinlikte yasaktır
nasıl çalıştırılır;
python un kendi sitesinde python u indirin ardından cmd yi açın sonra dosya konumuna girin ardından python saraç.py yazın Not:Tokeni girmeyi unutmayın
Dosya konumundan nasıl açılır?
Cevap: https://prnt.sc/rh3v1j burdaki yeri ctrl+a yapıp siliyoruz ardından cmd yazıyoruz
'''
import discord #Bu satır hata verirse terminale/cmd ye python3 -m pip install discord.py yazın  //CODARE
from discord.ext import commands #NOT KIMISINI OKUYUN KONG/EMİRHAN SARAÇ
from discord.utils import find #Token son satırlarda
import random #NOT KIMISINI OKUYUN KONG/EMİRHAN SARAÇ
import asyncio
import platform
#en son satıra token yazıyorsunuz nereye yazacağını belirtim 

def prefix(bot, message):
    
    # gayet basit bir şekilde prefix eklenebiliyor
    prefixler = ['!', 'saraç!', 'k!']

    # mesaj dm den mi yoksa sunucudan mı gelmiş ona bakar
    if not message.guild:
        # sadece dm için ? kullanmaya açık
        return '?'

    # eğer bot etiketlenirse prefix lsitesini atar
    return commands.when_mentioned_or(*prefixler)(bot, message)

komutlar = ['cogs.emirhan'] 
'''
üstdeki komutlar kısmında cogs da açtığınız py dosyasının ismini gireceksiniz örneğin;
komutlar = ['cogs.emirhan',
            'cogs.deneme',
            'cogs.ban']  
            gibi
'''

bot = commands.Bot(command_prefix=prefix, description='örnek')

if __name__ == '__main__': 
    for extension in komutlar:
        bot.load_extension(extension)

# bot açıldığında bilgileri konsolda göstermeye yarar
@bot.event
async def on_ready():
    print('-------------------------')     
    print('Giriş Yaptım!')                  
    print('Botun İsmi : ' + bot.user.name)  
    print('ID   : ' + str(bot.user.id))
    print(f"discord.py versiyon: {discord.__version__}")
    print(f"Python versiyon: {platform.python_version()}")
    print(f"Çalışma Yeri: {platform.system()} v{platform.version()}")
    print("Bot Komut Bilgileri\nKomut Sayısı {0}.Komutlarda aktif {1} \n".format(
        str(len(bot.cogs)), str(len(bot.commands))))     
    print('Made by Kong')           
    print('-------------------------')    
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Video")) #oynuyoru buradn değişebilirsiniz

# burdan token girebilrisiniz Emirhan Saraç/Kong
bot.run('NjgwNjYzNjI2NTExNTQ4NDU5.XlFOTw.4h22ctlkRvFyTIuFXWJv8Uyf9E4')