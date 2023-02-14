
import requests
import json
from gtts import gTTS 
from moviepy.editor import *

api_key="YOUR API KEY HERE"

def eng():
    try:
        
        
        r = requests.get(api_key)
        




        data = json.loads(r.content)

        #for i in range (0,10):
                #News= data['articles'][i]['title']
                #print('{i}',News)
                #text_w= ('%d)' % (i+1),News)



        News1 = data ['articles'][0]['title']
        print(News1)
        News2 = data ['articles'][1]['title']
        print(News2)
        News3 = data ['articles'][2]['title']
        print(News3)
        News4 = data ['articles'][3]['title']
        print(News4)
        News5 = data ['articles'][4]['title']
        print(News5)
        News6 = data ['articles'][5]['title']
        print(News6)
        News7 = data ['articles'][6]['title']
        print(News7)
        News8 = data ['articles'][7]['title']
        print(News8)
        News9 = data ['articles'][8]['title']
        print(News9)
        News10 = data ['articles'][9]['title']
        print(News10)




        text = "News 1!"+News1+"..."+"News 2!"+News2+"..."+"News 3!"+News3+"..."+"News 4!"+News4+"..."+"News 5!"+News5+"..."+"News 6!"+News6+"..."+"News 7!"+News7+"..."+"News 8!"+News8+"..."+"News 9!"+News9+"..."+"News 10!"+News10
        text_w = "1)"+News1+"\n"+"2)"+News2+"\n"+"3)"+News3+"\n"+"4)"+News4+"\n"+"5)"+News5+"\n"+"6)"+News6+"\n"+"7)"+News7+"\n"+"8)"+News8+"\n9)"+News9+"\n"+"10)"+News10
        #Writing as text
        f = open("eng_news.txt", "w")
        f.write(text_w)
        f.close()

        speech = gTTS(text=text, lang='hi', slow=False)

        speech.save("news_en.mp3")

        


    except :
        print("Only 8 news available...")
        print("")
        print("")
        r = requests.get(api_key)
        




        data = json.loads(r.content)




        News1 = data ['articles'][0]['title']
        print(News1)
        News2 = data ['articles'][1]['title']
        print(News2)
        News3 = data ['articles'][2]['title']
        print(News3)
        News4 = data ['articles'][3]['title']
        print(News4)
        News5 = data ['articles'][4]['title']
        print(News5)
        News6 = data ['articles'][5]['title']
        print(News6)
        News7 = data ['articles'][6]['title']
        print(News7)
        News8 = data ['articles'][7]['title']
        print(News8)


        text = "News 1!"+News1+"..."+"News 2!"+News2+"..."+"News 3!"+News3+"..."+"News 4!"+News4+"..."+"News 5!"+News5+"..."+"News 6!"+News6+"..."+"News 7!"+News7+"..."+"News 8!"+News8
        text_w = "1)"+News1+"\n2)"+News2+"\n3)"+News3+"\n4)"+News4+"\n5)"+News5+"\n6)"+News6+"\n7)"+News7+"\n8)"+News8
       #Writing As Text
       #Writing as text
        f = open("eng_news.txt", "w")
        f.write(text_w)
        f.close()


        speech = gTTS(text=text, lang='hi', slow=False)

        speech.save("news_en.mp3")


        



# Import the audio
    audio1 = AudioFileClip("news_en.mp3")
# Import the Image and set its duration same as the audio
    clip1 = ImageClip("eng.png").set_duration(audio1.duration)
# Set the audio of the clip
    clip1 = clip1.set_audio(audio1)
# Export the clip
    clip1.write_videofile("news_eng.mp4", fps=24)

eng()
