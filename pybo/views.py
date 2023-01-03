from django.shortcuts import render

#요청에 대한 응답을 할때 사용한다
from django.http import HttpResponse

from django.shortcuts import render
from .models import Question

# 오류를 조정하는 코드
from django.shortcuts import render, get_object_or_404


# #request는 HTTP 요청 객체
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


def index(request):
    # 질문 목록 데이터를 얻을 수 있음
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    # question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML 생성후 리턴
    # pybo/question_list.html은 템플릿이라고 한다 (템플릿 파일 : 파이썬 데이터를 읽어서 사용할 수 있는 HTML 파일이다.)
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # 그냥 불러서 오는 코드
    # question = Question.objects.get(id=question_id)
    # 만일 데이터를 가지고 오고 오류가 발생 했을 때 4xx오류로 변경하는 코드
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
