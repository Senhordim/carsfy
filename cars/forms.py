from django import forms
from .models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data['photo']
        )
        car.save()
        return car

class CarModelForm (forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year == None:
            raise forms.ValidationError('Ano do modelo é obrigatório')
        if model_year < 1900:
            raise forms.ValidationError('Ano do modelo inválido')
        return model_year

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year == None:
            raise forms.ValidationError('Ano de fabricação é obrigatório')
        if factory_year < 1900:
            raise forms.ValidationError('Ano de fabricação inválido')
        return factory_year

    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if Car.objects.filter(plate=plate).exists():
            raise forms.ValidationError('Plate already exists')
        return plate

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000.0:
            raise forms.ValidationError('Valor mínimo deve ser de R$10.000,00')
        return value
