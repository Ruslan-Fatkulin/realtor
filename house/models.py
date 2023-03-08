from django.contrib.auth.models import User
from django.db.models import *

Material_choise = [
    ('дерево', 'дерево'),
    ('кирпич', 'кирпич'),
    ('керамические блоки', 'керамические блоки'),
    ('газобетон', 'газобетон'),
]

Type_choise = [
    ('дом', 'дом'),
    ('квартира', 'квартира'),
    ('земельный участок', 'земельный участок'),

]

Furniture = [
    ('С мебелью', 'С мебелью'),
    ('Без мебели', 'Без мебели'),
    ('Частично', 'Частично'),
    ('Только кухня', 'Только кухня'),
    ('Только санузел', 'Только санузел'),
]

Repair = [
    ('Евро ремонт', 'Евро ремонт'),
    ('Черновая отделка', 'Черновая отделка'),
    ('Без ремонта', 'Без ремонта'),
    ('Частичная отделка', 'Частичная отделка'),
]

Building_type = [
    ('Новостройка', 'Новостройка'),
    ('Панельный дом', 'Панельный дом'),
    ('Кирпичный дом', 'Кирпичный дом'),
]

Location = [
    ('В городе', 'В городе'),
    ('Пригород', 'Пригород'),
    ('За городом', 'За городом'),
]


class House(Model):
    type = CharField(max_length=25, choices=Type_choise)
    title = CharField(max_length=255)
    bio = TextField()
    address = CharField(max_length=255)
    preview = ImageField(null=True, blank=True)
    price = IntegerField()
    size = IntegerField()
    material = CharField(max_length=255, choices=Material_choise)
    rooms = IntegerField()
    furniture = CharField(max_length=20, choices=Furniture)
    repair = CharField(max_length=20, choices=Repair)
    near = TextField(null=True, blank=True)
    date_of_building = IntegerField(max_length=4, null=True, blank=True)
    seller = ForeignKey(User, on_delete=CASCADE, null=True)
    #################
    floor = IntegerField(null=True, blank=True)
    storeys = IntegerField(null=True, blank=True)
    building_type = CharField(max_length=20, choices=Building_type)
    #################
    living_space = IntegerField(null=True)
    location = CharField(max_length=20, choices=Location)
    convenience = TextField(null=True)
    date_added = DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title


class Image(Model):
    house = ForeignKey(House, on_delete=CASCADE)
    image = ImageField(blank=True, null=True)

    def __str__(self):
        return self.house.title


class Image(Model):
    house = ForeignKey(House, on_delete=CASCADE, related_name='house')
    image1 = ImageField(blank=True)
    image2 = ImageField(blank=True)
    image3 = ImageField(blank=True)
    image4 = ImageField(blank=True)
    image5 = ImageField(blank=True)
    image6 = ImageField(blank=True)
    image7 = ImageField(null=True)
    image8 = ImageField(null=True)
    image9 = ImageField(null=True)
    image10 = ImageField(null=True)
    image11 = ImageField(null=True)
    image12 = ImageField(null=True)
    image13 = ImageField(null=True)
    image14 = ImageField(null=True)
    image15 = ImageField(null=True)
    image16 = ImageField(null=True)

    def __str__(self):
        return str(self.house)
