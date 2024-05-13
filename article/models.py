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
    
    class Meta:
        ordering = ['-create_date']
    

class Comment(models.Model):
    
   article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
   
   comment_author = models.CharField(max_length=50,verbose_name="İsim")
   comment_content = models.CharField(max_length=200,verbose_name="Yorum")
   comment_date = models.DateTimeField(auto_now_add=True)
   def __str__(self) :
        return self.comment_content
   class Meta:
        ordering = ['-comment_date']

