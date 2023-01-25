# to render html webpages
import random
from django.http import HttpResponse
from articles.models import Article


def home_view(request):
    " take in a request django sends a request  return html response we pick to return a response"

    name = 'halima'  # hard coded
    random_id = random.randint(1, 4)

    # from the database

    article_obj = Article.objects.get(id=random_id)
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "context": article_obj.content

    }

    # django templates
    html_string = """
    
    <h1>{title} (id: {id}!</h1>)
    <p> {content}!</p>
    
    """   .format(**context)
    return HttpResponse(html_string)
