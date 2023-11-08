from decimal import Decimal
from django.conf import settings
from shop.models import Product ,ProducPhoto


class Cart(object):

    def __init__(self, request): # ініціалізуємо кошик з допомогою обєкта request
        """
        створюєо корзину

        """
        self.session = request.session # тут ми зберігаємо поточну сесію щоб зробити її доступною до інших методів класу Cart
        cart = self.session.get(settings.CART_SESSION_ID) # Тут ми намагаємося отримати кошик із пточноє сесії
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {} # Ми очікуємо, що наш словник кошика буде використовувати коди
        self.cart = cart                                        # продуктів як ключі та словник з кількістю і ціною як значення
                                                                  #    для кожного ключа. Таким чином, ми можемо гарантувати,
                                                                # що продукт не буде додано до кошика більше ніж один раз; можна
                                                                    # також спростити доступ до даних елементів корзини. Якщо в
                                                                         # сесіє нема кошика  ми стоврюємо сесію з порожнім кошиком


    def add(self, product, quantity=1, update_quantity=False, size=None):
        """
        Добавить продукт в корзину і обновить кількість

        """
        product_id = str(product.id) # для додавання чи оновлення кошику
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'size': size}

        if update_quantity:  # Це логічне значення, яке вказує, чи потрібно оновлення кількості із заданою кількістю (True),

            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity # або нова кількість повинна бути додана до існуючої кількості (False)
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart # Зберігає всі ззмінні у кошикус сесії
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True # Це говорить про те, що сесія modified і має бути збережена.

    def remove(self, product):
        """
        Видалення товару з корзин
        Метод remove() видаляє заданий продукт із словника кошика та
        викликає метод save() для оновлення кошика у сесії.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебір елементів в корзині і отримання їх з бази дагих
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids) # У методі __iter__() ми вилучаємо екземпляри продукту, які
        photo = ProducPhoto.objects.all()
                                                       # є в кошику, щоб включити їх у номенклатури кошика.
        product_photos = ProducPhoto.objects.filter(product__in=products)
           # є в кошику, щоб включити їх у номенклатури кошика.
        for product in products:
            cart_item = self.cart[str(product.id)]
            cart_item['product'] = product

            selected_size = cart_item['size']




            product_photo = product_photos.filter(product=product).first()
            if product_photo:
                cart_item['product_photo'] = product_photo.photo  # Assuming the ProductPhoto model has a 'photo' field
            self.cart[str(product.id)] = cart_item


        for item in self.cart.values():   #Нарешті, ми проходимо елементами кошика, перетворюючи ціну номенклатури назад
            # print(item)
            item['price'] = Decimal(item['price'])   # у десяткове число і додаючи атрибут total_price до кожного елементу.
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Підрахунок всіх товарів в корзині.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Підрахунок всіх товарів в кошику
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # Видалення корзини з сесії
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True