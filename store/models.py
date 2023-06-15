
from django.db import models
from django.contrib.auth.models import User
import os
import datetime

# Create your models here.
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('uploads/',filename)
class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.CharField(max_length=200)
    big_description=models.TextField(max_length=500)
    price=models.IntegerField()
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s%s' %(self.category,self.name)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100,null=False)
    lname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    mobilenumber=models.IntegerField(null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state= models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField(null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=True)
    orderstatus=(
        ('pending','pending'),('Out For Delivery','Out For Delivery'),('completed','completed')
    )
    status=models.CharField(max_length=150,choices=orderstatus,default='pending')
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)

class Orderitems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id,self.order.tracking_no)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobilenumber = models.IntegerField(null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.IntegerField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    product=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="comments")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

class CancerType(models.Model):
    type=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    description=models.TextField()

    def __str__(self):
        return self.type

def get_file_path_chinese(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('chinese_uploads/',filename)
class ChineseCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_chinese,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def get_file_path_hindi(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('hindi_uploads/',filename)
class HindiCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_hindi,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def get_file_path_spanish(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('spanish_uploads/',filename)
class SpanishCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_spanish,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class ChineseComment(models.Model):
#     product=models.ForeignKey(ChineseCategory,on_delete=models.CASCADE,related_name="chinesecomments")
#     commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
#     comment_body=models.TextField()
#     comment_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return "%s %s" %(self.product.name,self.commenter_name.username)

class ChinaComment(models.Model):
    product=models.ForeignKey(ChineseCategory,on_delete=models.CASCADE,related_name="chinacomments")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_chinese,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

class HindiComment(models.Model):
    product=models.ForeignKey(HindiCategory,on_delete=models.CASCADE,related_name="hindicomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_hindi,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

class SpanishComment(models.Model):
    product=models.ForeignKey(SpanishCategory,on_delete=models.CASCADE,related_name="spanishcomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_spanish,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_shopping(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('shopping_uploads/',filename)
class Item(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_shopping,null=True,blank=True)
    price=models.FloatField(null=False,blank=False)
    stock=models.IntegerField(null=False,blank=False)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
def get_file_path_french(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('french_uploads/',filename)
class FrenchCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_french,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class FrenchComment(models.Model):
    product=models.ForeignKey(FrenchCategory,on_delete=models.CASCADE,related_name="frenchcomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_french,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_arabic(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('arabic_uploads/',filename)
class ArabicCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_arabic,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ArabicComment(models.Model):
    product=models.ForeignKey(ArabicCategory,on_delete=models.CASCADE,related_name="arabiccomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_arabic,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_bengali(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('bengali_uploads/',filename)
class BengaliCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_bengali,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class BengaliComment(models.Model):
    product=models.ForeignKey(BengaliCategory,on_delete=models.CASCADE,related_name="bengalicomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_bengali,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)


def get_file_path_russian(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('russian_uploads/', filename)
class RussianCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_russian,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class RussianComment(models.Model):
    product=models.ForeignKey(RussianCategory,on_delete=models.CASCADE,related_name="russiancomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_russian,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_portuguese(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('portuguese_uploads/', filename)
class PortugueseCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_portuguese,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class PortugueseComment(models.Model):
    product=models.ForeignKey(PortugueseCategory,on_delete=models.CASCADE,related_name="portuguesecomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_portuguese,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_urdu(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('urdu_uploads/', filename)
class UrduCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_urdu,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class UrduComment(models.Model):
    product=models.ForeignKey(UrduCategory,on_delete=models.CASCADE,related_name="urducomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_urdu,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_indonesian(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('indonesian_uploads/', filename)
class IndonesianCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_indonesian,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class IndonesianComment(models.Model):
    product=models.ForeignKey(IndonesianCategory,on_delete=models.CASCADE,related_name="indonesiancomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_indonesian,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_german(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('german_uploads/', filename)
class GermanCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_german,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class GermanComment(models.Model):
    product=models.ForeignKey(GermanCategory,on_delete=models.CASCADE,related_name="germancomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_german,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_japanese(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('japanese_uploads/', filename)
class JapaneseCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_japanese,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class JapaneseComment(models.Model):
    product=models.ForeignKey(JapaneseCategory,on_delete=models.CASCADE,related_name="japanesecomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_japanese,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_nigerian(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('nigerian_uploads/', filename)
class NigerianCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_nigerian,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class NigerianComment(models.Model):
    product=models.ForeignKey(NigerianCategory,on_delete=models.CASCADE,related_name="nigeriancomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_nigerian,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_marathi(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('marathi_uploads/', filename)
class MarathiCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_marathi,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class MarathiComment(models.Model):
    product=models.ForeignKey(MarathiCategory,on_delete=models.CASCADE,related_name="marathicomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_marathi,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_telugu(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('telugu_uploads/', filename)
class TeluguCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_telugu,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class TeluguComment(models.Model):
    product=models.ForeignKey(TeluguCategory,on_delete=models.CASCADE,related_name="telugucomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_telugu,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_turkish(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('turkish_uploads/', filename)
class TurkishCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_turkish,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class TurkishComment(models.Model):
    product=models.ForeignKey(TurkishCategory,on_delete=models.CASCADE,related_name="turkishcomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_turkish,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_tamil(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('tamil_uploads/', filename)
class TamilCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_tamil,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class TamilComment(models.Model):
    product=models.ForeignKey(TamilCategory,on_delete=models.CASCADE,related_name="tamilcomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_tamil,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_vietnamese(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('vietnamese_uploads/', filename)
class VietnameseCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_vietnamese,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class VietnameseComment(models.Model):
    product=models.ForeignKey(VietnameseCategory,on_delete=models.CASCADE,related_name="vietnamesecomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_vietnamese,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_tagalog(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('tagalog_uploads/', filename)
class TagalogCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_tagalog,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class TagalogComment(models.Model):
    product=models.ForeignKey(TagalogCategory,on_delete=models.CASCADE,related_name="tagalogcomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_tagalog,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_korean(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('tagalog_uploads/', filename)
class KoreanCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_korean,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class KoreanComment(models.Model):
    product=models.ForeignKey(KoreanCategory,on_delete=models.CASCADE,related_name="koreancomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_korean,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_iranian(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('iranian_uploads/', filename)
class IranianCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_iranian,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class IranianComment(models.Model):
    product=models.ForeignKey(IranianCategory,on_delete=models.CASCADE,related_name="iraniancomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_iranian,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_hausa(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('hausa_uploads/', filename)
class HausaCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_hausa,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class HausaComment(models.Model):
    product=models.ForeignKey(HausaCategory,on_delete=models.CASCADE,related_name="hausacomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_hausa,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_swahili(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('swahili_uploads/', filename)
class SwahiliCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_swahili,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class SwahiliComment(models.Model):
    product=models.ForeignKey(SwahiliCategory,on_delete=models.CASCADE,related_name="swahilicomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_swahili,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_javanese(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('javanese_uploads/', filename)
class JavaneseCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_javanese,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class JavaneseComment(models.Model):
    product=models.ForeignKey(JavaneseCategory,on_delete=models.CASCADE,related_name="javanesecomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_javanese,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_italian(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('italian_uploads/', filename)
class ItalianCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_italian,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ItalianComment(models.Model):
    product=models.ForeignKey(ItalianCategory,on_delete=models.CASCADE,related_name="italiancomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_italian,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)

def get_file_path_punjabi(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (nowTime, original_filename)
    return os.path.join('punjabi_uploads/', filename)
class PunjabiCategory(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path_punjabi,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class PunjabiComment(models.Model):
    product=models.ForeignKey(PunjabiCategory,on_delete=models.CASCADE,related_name="punjabicomment")
    commenter_name=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_body=models.TextField()
    comment_image=models.ImageField(upload_to=get_file_path_punjabi,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.product.name,self.commenter_name.username)