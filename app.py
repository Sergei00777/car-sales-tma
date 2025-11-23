from flask import Flask, render_template

app = Flask(__name__)

# Данные автомобилей
cars_data = {
    'geely-coolray': {
        'brand': 'Geely Coolray',
        'year': '2024',
        'engine': '1.5L Turbo',
        'transmission': 'Автомат',
        'drive': 'Полный привод',
        'mileage': '0 км',
        'color': 'Белый',
        'price': '1 890 000',
        'status': 'В наличии',
        'status_class': 'in-stock',
        'features': [
            'Панорамная крыша',
            'Кожаный салон',
            'Apple CarPlay',
            'Камера 360°',
            'Бесключевой доступ',
            'Подогрев сидений'
        ],
        'images': ['images/geely-coolray.jpg']
    },
    'haval-jolion': {
        'brand': 'Haval Jolion',
        'year': '2023',
        'engine': '1.5L Turbo',
        'transmission': 'Вариатор',
        'drive': 'Передний привод',
        'mileage': '0 км',
        'color': 'Серый',
        'price': '2 100 000',
        'status': 'В наличии',
        'status_class': 'in-stock',
        'features': [
            'Мультимедиа система',
            'Камера 360°',
            'Климат-контроль',
            'Светодиодные фары',
            'Датчики парковки',
            'Круиз-контроль'
        ],
        'images': ['images/haval-jolion.jpg']
    },
    'toyota-camry': {
        'brand': 'Toyota Camry',
        'year': '2024',
        'engine': '2.5L Hybrid',
        'transmission': 'Автомат',
        'drive': 'Передний привод',
        'mileage': '0 км',
        'color': 'Черный',
        'price': '3 500 000',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'features': [
            'Премиум аудио система',
            'Кожаный салон',
            'Паркинг-ассистент',
            'Панорамная крыша',
            'Вентиляция сидений',
            'Цифровая приборная панель'
        ],
        'images': ['images/toyota-camry.jpg']
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/car/<car_id>')
def car_detail(car_id):
    car = cars_data.get(car_id)
    if car:
        return render_template('car_detail.html', car=car)
    else:
        return "Автомобиль не найден", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)