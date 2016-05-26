from django.shortcuts import render
from .models import ArticleImage, Article, Zno, ZnoDoc, Dpa, DpaDoc, Vchitel, VchitelDoc, Klassam, KlassamDoc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def main(request):
	novosti = Article.objects.all().order_by("-pub_date")

	paginator = Paginator(novosti, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'main.html', {"novosti": contacts})


def novosti(request):
	novosti = Article.objects.all().order_by("-pub_date")
	articleImage = ArticleImage.objects.all()

	paginator = Paginator(novosti, 10) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)

	return render(request, "novosti.html", {"novosti": contacts, "articleImage": articleImage})


def novost(request, article_pk):
	novost = Article.objects.get(pk=article_pk)
	articleImage = ArticleImage.objects.filter(article=article_pk)

	context = {
		'novost': novost,
		'articleImage': articleImage,

	}

	return render(request, "novost.html", context)


def history(request):
	history = History.objects.all()
	historyImage = HistoryImage.objects.filter()

	context = {
		'history': history,
		'historyImage': historyImage,

	}

	return render(request, "history.html", context)



def dpa(request):
	dpa = Dpa.objects.all()
	dpadoc = DpaDoc.objects.all()

	context = {
	'dpa': dpa,
	'dpadoc': dpadoc
	}
	return render(request, 'dpa.html', context)


def zno(request):
	zno = Zno.objects.all()
	znodoc = ZnoDoc.objects.filter()

	context = {
	'zno': zno,
	'znodoc': znodoc
	}
	return render(request, 'zno.html', context)


def vchitel(request):
	vchitel = Vchitel.objects.all()
	vchiteldoc = VchitelDoc.objects.filter()

	context = {
	'vchitel': vchitel,
	'vchiteldoc': vchiteldoc
	}
	return render(request, 'vchitel.html', context)


def klassam(request):
	klassam = Klassam.objects.all()
	klassamdoc = KlassamDoc.objects.filter()

	context = {
	'klassam': klassam,
	'klassamdoc': klassamdoc
	}
	return render(request, 'classam.html', context)


