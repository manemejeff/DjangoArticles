from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article


def home_view(request):
    """
    Take in a request
    Return HTML as a response
    :param request:
    :return:
    """
    article_obj = Article.objects.get(id=1)
    article_list = Article.objects.all()
    context = {
        'object_list': article_list,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }
    HTML_STRING = render_to_string('home-view.html', context=context)

    return HttpResponse(HTML_STRING)
