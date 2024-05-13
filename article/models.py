from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):

    author = models.ForeignKey("auth.user",on_delete= models.CASCADE,verbose_name="Yazar") #on-delete user silinirse o usera ait tüm makaleler silinir.
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin")

    def __str__(self):
        return self.title
    



