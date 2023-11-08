import requests
import xml.etree.ElementTree as ET
from django.db import transaction
from django.utils.text import slugify
from .models import Category, Product

def transliterate(text):
    translit = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'є': 'ye',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
        'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh',
        'щ': 'shch', 'ь': '', 'ю': 'yu', 'я': 'ya', ',': '-',' ': '-'
    }

    result = ''.join([translit.get(c, c) for c in text.lower()])
    return result


@transaction.atomic
def run():
    print("Script started")

    # Замініть URL на адресу вашого нового файлу
    url = 'https://ager.ua/yml_prom?code=uk&param=5989'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return

    xml_data = ET.fromstring(response.content)
    print("XML data fetched and parsed")

    # try:
    for category_element in xml_data.findall('.//categories/category'):
        category_id = category_element.get('id')
        category_name = category_element.text.strip()
        category_slug = slugify(transliterate(category_name))

        category, _ = Category.objects.get_or_create(

            category_id=category_id,
            name=category_name,
            slug=category_slug,
        )
        # print(f"Category saved: {category_name}")

    for offer_element in xml_data.findall('.//offers/offer'):
        offer_id = offer_element.get('id')

        group = offer_element.get('group_id')
        available = offer_element.get("available").lower() == 'true'
        product_name = offer_element.find('name').text.strip()
        product_slug = slugify(transliterate(product_name))
        category_id = offer_element.find('categoryId').text.strip()
        category = Category.objects.get(category_id=category_id)
        price = float(offer_element.find('price').text)

        description = offer_element.find('description').text


        vendor_code = offer_element.find('vendorCode').text.strip()


        param_names = [
            "Виробник", "Країна виробник", "Стан", "Декорування", "Довжина",
            "Застібка", "Тип тканини", "Матеріал верху", "Матеріал наповнювача",
            "Матеріал підкладки", "Особливості моделі", "Особливості тканини",
            "Стать", "Сезон", "Склад", "Стиль", "Особливості крою", "Колір",
            "Ціновий сегмент", "Розмір"
        ]

        # Створення словника для збереження значень параметрів
        params = {}
        # Перевірка наявності та отримання значень параметрів
        for param_name in param_names:
            param_element = offer_element.find(f'param[@name="{param_name}"]')
            param_value = param_element.text.strip() if param_element is not None else ''
            params[param_name] = param_value

        manufacturer = params.get("Виробник", '')
        country_of_manufacture = params.get("Країна виробник", '')
        condition = params.get("Стан", '')
        decoration = params.get("Декорування", '')
        length = params.get("Довжина", '')
        fastener = params.get("Застібка", '')
        fabric_type = params.get("Тип тканини", '')
        upper_material = params.get("Матеріал верху", '')
        filler_material = params.get("Матеріал наповнювача", '')
        lining_material = params.get("Матеріал підкладки", '')
        model_features = params.get("Особливості моделі", '')
        fabric_features = params.get("Особливості тканини", '')
        gender = params.get("Стать", '')
        season = params.get("Сезон", '')
        composition = params.get("Склад", '')
        style = params.get("Стиль", '')
        cut_features = params.get("Особливості крою", '')
        color = params.get("Колір", '')
        price_segment = params.get("Ціновий сегмент", '')
        size = params.get("Розмір", '')

        quantity_in_stock = int(offer_element.find('quantity_in_stock').text.strip())


        extraimage_list = offer_element.findall('picture')
        picture1 = ''
        picture2 = ''
        picture3 = ''
        picture4 = ''
        picture5 = ''

        for i, extraimage_element in enumerate(extraimage_list):
            if i == 0:
                picture1 = extraimage_element.text.strip()
            elif i == 1:
                picture2 = extraimage_element.text.strip()
            elif i == 2:
                picture3 = extraimage_element.text.strip()
            elif i == 3:
                picture4 = extraimage_element.text.strip()
            elif i == 4:
                picture5 = extraimage_element.text.strip()

            else:
                break


        if group:
            try:
                # Find an existing product with the same vendor_code
                existing_product = Product.objects.get(group=group)

                # Get the current list of sizes for the existing product
                existing_sizes = existing_product.size # if existing_product.size else []

                # Ensure existing_sizes is always a list
                # if not isinstance(existing_sizes, list):
                #     existing_sizes = existing_sizes

                # Convert the size string into a list containing that string
                size_list = size

                existing_sizes.append(size_list)

                # Update the existing product with the updated size list
                existing_product.size = existing_sizes
                print(existing_sizes)
                existing_product.save()



            except Product.DoesNotExist:
                # If the product doesn't exist, create a new one
                product, _ = Product.objects.get_or_create(
                    offer_id=offer_id,
                    group=group,
                    available=available,
                    category=category,
                    name=product_name,
                    slug=product_slug,
                    price=price,
                    description=description,
                    vendor_code=vendor_code,
                    manufacturer=manufacturer,
                    country_of_manufacture=country_of_manufacture,
                    condition=condition,
                    decoration=decoration,
                    length=length,
                    fastener=fastener,
                    fabric_type=fabric_type,
                    upper_material=upper_material,
                    filler_material=filler_material,
                    lining_material=lining_material,
                    model_features=model_features,
                    fabric_features=fabric_features,
                    gender=gender,
                    season=season,
                    composition=composition,
                    style=style,
                    cut_features=cut_features,
                    color=color,
                    price_segment=price_segment,
                    size=[size],
                    quantity_in_stock=quantity_in_stock,
                    picture1=picture1,
                    picture2=picture2,
                    picture3=picture3,
                    picture4=picture4,
                    picture5=picture5,
                )
                print(f"Product saved: {product_name}")
        else:
            print("Vendor code is missing.")

if __name__ == '__main__':
    run()
