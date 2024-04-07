from django.db import models

# Create your models here.
class contact(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=200,null=True)
    Mobile=models.CharField(max_length=20,null=True)
    Message=models.TextField(null=True)
    def __str__(self):
        return self.Name
    
class category(models.Model):
    cname=models.CharField(max_length=200,null=True)
    cpic=models.ImageField(upload_to='static/categorypic/',null=True)
    cdate=models.DateField()
    def __str__(self):
        return self.cname

class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider/',null=True)
    sdate=models.DateField()
    
class subcategory(models.Model):
    category_name=models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.subcategory_name

class products(models.Model):
    product_category=models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory_name=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    price=models.IntegerField()
    discount_price=models.IntegerField()
    product_pic=models.ImageField(upload_to='static/product/',null=True)
    total_discount=models.IntegerField()
    product_quantity=models.CharField(max_length=200,null=True)
    pdate=models.DateField()
    
class register(models.Model):
    name=models.CharField(max_length=150,null=True)
    email=models.CharField(max_length=100,primary_key=True)
    mobile=models.CharField(max_length=20,null=True)
    passwd=models.CharField(max_length=100,null=True)
    profile=models.ImageField(upload_to='static/userpic/',null=True)
    address=models.TextField(null=True)

class cart(models.Model):
    userid=models.CharField(max_length=200,null=True)
    product_name=models.CharField(max_length=200,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    total_price=models.FloatField(null=True)
    product_picture=models.CharField(max_length=300,null=True)
    pw=models.CharField(max_length=200,null=True)
    added_date=models.DateField(null=True)


class myorder(models.Model):
    userid=models.CharField(max_length=200,null=True)
    product_name=models.CharField(max_length=200,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    total_price=models.FloatField(null=True)
    product_picture=models.CharField(max_length=300,null=True)
    pw=models.CharField(max_length=200,null=True)
    orderd_date=models.DateField(null=True)
    status=models.CharField(max_length=200,null=True)

