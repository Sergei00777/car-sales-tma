from flask import Flask, render_template
from cars_data import cars_data, cars_in_stock, cars_on_order, cities_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                         in_stock_cars=cars_in_stock,
                         on_order_cars=cars_on_order,
                         cars=cars_data,
                         cities=cities_data)

@app.route('/car/<car_id>')
def car_detail(car_id):
    car = cars_data.get(car_id)
    if car:
        template_name = f'cars/{car_id.replace("-", "_")}.html'
        return render_template(template_name, car=car, car_id=car_id, cities=cities_data)  # Добавляем cities
    else:
        return "Автомобиль не найден", 404

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', cities=cities_data)

@app.route('/faq')
def faq():
    return render_template('faq.html', cities=cities_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)