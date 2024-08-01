from django.shortcuts import render

def index(request):
  return render(request, 'index.html', context={
    'cars': [
      {
        'model': 'Toyota Camry',
        'year': 2022,
        'price': 25000,
        'image': 'https://www.toyota.com/imgix/responsive/images/mlp/colorizer/2022/camry/1H1/1.png?bg=fff&fm=webp&w=930',
      },
      {
        'model': 'Honda Accord',
        'year': 2022,
        'price': 24000,
        'image': 'https://www.honda.com/imgix/responsive/images/mlp/colorizer/2022/accord/1H1/1.png?bg=fff&fm=webp&w=930',
      },
      {
        'model': 'Nissan Altima',
        'year': 2022,
        'price': 23000,
        'image': 'https://www.nissanusa.com/imgix/responsive/images/mlp/colorizer/2022/altima/1H1/1.png?bg=fff&fm=webp&w=930',
      },
    ]
  })
