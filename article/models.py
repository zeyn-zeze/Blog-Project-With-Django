from django.db import models

class Article(models.Model):

    author = models.ForeignKey("auth.user",on_delete= models.CASCADE,verbose_name="Yazar") #on-delete user silinirse o usera ait tüm makaleler silinir.
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")

    def __str__(self):
        return self.title
    



