from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem

def hello_world(request):
    # products = Product.objects.order_by('-title')[:5]

    # content_type = ContentType.objects.get_for_model(Product)
    # query_set = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )

    # collection = Collection.objects.get(pk=1)
    # collection.title = 'Edided Game'
    # collection.save()

    Collection.objects.filter(pk=1).update(featured_product=None)

    return render(request, 'hello.html')