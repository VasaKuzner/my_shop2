from django.db.models import Count

from .models import *

menu = [{'title': 'Про сайт','url_name':'about'},
        {'title': 'Добавити машину ','url_name':'add_car'},
        {'title': 'Зворотній звязок','url_name':'contact'},
        {'title': 'Замовити покраску ','url_name':'order'},
        {'title': 'Класні фото з нету   ','url_name':'like_photo'},

]
class DataMixin:
    paginate_by = 3  # Кількість постів на сторінц

    def get_user_context(self, **kwargs):
        context = kwargs #

        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        # context['photo'] = photo
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context