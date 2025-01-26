from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.http import request
from django.utils.safestring import mark_safe

from utility.models import Social_Site
# Create your models here.


class About_Page(models.Model):
    image = models.ImageField(upload_to='logo/')
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    mission = models.CharField(blank=True,max_length=2055)
    vision = models.CharField(blank=True,max_length=2000)
    values = models.CharField(blank=True,max_length=2055)
    aboutus = RichTextUploadingField(blank=True)
    experience = models.CharField(max_length=150,blank=True,)
    technician = models.CharField(max_length=150,blank=True,)

    def __str__(self):
        return self.title
    
        
    class Meta:
        verbose_name_plural='2. About Page'


class Contact_Page(models.Model):
    image = models.ImageField(upload_to='logo/')
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contctus = RichTextUploadingField(blank=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='3. Contact Page'



class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    logo = models.ImageField(upload_to='logo/')
    testmonial_bg = models.ImageField(upload_to='logo/')
    nav_color_1 = models.CharField(max_length=150,blank=True,)
    nav_color_2 = models.CharField(max_length=150,blank=True,)
    nav_color_3 = models.CharField(max_length=150,blank=True,)
    footer_color_1 = models.CharField(max_length=150,blank=True,)
    footer_color_2 = models.CharField(max_length=150,blank=True,)
    text_color = models.CharField(max_length=150,blank=True,)
    title = models.CharField(max_length=150)
    OurServices_title = models.CharField(blank=True,max_length=150)
    product_title = models.CharField(blank=True,max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    location = models.CharField(blank=True,max_length=30)
    phone = models.CharField(blank=True,max_length=15)
    whatsapp = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    google_map = models.CharField(blank=True,max_length=1000)
    copy_right = models.CharField(blank=True,max_length=100)
    icon = models.ImageField(upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    some_faq_title = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
        
    class Meta:
        verbose_name_plural='9. Web Site Setting'


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=False,max_length=20)
    email= models.EmailField(blank=False,max_length=50)
    subject= models.CharField(blank=False,max_length=50)
    message= models.TextField(blank=False,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='1. ContactMessage'


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : TextInput (attrs={'class': 'input','placeholder':'Name & Surname',} ),
            'subject' : TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }

class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
    status=models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Our_Team(models.Model):
    title = models.CharField(max_length=50,blank=True)
    designation = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=True)
    facebook = models.CharField(max_length=150,blank=True)
    twitter = models.CharField(max_length=150,blank=True)
    instagram = models.CharField(max_length=150,blank=True)
    pinterest = models.CharField(max_length=150,blank=True)
    youtube = models.CharField(max_length=150,blank=True)
    featured = models.BooleanField(default=False)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='4. Our Team'
   

class Testimonial(models.Model):
    name = models.CharField(max_length=50,blank=True)
    designation = models.CharField(max_length=50,null=True, blank=True)
    comment = models.CharField(max_length=500,blank=True)
    image = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='5. Testimonial'


class Social_Link(models.Model):
    social_site = models.ForeignKey(Social_Site, on_delete=models.CASCADE)
    our_team = models.ForeignKey(Our_Team, on_delete=models.CASCADE) # many to one relation with Brand
    link=models.CharField(max_length=100)
    
    def __str__(self):
        return self.link    
    class Meta:
        verbose_name_plural='6. Social Link'


class Offer(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(blank=True,upload_to='images/')
    image_2=models.ImageField(blank=True,upload_to='images/')
    image_3=models.ImageField(blank=True,upload_to='images/')
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='7. Offer'


class Slider(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50,blank=True,)

    image=models.ImageField(upload_to='images/')
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='8. Slider'

class Content_Slider(models.Model):
    title = models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='11. Content_Slider'



class Banner(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=150)
    image=models.ImageField(blank=True,upload_to='images/')
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='10. Banner'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    sub_title = models.CharField(max_length=150)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    class Meta:
        verbose_name_plural='10. Gallery Page'