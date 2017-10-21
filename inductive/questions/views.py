from django.http import Http404
from django.shortcuts import render, HttpResponse

from .models import Chapter
# Create your views here.

# def chapter_questions(request, )

def index(request, bk, chap):
    print(bk, chap)
    try:
        chapter = Chapter.objects.get(book=str(bk), chapter = int(chap));
    except:
        raise Http404("Stop that!")
    return HttpResponse("<html><body>Book: %s. Chapter:</body></html>" %chapter.book)