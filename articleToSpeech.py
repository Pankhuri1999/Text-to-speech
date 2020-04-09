#This code converts any text on any website into speech. You just have to provide the link of the article
# Code will not work for PDF files


article = Article('Link of article')

article.download() 
article.parse() 
nltk.download('punkt') 
article.nlp() 


text = article.text


print(text)


language = 'en' #English  # 'hi' for Hindi


myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("read_article.mp3")


os.system("start read_article.mp3") 
