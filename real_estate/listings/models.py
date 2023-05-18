from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    skype = models.CharField(max_length=30)
    telegtam = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30)
    viber = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Listing(models.Model):
    HOUSE = 'Дом'
    COTTAGE = 'Коттедж'
    APARTMENT = 'Квартира'
    ROOM = 'Комната'

    TYPE_OF_HOUSING = [
        (HOUSE, 'Дом'),
        (COTTAGE, 'Коттедж'),
        (APARTMENT, 'Квартира'),
        (ROOM, 'Комната'),
    ]

    SALE = 'Продажа'
    RENT = 'Аренда'

    AD_TYPE = [
        (SALE, 'Продажа'),
        (RENT, 'Аренда'),
    ]
    #author = 
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField()    
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    type_of_housing = models.CharField(
        max_length=10,
        choices=TYPE_OF_HOUSING,
        default=APARTMENT
    )
    ad_status = models.CharField(
        max_length=10,
        choices=AD_TYPE,
        default=SALE
    )
    square = models.DecimalField(max_digits=5, decimal_places=2)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    garage = models.IntegerField()
    video = models.FileField(upload_to='video/%y', blank=True, null=True)
    floor_plan = models.ImageField(blank=True, null=True)
    #location = map will be here =)
    agent = models.ForeignKey(
        Agent, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='listing'
    )
    
    def __str__(self):
        return self.title
    
    

    def __str__(self):
        return self.title
