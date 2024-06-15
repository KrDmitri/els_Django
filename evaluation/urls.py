from django.urls import path


from .views import get_evaluated_price


app_name = 'evaluation-namespace'


urlpatterns = [
    path("get-price/", get_evaluated_price, name='get_chatbot_answer'),

]