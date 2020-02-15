from django.shortcuts import render
from . models import Item, ItemImage, PopularProducts, NewArrivals
from django.http import Http404
from marketing.models import MarketingMessage, Slider
# Create your views here.



def search(request):
	try:
	    q = request.GET.get('q')
	except:
		q = None
	if q:
		items = Item.objects.filter(title__icontains=q)
		context = {"query": q, "items": items}
		template = 'results.html'
	else:
		template = 'home.html'
		context={}
	
	return render(request, template, context)



def home(request):
	sliders = Slider.objects.all_featured()
	items = Item.objects.all()
	populars = PopularProducts.objects.all()
	arrivals = NewArrivals.objects.all()
	marketing_message = MarketingMessage.objects.all()[0]
	
	context={'items': items,
			'populars': populars,
			'arrivals': arrivals,
			'marketing_message':marketing_message,
			'sliders': sliders
			}
	return render(request, 'index.html', context)



def all(request):
	populars = PopularProducts.objects.all()
	arrivals = NewArrivals.objects.all()
	items = Item.objects.all()
	context={'items': items,
			'populars': populars,
			'arrivals': arrivals

			}

	return render(request, 'all.html', context)


def single(request, slug):
	try:
		item = Item.objects.get(slug=slug)
		# images = item.itemimage_set.all()
		images = ItemImage.objects.filter(item=item)
		context={'item': item, 'images': images }

		return render(request, 'single.html', context)
	except:
		raise Http404
