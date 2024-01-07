from django.db import models



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # Поле для ввода даты и времени
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")  # Поле для ввода даты и времени
    class Meta:
        abstract = True


class Category(BaseModel):
    product = models.ForeignKey(
        "product.Product",  # Поле для связи с другой моделью
        on_delete=models.CASCADE,  # Поле для связи с другой моделью
        verbose_name="Продукт",  # Название поля в форме (админка, форма регистрации, форма авторизации)
        related_name="categories"  # Поле для обратной связи (по умолчанию appname_classname_set (post_comments_set))
    )
    text = models.TextField(null=True, blank=True, verbose_name="Текст")  # Поле для ввода текста без ограничения

    def __str__(self) -> str:
        return f"{self.text}"

    class Meta:  # Мета класс - Это класс, который содержит дополнительную информацию о модели
        db_table = 'categories'  # Название таблицы в базе данных (по умолчанию appname_classname (post_post))
        verbose_name = 'Категорий'  # Название модели в единственном числе
        verbose_name_plural = 'Категории'  # Название модели во множественном числе


class Product(BaseModel):
    image = models.ImageField(
        upload_to='products',

    text = models.TextField(null=True, blank=True, verbose_name="Текст")  # Поле для ввода текста без ограничения
    grade = models.FloatField(default=0, verbose_name="Оценка")  # Поле для ввода числа с плавающей точкой
    price = models.FloatField(default=0, verbose_name="Цена")  # Поле для ввода числа с плавающей точкой
    # categories = models.ManyToManyField(  # Поле для связи с другой моделью (автомвтически создает промежуточную таблицу)
    #     Category,  # Модель, с которой будет связь
    #     verbose_name="Категории",  # Название поля в форме (админка, форма регистрации, форма авторизации)
    #     related_name="products"  # Поле для обратной связи (по умолчанию appname_classname_set (post_hashtag_set))
    # )

    def __str__(self) -> str:
        return f"{self.title} {self.grade}"


verbose_name_plural = 'Продукты'  # Название модели во множественном числе


# class Like(BaseModel):
# pass

class Review(BaseModel):
    product = models.ForeignKey(
        "product.Product",  # Поле для связи с другой моделью
        on_delete=models.CASCADE,  # Поле для связи с другой моделью
        verbose_name="Продукт",  # Название поля в форме (админка, форма регистрации, форма авторизации)
        related_name="Reviews"  # Поле для обратной связи (по умолчанию appname_classname_set (post_comments_set))
    )
    text = models.TextField(null=True, blank=True, verbose_name="Текст")  # Поле для ввода текста без ограничения

    def __str__(self) -> str:
        return f"{self.text}"



# class ProductInfo(models.Model):
#     product = models.OneToOneField(  # Поле для связи с другой моделью
#         Product,  # Поле для связи с другой моделью
#     class Meta:  # Мета класс - Это класс, который содержит дополнительную информацию о модели
#         db_table = 'product_hashtags'  # Название таблицы в базе данных (по умолчанию appname_classname (post_posthastegs))
#         verbose_name = 'Хэштег Продукт'  # Название модели в единственном числе
#         verbose_name_plural = 'Хэштеги Продуктов'  # Название модели во множественном числе