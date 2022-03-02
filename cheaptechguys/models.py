from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
# Create your models here.


class contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=300)


def get_profile_image_filepath(self, filepath):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "ii.png"

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(email=self.normalize_email(email),
                          username=username,)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(verbose_name='email', max_length=200, unique=True)
    username=models.CharField(max_length=200, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perm(self, app_label):
        return True





class Product(models.Model):
    Title = models.CharField(max_length=100)
    Image1 = models.FileField(null=True)
    Image2 = models.FileField(null=True)
    Image3 = models.FileField(null=True)
    Image4 = models.FileField(null=True)
    Image5 = models.FileField(null=True)
    Before_price = models.CharField(max_length=200)
    After_price = models.CharField(max_length=200)
    c = (
        ('Top','Top'),
        ('None', 'None')
    )
    type = models.CharField(choices=c, max_length=50, null=True)
    discount = models.CharField(max_length=200)
    Choices = (
        ('Smart Phone', 'Smart Phone'),
        ('Camera', 'Camera'),
        ('Games', 'Games'),
        ('Smart Speakers', 'Smart Speakers'),
        ('Smart Watch', 'Smart Watch'),
        ('Tablets', 'Tablets'),
        ('Laptops', 'Laptops'),
        ('Mouse', 'Mouse'),
        ('keyboard', 'Keyboard'),
        ('Headphone', 'Headphone'),
        ('Monitors', 'Monitors'),
        ('TV', 'TV')
    )
    choice = models.CharField(max_length=100, choices=Choices, default=None)
    Description1title = models.CharField(max_length=100)
    Description2title = models.CharField(max_length=100)
    Description3title = models.CharField(max_length=100)
    Description4title = models.CharField(max_length=100)
    Description1 = models.TextField()
    Description2 = models.TextField()
    Description3 = models.TextField()
    Description4 = models.TextField()
    Buy_link = models.URLField()
    Dateofpublished = models.DateTimeField(auto_now_add=True)
    Brand = models.CharField(max_length=100)
    Memory = models.CharField(max_length=200, blank=True, default=None)
    cchoice = (
        ('Red', 'Red'),
        ('White', 'White'),
        ('Blue', 'Blue'),
        ('Brown', 'Brown'),
        ('Pink', 'Pink'),
        ('Green', 'Green'),
        ('Sky Blue', 'Sky Blue'),
        ('Yellow', 'Yellow'),
        ('Black', 'Black')
    )
    Colour = models.CharField(max_length=50, choices=cchoice, default=None)
    Memory = models.CharField(max_length=200, blank=True, default=None)
    cellular_technology = models.CharField(max_length=200, blank=True, default=None)
    Included_items = models.CharField(max_length=200, blank=True, default=None)
    Model = models.CharField(max_length=200, blank=True, default=None)
    Camera_quality = models.CharField(max_length=200, blank=True, default=None)
    Model = models.CharField(max_length=200, blank=True, default=None)
    screensize = models.CharField(max_length=200, blank=True, default=None)
    RAM = models.CharField(max_length=200, blank=True, default=None)
    ROM = models.CharField(max_length=200, blank=True, default=None)
    Resolution = models.CharField(max_length=200, blank=True, default=None)
    Zoom = models.CharField(max_length=200, blank=True, default=None)
    displaytype = models.CharField(max_length=200, blank=True, default=None)
    Genre = models.CharField(max_length=200, blank=True, default=None)
    Mode = models.CharField(max_length=200, blank=True, default=None)
    releasedate = models.DateTimeField(auto_now_add=True)
    Bluetoothconnectivity = models.CharField(max_length=200, blank=True, default=None)
    waterresistance = models.CharField(max_length=200, blank=True, default=None)
    connectivitytype = models.CharField(max_length=200, blank=True, default=None)
    storage = models.CharField(max_length=200, blank=True, default=None)
    Zoom = models.CharField(max_length=200, blank=True, default=None)
    Graphicscoprocessor = models.CharField(max_length=200, blank=True, default=None)
    Batterylife = models.CharField(max_length=200, blank=True, default=None)
    compatibledevices = models.CharField(max_length=200, blank=True, default=None)
    Refreshrate = models.CharField(max_length=200, blank=True, default=None)
    Supportedinternetservices = models.CharField(max_length=200, blank=True, default=None)
    Specialfeatures = models.CharField(max_length=200, blank=True, default=None)
    series = models.CharField(max_length=200, blank=True, default=None)
    ratings = models.FloatField(null=True, default=None)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, default='Del')
    likes = models.ManyToManyField(Account, related_name='likes', null=True, default='Del')

    def get_absolute_url(self):
        return reverse('product', kwargs={'name':self.Title})
    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Product'
        get_latest_by = ['-Dateofpublished']

class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist')














