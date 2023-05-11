from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    """
    QuestionManager - менеджер модели Question
        new - метод возвращающий последние добавленные вопросы
        popular - метод возвращающий вопросы отсортированные по рейтингу
    """
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    """
    Question - вопрос
    title - заголовок вопроса
    text - полный текст вопроса
    added_at - дата добавления вопроса
    rating - рейтинг вопроса (число)
    author - автор вопроса
    likes - список пользователей, поставивших "лайк"
    """
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_ad = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(to=User, related_name='question_like_user')

 
   # def __unicode__(self):
   # return self.title

   # def get_absolute_url(self):
   # return '/post/%d/' % self.pk
    

class Answer(models.Model):
    """
    Answer - ответ
    text - текст ответа
    added_at - дата добавления ответа
    question - вопрос, к которому относится ответ
    author - автор ответа
    """
    text = models.TextField()
    added_ad = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(to=Question, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    objects = QuestionManager() 
   # def __unicode__(self):
   # return self.title

   # def get_absolute_url(self):
   # return '/post/%d/' % self.pk

