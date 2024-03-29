from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    
    vector = SearchVector("name", "description")
    squery = SearchQuery(query)
    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
''' keywords = [word for word in query.split() if len(word) > 2]
    
    q_objects = Q()
    
    for keyword in keywords:
        q_objects |= Q(description__icontains=keyword)
        q_objects |= Q(name__icontains=keyword)
        
    return Products.objects.filter(q_objects)'''