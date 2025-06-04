from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import title, slugify

Jop_Type=(('Full Type','Full Type'),
          ('Part Type','Part Type'),)

def image_upload(instance, filename):
    imagename, extension = filename.rsplit(".", 1)
    return f"jobs/{instance.title}_{instance.id}.{extension}"





class Job(models.Model):
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=Jop_Type)
    decreption=models.TextField(max_length=1000)
    date_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category= models.ForeignKey('Category',on_delete=models.CASCADE ,null=True, blank=True)
    imge = models.ImageField( upload_to=image_upload, blank=True, null=True )
    slug=models.SlugField(blank=True, null=True)



    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job=models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    website=models.URLField()
    cv=models.FileField(upload_to='apply')
    coverletter=models.TextField()
    creat_at = models.DateTimeField( auto_now=True )

    def __str__(self):
        return self.name


