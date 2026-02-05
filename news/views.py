from django.shortcuts import render, get_object_or_404
from .models import News, Category


def news_detail(request, slug):
    # news_detail nomi urls.py dagi name='news_detail' bilan bir xil bo'lishi shart
    news = get_object_or_404(News, slug=slug)
    news.views += 1
    news.save()

    categories = Category.objects.all()
    return render(request, 'news/detail.html', {'news': news, 'categories': categories})


def home(request):
    region = request.GET.get('region')
    category_slug = request.GET.get('category')  # Kategoriya filtrini qo'shdik

    # Barcha yangiliklarni olish (avval hammasini olib, keyin saralaymiz)
    latest_news = News.objects.all().order_by('-created_at')

    is_filter_view = False

    # 1. VILOYAT BO'YICHA FILTR
    if region:
        latest_news = latest_news.filter(region=region)
        is_filter_view = True

    # 2. KATEGORIYA BO'YICHA FILTR
    if category_slug:
        latest_news = latest_news.filter(category__slug=category_slug)
        is_filter_view = True

    # 3. ASOSIY SAHIFA (FILTRSIZ) HOLATI
    top_news = None
    if not is_filter_view:
        # Faqat filtr yo'q bo'lsa "Top" yangilikni chiqaramiz
        top_news = News.objects.filter(is_top=True).first()
        if top_news:
            latest_news = latest_news.exclude(id=top_news.id)[:12]
        else:
            latest_news = latest_news[:12]

    return render(request, 'news/home.html', {
        'top_news': top_news,
        'latest_news': latest_news,
        'is_filter_view': is_filter_view,
        'categories': Category.objects.all()
    })