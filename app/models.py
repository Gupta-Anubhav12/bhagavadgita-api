from pydantic import BaseModel
from typing import List


example_chapters_list = [
    {
      "chapter_number": 1,
      "name": "अर्जुनविषादयोग",
      "name_translation": "Arjuna Visada Yoga",
      "name_transliterated": "Arjun Viṣhād Yog",
      "name_meaning": "Arjuna's Dilemma",
      "chapter_summary": "The first chapter of the Bhagavad Gita - \"Arjuna Vishada Yoga\" introduces the setup, the setting, the characters and the circumstances that led to the epic battle of Mahabharata, fought between the Pandavas and the Kauravas. It outlines the reasons that led to the revelation of the of Bhagavad Gita.\nAs both armies stand ready for the battle, the mighty warrior Arjuna, on observing the warriors on both sides becomes increasingly sad and depressed due to the fear of losing his relatives and friends and the consequent sins attributed to killing his own relatives. So, he surrenders to Lord Krishna, seeking a solution. Thus, follows the wisdom of the Bhagavad Gita.",
      "verses_count": 47
    },
    {
      "chapter_number": 2,
      "name": "सांख्ययोग",
      "name_translation": "Sankhya Yoga",
      "name_transliterated": "Sānkhya Yog",
      "name_meaning": "Transcendental Knowledge",
      "chapter_summary": "The second chapter of the Bhagavad Gita is \"Sankhya Yoga\". This is the most important chapter of the Bhagavad Gita as Lord Krishna condenses the teachings of the entire Gita in this chapter. This chapter is the essence of the entire Gita. \n\"Sankhya Yoga\" can be categorized into 4 main topics - \n1. Arjuna completely surrenders himself to Lord Krishna and accepts his position as a disciple and Krishna as his Guru. He requests Krishna to guide him on how to dismiss his sorrow.\n2. Explanation of the main cause of all grief, which is ignorance of the true nature of Self.\n3. Karma Yoga - the discipline of selfless action without being attached to its fruits.\n4. Description of a Perfect Man - One whose mind is steady and one-pointed.",
      "verses_count": 72
    },
]

example_verses_list = [  
    {
      "title": "Verse 1",
      "chapter_number": 1,
      "verse_number": "1",
      "text": "धृतराष्ट्र उवाच |\nधर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः |\nमामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय ॥1॥\n",
      "transliteration": "dhṛitarāśhtra uvācha\ndharma-kṣhetre kuru-kṣhetre samavetā yuyutsavaḥ\nmāmakāḥ pāṇḍavāśhchaiva kimakurvata sañjaya\n",
      "meaning": "Dhritarastra said: O Sanjaya, what did my sons and the sons of Pandu actually do when, eager for battle, they gathered together on the holy field of Kuruksetra?",
      "word_meanings": "dhṛitarāśhtraḥ uvācha—Dhritarashtra said; dharma-kṣhetre—the land of dharma; kuru-kṣhetre—at Kurukshetra; samavetāḥ—having gathered; yuyutsavaḥ—desiring to fight; māmakāḥ—my sons; pāṇḍavāḥ—the sons of Pandu; cha—and; eva—certainly; kim—what; akurvata—did they do; sañjaya—Sanjay\n"
    },
    {
      "title": "Verse 2",
      "chapter_number": 1,
      "verse_number": "2",
      "text": "सञ्जय उवाच ।\nदृष्ट्वा तु पाण्डवानीकं व्यूढं दुर्योधनस्तदा ।\nआचार्यमुपसङ्गम्य राजा वचनमब्रवीत् ॥2॥\n",
      "transliteration": "sañjaya uvācha\ndṛiṣhṭvā tu pāṇḍavānīkaṁ vyūḍhaṁ duryodhanastadā\nāchāryamupasaṅgamya rājā vachanamabravīt\n",
      "meaning": "Sanjaya said: But then, seeing the army of the Pandavas in battle array, King Duryodhana approached his teacher (Dronacharya) and spoke the following words:",
      "word_meanings": "sanjayaḥ uvācha—Sanjay said; dṛiṣhṭvā—on observing; tu—but; pāṇḍava-anīkam—the Pandava army; vyūḍham—standing in a military formation; duryodhanaḥ—King Duryodhan; tadā—then; āchāryam—teacher; upasaṅgamya—approached; rājā—the king; vachanam—words; abravīt—spoke\n"
    },
]

class Chapter(BaseModel):
    chapter_number: int = 1
    name: str = "अर्जुनविषादयोग"
    name_translation: str = "Arjuna Visada Yoga"
    name_transliterated: str = "Arjun Viṣhād Yog"
    name_meaning: str = "Arjuna's Dilemma"
    chapter_summary: str = """The first chapter of the Bhagavad Gita - \"Arjuna Vishada Yoga\" introduces the setup, the setting, the characters and the circumstances that led to the epic battle of Mahabharata, fought between the Pandavas and the Kauravas. It outlines the reasons that led to the revelation of the of Bhagavad Gita.\nAs both armies stand ready for the battle, the mighty warrior Arjuna, on observing the warriors on both sides becomes increasingly sad and depressed due to the fear of losing his relatives and friends and the consequent sins attributed to killing his own relatives. So, he surrenders to Lord Krishna, seeking a solution. Thus, follows the wisdom of the Bhagavad Gita."""
    verses_count: int = 47


class AllChapters(BaseModel):
    chapters: List[Chapter] = example_chapters_list


class Verse(BaseModel):
    title: str = "Verse 1"
    chapter_number: int = 1
    verse_number: str = "1"
    text: str = "धृतराष्ट्र उवाच |\nधर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः |\nमामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय ॥1॥\n"
    transliteration: str = "dhṛitarāśhtra uvācha\ndharma-kṣhetre kuru-kṣhetre samavetā yuyutsavaḥ\nmāmakāḥ pāṇḍavāśhchaiva kimakurvata sañjaya\n"
    meaning: str = "Dhritarastra said: O Sanjaya, what did my sons and the sons of Pandu actually do when, eager for battle, they gathered together on the holy field of Kuruksetra?"
    word_meanings: str = "dhṛitarāśhtraḥ uvācha—Dhritarashtra said; dharma-kṣhetre—the land of dharma; kuru-kṣhetre—at Kurukshetra; samavetāḥ—having gathered; yuyutsavaḥ—desiring to fight; māmakāḥ—my sons; pāṇḍavāḥ—the sons of Pandu; cha—and; eva—certainly; kim—what; akurvata—did they do; sañjaya—Sanjay\n"


class AllVerses(BaseModel):
    verses: List[Verse] = example_verses_list
