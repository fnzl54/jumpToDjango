from django.shortcuts import render

from django.http import HttpResponse #요청에 대한 응답을 할때 사용한다


def index(request): #request는 HTTP 요청 객체
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
