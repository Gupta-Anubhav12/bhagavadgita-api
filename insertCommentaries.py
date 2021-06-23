import json
from database import engine
from sqlalchemy import  MetaData
from sqlalchemy.orm import  sessionmaker
from models import gitaChapter, gitaCommentary, gitaVerse,gitaTranslation

Session = sessionmaker(bind=engine)
session = Session()     

# meta = MetaData()

with open('data/commentary.json','r',encoding='utf8') as file:
        
    
    li = []
    data = json.loads(file.read().encode('utf-8'))

    for i in data:
        li.append(gitaCommentary(
            description=i.get('description'),
            authorName=i.get('authorName'),
            lang = i.get('lang'),
            verseNumber = i.get('verseNumber'),
       
        )) 
    session.add_all(li)
    session.commit()
   