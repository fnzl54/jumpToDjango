from django.db import models

#Question 모델의 속성 설정 
class Question(models.Model):
    # 제한된 글자수 속성 지정
    subject = models.CharField(max_length=200)
    # 글자수를 제한 할 수 없는 텍스트
    content = models.TextField()
    # 시간과 관한 속성
    create_date = models.DateTimeField()


class Answer(models.Model):
    # 대답 특성의 경우 키를 활용하여 가지고 데이터 사용, https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    # 출력시에 id값 대신 제목을 표시
    def __str__(self):
        return self.subject
