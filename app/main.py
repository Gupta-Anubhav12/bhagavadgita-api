import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import logging
import requests
from utils import graphql_query
from models import AllChapters, Chapter, Verse, AllVerses
from functools import lru_cache
import config


logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)


@lru_cache()
def get_settings():
    return config.Settings()


app = FastAPI(
    title="Bhagavad Gita API",
    description="The Bhagavad Gita Application Programming Interface (API) allows a web or mobile developer to use the Bhagavad Gita text in their web or mobile application(s). It is a RESTful API that follows some of the Best Practices for designing a REST API which makes it easy for developers to use and implement.",
    version="2.0",
)

origins = [
    "http://localhost", "http://localhost:3000", "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


# CHAPTERS
@app.get("/v2/chapters/", response_model = AllChapters, tags=["chapters"])
async def get_all_chapters(settings: config.Settings = Depends(get_settings)):
    output = None

    try:
        query = """
            query getAllChapters {
                allGitaChapter(sort: { chapter_number: ASC }) {
                    chapter_number
                    name
                    name_translation
                    name_transliterated
                    name_meaning
                    chapter_summary
                    verses_count
                }
            }
        """

        result = graphql_query("https://08ar7hpl.api.sanity.io/v1/graphql/production/default", query)
        output = result['data']['allGitaChapter']
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Couldn't fetch the chapters.")
    return {"chapters": output}


@app.get("/v2/chapters/{chapter_number}", response_model = Chapter, tags=["chapters"])
async def get_particular_chapter(chapter_number: int, settings: config.Settings = Depends(get_settings)):
    output = None

    try:
        query = """
            query getParticularChapter {
                allGitaChapter(where: {chapter_number: {
                    eq: %s
                }}){
                    chapter_number
                    name
                    name_translation
                    name_transliterated
                    name_meaning
                    chapter_summary
                    verses_count
                }
            }
        """ % (chapter_number)

        result = graphql_query("https://08ar7hpl.api.sanity.io/v1/graphql/production/default", query)
        output = result['data']['allGitaChapter'][0]
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Couldn't fetch the chapter.")
    return output


# VERSES
@app.get("/v2/verses/", response_model = AllVerses, tags=["verses"])
async def get_all_verses_from_all_chapters(settings: config.Settings = Depends(get_settings)):
    output = None

    try:
        query = """
            query getAllVerses {
                allGitaVerse(sort: { verse_order: ASC }) {
                    title
                    chapter_number
                    verse_number
                    text	
                    transliteration
                    meaning
                    word_meanings
                }
            }
        """

        result = graphql_query("https://08ar7hpl.api.sanity.io/v1/graphql/production/default", query)
        output = result['data']['allGitaVerse']
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Couldn't fetch the verses.")
    return {"verses": output}


@app.get("/v2/chapters/{chapter_number}/verses", response_model = AllVerses, tags=["verses"])
async def get_all_verses_from_particular_chapter(chapter_number: int, settings: config.Settings = Depends(get_settings)):
    output = None

    try:
        query = """
            query getAllVersesFromChapter {
                allGitaChapter(where: {chapter_number: {
                    eq: %s
                }}){
                    verses {
                        title
                        chapter_number
                        verse_number
                        text	
                        transliteration
                        meaning
                        word_meanings
                    }
                }
            }
        """ % (chapter_number)

        result = graphql_query("https://08ar7hpl.api.sanity.io/v1/graphql/production/default", query)
        output = result['data']['allGitaChapter'][0]['verses']
        print(output)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Couldn't fetch the verses.")
    return {"verses": output}


@app.get("/v2/chapters/{chapter_number}/verses/{verse_number}", response_model = Verse, tags=["verses"])
async def get_particular_verse(chapter_number: int, verse_number: str, settings: config.Settings = Depends(get_settings)):
    output = None

    try:
        query = """
            query getAllVersesFromChapter {
                allGitaVerse(where: 
                {
                    chapter_number: {
                        eq: %s
                    },
                    verse_number: {
                        eq: %s
                    }
                }){
                    title
                    chapter_number
                    verse_number
                    text	
                    transliteration
                    meaning
                    word_meanings
                }
            }
        """ % (chapter_number, verse_number)

        result = graphql_query("https://08ar7hpl.api.sanity.io/v1/graphql/production/default", query)
        output = result['data']['allGitaVerse'][0]
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Couldn't fetch the verse.")
    return output