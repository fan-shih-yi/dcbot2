import discord

client = discord.Client()

@client.event
async def on_ready():
    print('目前登入身分:', client.user)
    game = discord.Game('lol')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user :
        return
    if message.content == "test" or message.content == "Test":
        await message.channel.send('already')
    if message.content == "偉晏" or message.content == "光頭":
        await message.channel.send('是智障')
        await message.channel.send('也是白癡')
    if message.content == "昊陞" or message.content == "胖子":
        await message.channel.send('加油站旁的暗殺心，2024年肄業於國立苗栗農工，2025修業年限已滿，未取得高中文憑。無前科。')
    if message.content == "彥嘉" or message.content == "嘉嘉":
        await message.channel.send('炸機達人又名炸雞劊子手，光榮戰績有:metoo事件受害者范世易確診當晚，送了一桶炸雞到他家。')
    if message.content == "國凱" or message.content == "曾國凱":
        await message.channel.send('林瑀豆殺手，曾代表苗栗縣參與原神比賽，並勇奪第一的男人。曾涉嫌性侵孫偉晏豈料未得手，2024年與孫瑋瑄交往，而目光卻是她哥哥，多年前性侵未得手，現在等待時機伺機而動。')
    if message.content == "阿邱" or message.content == "邱世璿":
        await message.channel.send('羅莉殺手aka巧寧寶貝，2021年暑假帶著對於未來美好的憧憬畢業於苗栗縣縣立建國國民中學。妹妹於2026年被哥哥的國中同學謝承恩，在性愛過程中被幹死')
    if message.content == "承恩" or message.content == "謝承恩":
        await message.channel.send('幹死邱千雨的男人，犯下多筆強姦罪入獄五次，受害者有孫瑋瑄、邱千雨、范世易等兩人。受訪過程中還對記者孫偉晏偏偏起手，真是窮兇惡極的強姦犯呢。')
    if message.content == "世易" or message.content == "范世易":
        await message.channel.send('南寮漁港、可悲高中生、me too 事件受害者之一，同時是位好同學，偉彥的一句叫世易去修機器人，他索性直接做一支給他，還充滿了對偉晏無止境的愛。')
    if message.content == "聖潔" or message.content == "聖傑":
        await message.channel.send('銅鑼灣扛壩子、代表國立苗栗農工參與第二十三屆全民高等中學炸雞杯最後一名。')
    if message.content == "最新消息" or message.content == "新聞":
        await message.channel.send('驚爆熱死!!!位於苗栗縣頭份市一名就讀竹南高中的學生，晚上在家竟然突然暴斃，法醫鑑定死因可排除他殺，死因可能為天氣太熱，真是細狗一條。轉載TVBS新聞報導')
    if message.content == "孫同學" or message.content == "猝死":
        await message.channel.send('2023/7/5凌晨猝死於家中，數名國中同學與老師都表示該名學生很優秀、很孝順，聽到這噩耗也十分驚訝，為了省一晚的冷氣費搞到全村吃席，節哀。')
    if message.content == "出殯" or message.content == "告別式":
        await message.channel.send('7/5猝死於家中的孫同學，告別式舉辦於7/7~7/10，大坪頂納骨塔(永生園)服務一手承辦，詳情請至電0971-135-016，請各路好友撥空前來與死者見最後一面，做個告別，讓死者沒有後顧之憂與菩薩去取經。')
    if message.content == "可憐" or message.content == "可悲":
        await message.channel.send('想想孫偉晏，你已經很幸福了，別再自暴自棄，努力的活下去吧，你很棒的')
    if message.content == "孫偉晏超可憐" or message.content == "孫偉晏超可悲":
        await message.channel.send('我超級認同你的想法，要不是范世易有學會乳核給機器人自動聊天功能，我一定跟你們易起嘴可悲小孩孫偉晏777。')
    if message.content == "范世易超可憐" or message.content == "范世易超可悲":
        await message.channel.send('哪有孫偉晏來的可憐與可悲呢哪有孫偉晏來的可憐與可悲呢?')
    if message.content == "哪個破腦製造這個機器人的" or message.content == "哪個智障製造這個機器人的":
        await message.channel.send('超可悲高中生孫偉晏的朋友。')
    if message.content == "還有嗎" or message.content == "你還會講甚麼":
        await message.channel.send('沒了，我暫時想不到還能怎麼嘴孫偉晏了。')

    if message.content.startswith('!'):
      tmp = message.content.split("",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send(tmp[1])

client.run("MTEyNTgxMDY4NzM5OTE4MjMzNg.GTZ6oK.9w98BpZ_9twM5oq4egm2eLkDb49pVAsdmyMqlQ")