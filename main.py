# pip install pdfplumber
# pip install gTTS
import pdfplumber
from gtts import gTTS

# https://www.youtube.com/watch?v=XQqDMkwdAQw
# Python Text To Speech Tutorial - How to make an Audiobook with Python
 # https://github.com/tombaranowicz/PythonAudiobookGenerator/blob/main/pythonTextToSpeech.py


"""
Other tutorials:

https://www.youtube.com/watch?v=Flm2YHEFd5A
https://www.youtube.com/watch?v=9G47uuBTz04
https://www.youtube.com/watch?v=LXsdt6RMNfY


"""


# article source: https: // www.wired.com/story/what-forest-floor-playgrounds-teach-us-about-kids-and-germs/
article = """
AS DUSK FELL on the Finnish city of Lahti on a still chilly day in May 2016, a crew of workers let themselves into 
the yard of an empty daycare center. Underneath the swings and jungle gyms, they installed squares of forest 
floor—scruffy shrubs, shin-high berry bushes, wispy meadow grasses, and velvety mounds of moss—harvested from 
the woods somewhere in a less developed part of the country. Around the edges, they put in soft green sod. 
In the morning, when the children arrived, they found their playground—formerly a drab patchwork of asphalt, 
gravel, and sand—transformed overnight into micro-oases of wilderness.

This scenario played out three more times that month at daycares in Lahti, and 500 miles to the west, in the 
city of Tampere. It wasn’t the work of some nature-loving guerrilla artists, but the start of an ambitious 
science experiment to find out if the lack of microbes in paved-over urban environments could be turning people’s 
immune systems against them. “There is this ‘biodiversity hypothesis,’ that in the absence of diverse environmental 
microbiota, people are more likely to get immune-mediated diseases,” says Aki Sinkkonen, an evolutionary ecologist 
at the Natural Resources Institute Finland. “But no one had really tested this with children.”

"""

####### ARTICLE
def wired_article():
    language = 'en'
    gtts_transformer = gTTS(text=article, lang=language)
    gtts_transformer.save("wired_article.mp3")
    print("WORK DONE")

###### PDF
def extract_text_from_pdf(pdf, page):

    pdf_path = pdf
    pdf = pdfplumber.open(pdf_path)
    page = pdf.pages[page]
    text = page.extract_text()
    print(text)
    pdf.close()
    return text


def text_to_audio(text, title):
    language = 'en'
    gtts_transformer = gTTS(text=text, lang=language)
    gtts_transformer.save(f"{title}.mp3")
    print("WORK DONE")


text = extract_text_from_pdf("very-short-english-stories.pdf", 12)

text_to_audio(text, "short story")