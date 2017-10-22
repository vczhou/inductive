from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect

from .models import Chapter, Question
from .forms import QuestionForm
from .bibles_api import BiblesAPI
# Create your views here.
 
# def chapter_questions(request, )
def index(request):
    return render(request, 'index.html', {})

def chap_view(request, bk, chapter):
    try:
        chapter_obj = Chapter.objects.get(book=str(bk), chap = int(chapter))
        bib = BiblesAPI("ESV")
        passage = bib.esv(bk,int(chapter))
    except:
        raise Http404("Stop that!")
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            q = Question(reference=chapter_obj, question_text=form.cleaned_data['question'])
            # print('xd')
            q.save()
            return redirect('chap_view', bk, chapter)
    else:
        form = QuestionForm()
    return render(request, 'chapter.html', {
        'book': chapter_obj.book,
        'chapter': chapter_obj.chap,    
        'form': form,
        'questions': chapter_obj.points_to.all(),
        'passage': passage
    })