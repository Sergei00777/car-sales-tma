# cars_on_order.py - Полный список всех автомобилей
cars_on_order = {
    # Ваши существующие авто
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
        'images': ['images/toyota-camry.jpg'],
        'description': 'Легендарный седан бизнес-класса с гибридной силовой установкой.'
    },

    # Основной список автомобилей
    'changan-cs35-plus': {
        'brand': 'Changan CS35 PLUS',
        'year': '2021',
        'engine': '1.4T (140 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '50 000 км',
        'color': 'Белый',
        'price': '1 115 000',
        'price_cny': '52 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '30-45 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/changan-cs35-plus.jpg'],
        'features': [
            'Панорамная крыша',
            'Камера 360°',
            'Apple CarPlay',
            'Круиз-контроль',
            'Кожаный салон'
        ],
        'description': 'Changan CS35 PLUS 2021 года в отличном состоянии. Полностью обслужен, готов к эксплуатации.'
    },

    'mazda-cx-30-2023': {
        'brand': 'Mazda CX-30',
        'year': '2023',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '22 000 км',
        'color': 'Серый металлик',
        'price': '2 120 000',
        'price_cny': '104 900 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '35-50 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-cx-30.jpg'],
        'features': [
            'Матричные фары',
            'Кожаный салон',
            'Подогрев сидений',
            'Беспроводной CarPlay',
            'Давление в шинах'
        ],
        'description': 'Mazda CX-30 2023 года с минимальным пробегом. Все оригинальные документы в наличии.'
    },

    'mazda-3-angkesela-2021': {
        'brand': 'Mazda 3 Angkesela',
        'year': '2021',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '17 000 км',
        'color': 'Красный',
        'price': '1 672 000',
        'price_cny': '77 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-3.jpg'],
        'features': [
            'Кожаный руль',
            'Климат-контроль',
            'Камера заднего вида',
            'Датчики дождя',
            'Легкосплавные диски'
        ],
        'description': 'Mazda 3 2021 года. Экономичный расход, отличная управляемость.'
    },

    'chevrolet-cruze': {
        'brand': 'Chevrolet Cruze',
        'year': '2022',
        'engine': '1.3T (165 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '45 000 км',
        'color': 'Синий',
        'price': '1 021 000',
        'price_cny': '45 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '25-40 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/chevrolet-cruze.jpg'],
        'features': [
            'Мультимедийная система',
            'Кондиционер',
            'Парктроники',
            'Электростеклоподъемники',
            'Круиз-контроль'
        ],
        'description': 'Chevrolet Cruze 2022 года. Надежный и экономичный седан.'
    },

    'mazda-cx-30-2021': {
        'brand': 'Mazda CX-30',
        'year': '2021',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '28 600 км',
        'color': 'Белый',
        'price': '1 896 000',
        'price_cny': '97 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '30-45 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-cx-30-2.jpg'],
        'features': [
            'Светодиодные фары',
            'Климат-контроль',
            'Мультимедийная система',
            'Круиз-контроль',
            'Датчики парковки'
        ],
        'description': 'Mazda CX-30 2021 года. Отличное состояние, полная комплектация.'
    },

    'mazda-cx-4': {
        'brand': 'Mazda CX-4',
        'year': '2022',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '69 000 км',
        'color': 'Серый',
        'price': '1 694 000',
        'price_cny': '79 700 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '35-50 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-cx-4.jpg'],
        'features': [
            'Кожаный салон',
            'Подогрев сидений',
            'Камера 360°',
            'Панорамная крыша',
            'Бесключевой доступ'
        ],
        'description': 'Mazda CX-4 2022 года. Стильный кроссовер с отличной управляемостью.'
    },

    'haval-h6': {
        'brand': 'Haval H6',
        'year': '2022',
        'engine': '1.5T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '13 000 км',
        'color': 'Черный',
        'price': '1 423 000',
        'price_cny': '79 000 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/haval-h6.jpg'],
        'features': [
            'Панорамная крыша',
            'Цифровая приборная',
            'Подогрев всех сидений',
            'Адаптивный круиз',
            'Система распознавания знаков'
        ],
        'description': 'Haval H6 2022 года. Современный кроссовер с богатой комплектацией.'
    },

    'bmw-x2': {
        'brand': 'BMW X2',
        'year': '2022',
        'engine': '1.5T (140 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '60 900 км',
        'color': 'Синий',
        'price': '1 547 000',
        'price_cny': '90 100 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/bmw-x2.jpg'],
        'features': [
            'Кожаный салон',
            'Спортивные сиденья',
            'Навигационная система',
            'Светодиодные фары',
            'Парктроник'
        ],
        'description': 'BMW X2 2022 года. Компактный премиум кроссовер с характером.'
    },

    'audi-a4': {
        'brand': 'Audi A4',
        'year': '2021',
        'engine': '2.0T (190 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '88 000 км',
        'color': 'Черный',
        'price': '2 117 000',
        'price_cny': '117 000 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '50-65 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/audi-a4.jpg'],
        'features': [
            'Полный привод quattro',
            'Виртуальная приборная',
            'Кожаный салон',
            'Аудиосистема Bang & Olufsen',
            'Матричные фары'
        ],
        'description': 'Audi A4 2021 года. Премиальный седан с полным приводом.'
    },

    'mazda-cx-4-2023': {
        'brand': 'Mazda CX-4',
        'year': '2023',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '47 000 км',
        'color': 'Красный',
        'price': '1 941 000',
        'price_cny': '88 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '35-50 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-cx-4-2.jpg'],
        'features': [
            'Обновленная мультимедия',
            'Беспроводной CarPlay',
            'Кожаный руль',
            'Климат-контроль',
            'Давление в шинах'
        ],
        'description': 'Mazda CX-4 2023 года. Свежая модель с минимальным пробегом.'
    },

    'nissan-x-trail': {
        'brand': 'Nissan X-Trail (Qijun)',
        'year': '2022',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Вариатор',
        'drive': 'Передний',
        'mileage': '57 000 км',
        'color': 'Белый',
        'price': '1 661 000',
        'price_cny': '76 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/nissan-x-trail.jpg'],
        'features': [
            'Панорамная крыша',
            'Кожаный салон',
            'Камера 360°',
            'Интеллектуальный ключ',
            'Система экстренного торможения'
        ],
        'description': 'Nissan X-Trail 2022 года. Надежный семейный кроссовер.'
    },

    'honda-civic': {
        'brand': 'Honda Civic',
        'year': '2022',
        'engine': '1.5T (182 л.с.)',
        'transmission': 'Вариатор',
        'drive': 'Передний',
        'mileage': '45 000 км',
        'color': 'Белый',
        'price': '1 510 000',
        'price_cny': '86 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/honda-civic.jpg'],
        'features': [
            'Спортивный дизайн',
            'Цифровая приборная',
            'Android Auto',
            'Подогрев руля',
            'LED фары'
        ],
        'description': 'Honda Civic 2022 года в спортивном исполнении. Мощный турбо-двигатель.'
    },

    'mercedes-a-class': {
        'brand': 'Mercedes-Benz A-Class',
        'year': '2022',
        'engine': '1.3T (163 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '76 000 км',
        'color': 'Серый',
        'price': '1 504 000',
        'price_cny': '89 000 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '50-70 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mercedes-a-class.jpg'],
        'features': [
            'MBUX мультимедиа',
            'Цифровая приборная',
            'Кожаный салон',
            'Панорамная крыша',
            'Адаптивный круиз'
        ],
        'description': 'Mercedes-Benz A-Class 2022 года. Премиальный компактный седан.'
    },

    'mercedes-gla': {
        'brand': 'Mercedes-Benz GLA',
        'year': '2022',
        'engine': '1.3T (163 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '89 000 км',
        'color': 'Белый',
        'price': '1 669 000',
        'price_cny': '103 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '55-75 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mercedes-gla.jpg'],
        'features': [
            'Полный привод 4MATIC',
            'Панорамная крыша',
            'Подогрев сидений',
            'Беспроводная зарядка',
            'Система помощи при парковке'
        ],
        'description': 'Mercedes-Benz GLA 2022 года. Компактный премиум кроссовер.'
    },

    'volkswagen-passat': {
        'brand': 'Volkswagen Passat',
        'year': '2022',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '90 000 км',
        'color': 'Серый',
        'price': '1 450 000',
        'price_cny': '82 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/volkswagen-passat.jpg'],
        'features': [
            'Климат-контроль',
            'Кожаный салон',
            'Электрорегулировка сидений',
            'Камера заднего вида',
            'Круиз-контроль'
        ],
        'description': 'Volkswagen Passat 2022 года. Классический бизнес-седан.'
    },

    'volkswagen-tiguan-l': {
        'brand': 'Volkswagen Tiguan L',
        'year': '2022',
        'engine': '1.5T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '109 000 км',
        'color': 'Синий',
        'price': '1 644 000',
        'price_cny': '98 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/volkswagen-tiguan.jpg'],
        'features': [
            'Панорамная крыша',
            'Цифровая приборная',
            'Трехзонный климат',
            'Подогрев сидений',
            'Система помощи при движении'
        ],
        'description': 'Volkswagen Tiguan L 2022 года. Удлиненная версия популярного кроссовера.'
    },

    'hyundai-elantra': {
        'brand': 'Hyundai Elantra',
        'year': '2021',
        'engine': '1.5L (115 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '80 000 км',
        'color': 'Серый',
        'price': '1 209 000',
        'price_cny': '59 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '30-45 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/hyundai-elantra.jpg'],
        'features': [
            'Мультимедийная система',
            'Кондиционер',
            'Парктроники',
            'Электростеклоподъемники',
            'Легкосплавные диски'
        ],
        'description': 'Hyundai Elantra 2021 года. Надежный и экономичный седан.'
    },

    'skoda-karoq': {
        'brand': 'Skoda Karoq',
        'year': '2021',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '58 000 км',
        'color': 'Белый',
        'price': '1 904 000',
        'price_cny': '122 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '50-65 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/skoda-karoq.jpg'],
        'features': [
            'Панорамная крыша',
            'Кожаный салон',
            'Подогрев сидений',
            'Камера заднего вида',
            'Круиз-контроль'
        ],
        'description': 'Skoda Karoq 2021 года. Практичный европейский кроссовер.'
    },

    'mazda-cx-5': {
        'brand': 'Mazda CX-5',
        'year': '2022',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '64 000 км',
        'color': 'Серый',
        'price': '2 765 000',
        'price_cny': '175 000 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-cx-5.jpg'],
        'features': [
            'Кожаный салон',
            'Подогрев сидений',
            'Камера 360°',
            'Панорамная крыша',
            'Беспроводной CarPlay'
        ],
        'description': 'Mazda CX-5 2022 года. Популярный кроссовер среднего класса.'
    },

    'mazda-3-angkesela-2023': {
        'brand': 'Mazda 3 Angkesela',
        'year': '2023',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '17 200 км',
        'color': 'Серый',
        'price': '1 952 000',
        'price_cny': '89 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '35-50 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-3-2.jpg'],
        'features': [
            'Обновленная мультимедия',
            'Беспроводной CarPlay',
            'Кожаный руль',
            'Климат-контроль',
            'Давление в шинах'
        ],
        'description': 'Mazda 3 2023 года. Свежая модель с минимальным пробегом.'
    },

    'haval-cool-dog': {
        'brand': 'Haval Cool Dog',
        'year': '2022',
        'engine': '1.5T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '43 000 км',
        'color': 'Зеленый',
        'price': '2 997 000',
        'price_cny': '86 700 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/haval-cool-dog.jpg'],
        'features': [
            'Необычный дизайн',
            'Панорамная крыша',
            'Цифровая приборная',
            'Подогрев сидений',
            'Камера 360°'
        ],
        'description': 'Haval Cool Dog 2022 года. Молодежный кроссовер с ярким дизайном.'
    },

    'volkswagen-sagitar': {
        'brand': 'Volkswagen Sagitar',
        'year': '2022',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '20 000 км',
        'color': 'Белый',
        'price': '1 417 000',
        'price_cny': '79 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '35-50 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/volkswagen-sagitar.jpg'],
        'features': [
            'Кожаный салон',
            'Климат-контроль',
            'Камера заднего вида',
            'Круиз-контроль',
            'Легкосплавные диски'
        ],
        'description': 'Volkswagen Sagitar 2022 года. Качественный седан для города.'
    },

    'volkswagen-golf': {
        'brand': 'Volkswagen Golf',
        'year': '2022',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '33 600 км',
        'color': 'Синий',
        'price': '1 937 000',
        'price_cny': '125 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/volkswagen-golf.jpg'],
        'features': [
            'Цифровая приборная',
            'Кожаный салон',
            'Подогрев сидений',
            'Адаптивный круиз',
            'Матричные фары'
        ],
        'description': 'Volkswagen Golf 2022 года. Легендарный хэтчбек в новой генерации.'
    },

    'toyota-corolla': {
        'brand': 'Toyota Corolla',
        'year': '2022',
        'engine': '1.5L (121 л.с.)',
        'transmission': 'Вариатор',
        'drive': 'Передний',
        'mileage': '51 000 км',
        'color': 'Белый',
        'price': '1 195 000',
        'price_cny': '58 500 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/toyota-corolla.jpg'],
        'features': [
            'Гибридная система',
            'Экономичный расход',
            'Камера заднего вида',
            'Климат-контроль',
            'Легкосплавные диски'
        ],
        'description': 'Toyota Corolla 2022 года. Самый продаваемый автомобиль в мире.'
    },

    'nissan-qashqai': {
        'brand': 'Nissan Qashqai',
        'year': '2022',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Вариатор',
        'drive': 'Передний',
        'mileage': '37 000 км',
        'color': 'Красный',
        'price': '1 786 000',
        'price_cny': '88 000 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/nissan-qashqai.jpg'],
        'features': [
            'Панорамная крыша',
            'Кожаный салон',
            'Камера 360°',
            'Интеллектуальный ключ',
            'Система экстренного торможения'
        ],
        'description': 'Nissan Qashqai 2022 года. Компактный кроссовер для города.'
    },

    'audi-q3': {
        'brand': 'Audi Q3',
        'year': '2021',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '59 000 км',
        'color': 'Белый',
        'price': '1 870 000',
        'price_cny': '119 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '50-65 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/audi-q3.jpg'],
        'features': [
            'Кожаный салон',
            'Панорамная крыша',
            'Цифровая приборная',
            'Матричные фары',
            'Аудиосистема Bang & Olufsen'
        ],
        'description': 'Audi Q3 2021 года. Компактный премиум кроссовер.'
    },

    'audi-q2l': {
        'brand': 'Audi Q2L',
        'year': '2022',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '50 000 км',
        'color': 'Серый',
        'price': '1 528 000',
        'price_cny': '89 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/audi-q2l.jpg'],
        'features': [
            'Светодиодная оптика',
            'Кожаный салон',
            'Мультимедиа MMI',
            'Датчики парковки',
            'Легкосплавные диски'
        ],
        'description': 'Audi Q2L 2022 года. Субкомпактный кроссовер премиум-класса.'
    },

    'audi-a3-hatchback': {
        'brand': 'Audi A3',
        'year': '2021',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '75 000 км',
        'color': 'Синий',
        'price': '1 739 000',
        'price_cny': '108 000 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/audi-a3-hatchback.jpg'],
        'features': [
            'Спортивный дизайн',
            'Цифровая приборная',
            'Кожаный салон',
            'Светодиодные фары',
            'Мультимедиа MMI'
        ],
        'description': 'Audi A3 Sportback 2021 года. Динамичный премиальный хэтчбек.'
    },

    'audi-a3-sedan': {
        'brand': 'Audi A3',
        'year': '2022',
        'engine': '1.4T (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '55 000 км',
        'color': 'Белый',
        'price': '1 607 000',
        'price_cny': '96 900 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/audi-a3-sedan.jpg'],
        'features': [
            'Современный дизайн',
            'Цифровая приборная',
            'Кожаный салон',
            'Светодиодная оптика',
            'Система помощи при парковке'
        ],
        'description': 'Audi A3 Sedan 2022 года. Элегантный премиальный седан.'
    },

    'bmw-x1': {
        'brand': 'BMW X1',
        'year': '2021',
        'engine': '1.5T (140 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '65 000 км',
        'color': 'Белый',
        'price': '1 645 000',
        'price_cny': '98 900 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '45-60 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/bmw-x1.jpg'],
        'features': [
            'Кожаный салон',
            'Навигационная система',
            'Светодиодные фары',
            'Парктроник',
            'Электрорегулировка сидений'
        ],
        'description': 'BMW X1 2021 года. Компактный кроссовер от немецкого бренда.'
    },

    'bmw-3-series': {
        'brand': 'BMW 3 Series',
        'year': '2021',
        'engine': '2.0T (184 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Задний',
        'mileage': '60 000 км',
        'color': 'Черный',
        'price': '2 249 000',
        'price_cny': '128 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '50-65 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/bmw-3-series.jpg'],
        'features': [
            'Пакет M Sport',
            'Кожа Vernasca',
            'Хэд-ап дисплей',
            'Адаптивный круиз',
            'Паркинг-ассистент'
        ],
        'description': 'BMW 320i 2021 года в комплектации M Sport. Задний привод, динамичное управление.'
    },

 'mazda-3-angkesela-2022': {
        'brand': 'Mazda 3 Angkesela',
        'year': '2022',
        'engine': '2.0L (150 л.с.)',
        'transmission': 'Автомат',
        'drive': 'Передний',
        'mileage': '63 800 км',
        'color': 'Серый',
        'price': '1 695 000',
        'price_cny': '79 800 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '35-50 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['cars/mazda-3-3.jpg'],
        'features': [
            'Кожаный салон',
            'Климат-контроль',
            'Камера заднего вида',
            'Круиз-контроль',
            'Легкосплавные диски'
        ],
        'description': 'Mazda 3 2022 года. Надежный японский седан.'
    },

    'honda-vezel': {
        'brand': 'Honda Vezel (Binzhi)',
        'year': '2022',
        'engine': '1.5L (131 л.с.)',
        'transmission': 'Вариатор',
        'drive': 'Передний',
        'mileage': '47 000 км',
        'color': 'Серый',
        'price': '1 345 000',
        'price_cny': '72 000 ¥',
        'status': 'Под заказ',
        'status_class': 'on-order',
        'delivery_time': '40-55 дней',
        'delivery': 'доставка до Иркутска',
        'images': ['images/honda-vezel.jpg'],
        'features': [
            'Гибридная установка',
            'Экономичный расход',
            'Камера заднего вида',
            'Климат-контроль',
            'Легкосплавные диски'
        ],
        'description': 'Honda Vezel 2022 года. Компактный кроссовер-гибрид с низким расходом.'
    }
}

