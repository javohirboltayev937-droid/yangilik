from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class News(models.Model):
    REGION_CHOICES = [
        ('toshkent', 'Toshkent'),
        ('andijon', 'Andijon'),
        ('fargona', 'Farg\'ona'),
        ('namangan', 'Namangan'),
        ('samarqand', 'Samarqand'),
        ('buxoro', 'Buxoro'),
        ('navoiy', 'Navoiy'),
        ('qashqadaryo', 'Qashqadaryo'),
        ('surxondaryo', 'Surxondaryo'),
        ('jizzax', 'Jizzax'),
        ('sirdaryo', 'Sirdaryo'),
        ('xorazm', 'Xorazm'),
        ('qoraqalpogiston', 'Qoraqalpog\'iston'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.CharField(max_length=50, choices=REGION_CHOICES, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_top = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"