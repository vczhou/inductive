import requests
import json

class BiblesAPI():
    _BIBLES_API_KEY = "xdCoUihEKWvpq994hRlGJwyurTTCQs7HOjTt5NAj"
    _API_BASE_URL = "https://bibles.org/v2/"
    _BIBLE_VERSION = "ESV"
    _LANGUAGE = "eng"

    def __init__(self, bible_version="ESV", language="eng"):
          self._BIBLE_VERSION = bible_version
          self._LANGUAGE = language
          print ("Bibles API Key",self._BIBLES_API_KEY)

    def setBibleVersion(self, bible_version="ESV"):
        self._BIBLE_VERSION = bible_version

    def setLanguage(self, language="eng"):
        self._LANGUAGE = language

    # def doRequest(self, url, payload={}):
    #     print ("In do request")
    #     r = requests.get(url, params=payload,
    #                      auth=(self._BIBLES_API_KEY, 'pass'))
    #
    #     r.raise_for_status()
    #     print(r.url, r.headers)
    #     print ("hellooo")
    #
    #     print (r)
    #     return r.json()

    def getResponse(self, url):
        s = requests.Session()
        s.auth = (self._BIBLES_API_KEY, 'X')
        headers = {'content-type': 'application/json'}
        try:
            r = s.get(url, headers=headers)
            data = r.json()
            print ("r", r)
        except Exception as e:
            print ("Raised exception")
            data = {"error": e}
        return data

    def chapter(self, book_name, chapter_number):
        url = self._API_BASE_URL + "chapters/" + self._LANGUAGE + "-" + \
              self._BIBLE_VERSION + ":" + book_name + "." + \
              str(chapter_number) + ".js"

        payload = {"include_marginalia": True,}
        print ("Get passage", url, payload)
        response = self.getResponse(url)
        text = response['response']['chapters'][0]['text']
        print ("Text:", text)
        return text

if __name__ == '__main__':
    testApi = BiblesAPI("ESV")
    r = testApi.chapter("John", 1)

