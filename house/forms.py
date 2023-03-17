from django import forms
from .models import *


class BaseForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Type_choise, label='Выберите тип дома')
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Введите заголовок')
    bio = forms.CharField(widget=forms.Textarea(), label='Опишите ваш дом')
    preview = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input'}),label='Главное фото')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Введите адрес')
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered'}), label='Цена')
    size = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered'}), label='Размер')
    material = forms.ChoiceField(choices=Material_choise, label='Материал')
    rooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered', 'maxlength': '3',
                                                               'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength)'}),
                               label='Количество комнат')
    furniture = forms.ChoiceField(choices=Furniture, label='Мебилизаация')
    repair = forms.ChoiceField(choices=Repair, label='Тип ремонта')
    near = forms.CharField(widget=forms.Textarea(), label='Что есть рядом')
    date_of_building = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input has-text-centered', 'maxlength': '4',
                                        'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength)'}), label='Дата постройки')

    class Meta:
        model = House
        fields = [
            'type', 'title', 'bio', 'preview', 'address',
            'price',
            'size', 'material', 'rooms', 'furniture', 'repair',
            'near', 'date_of_building', ]


class ApartamentForm(forms.ModelForm):
    floor = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input'}), label='Этаж')
    storeys = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input'}), label='Этажность дома')
    building_type = forms.ChoiceField(choices=Building_type, label='Тип строения')

    class Meta:
        model = House
        fields = ['floor', 'storeys', 'building_type']


class HouseForm(forms.ModelForm):
    living_space = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input'}), label='Жилая площадь')
    location = forms.ChoiceField(choices=Location, label='Локация')
    convenience = forms.CharField(widget=forms.Textarea(), label='Удобства')

    class Meta:
        model = House
        fields = ['living_space', 'location', 'convenience']


class CustomFileField(forms.FileInput):
    template_name = 'file.html'


class ImageForm(forms.ModelForm):
    image1 = forms.ImageField()
    image2 = forms.ImageField()
    image3 = forms.ImageField()
    image4 = forms.ImageField()
    image5 = forms.ImageField()
    image6 = forms.ImageField()
    image7 = forms.ImageField()
    image8 = forms.ImageField()
    image9 = forms.ImageField()
    image10 = forms.ImageField()
    image11 = forms.ImageField()
    image12 = forms.ImageField()
    image13 = forms.ImageField()
    image14 = forms.ImageField()
    image15 = forms.ImageField()
    image16 = forms.ImageField()

    class Meta:
        model = Image
        fields = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6',
                  'image7', 'image8', 'image9', 'image10', 'image11', 'image12', 'image13', 'image14', 'image15',
                  'image16', ]
