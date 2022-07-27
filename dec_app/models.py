from django.db import models

# Create your models here.

# create category table into database.
class Category_table(models.Model):
    cname = models.CharField(max_length=200, primary_key=True)
    # slug is a unique for category.
    slug = models.SlugField(max_length=200, unique=True, default='')
    cat_img = models.ImageField(upload_to="category_list", default="default.png")
    category_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cname
