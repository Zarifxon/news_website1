from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify






# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status= News.Status.Published)



class Category(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"





    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images', blank=True, null=True)

    #category bilan newsni bog'laymiz
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)

    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    upload_time =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default = Status.Draft)


    view_count= models.IntegerField(default=0)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish_time'] #Yangilikni oxirgisini eng yuqorida  chiqaradi

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while News.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)




#
# Draft = qoralama
# published = jo'natilgan'



class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    massage = models.TextField()

    def __str__(self):
        return self.email


# comment
class Comment(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['created_time']
    def __str__(self):
        return f"Comment - {self.body} by {self.user}"
