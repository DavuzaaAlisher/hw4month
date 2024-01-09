'''
models.py - Файл моделей приложения.
migration - Файлы миграций.
классы которые наследуются от models.Model - модели (таблицы в базе данных)
классы которые заканчиваются на Field - поля модели (CharField, TextField, IntegerField, FloatField, BooleanField, DateTimeField, DateField, TimeField, ImageField, FileField, ForeignKey, ManyToManyField, OneToOneField)
в аргументах полей модели можно указывать следующие аргументы (общие для всех полей):
null - указывает на то, что поле может быть пустым (True - может быть пустым, False - не может быть пустым) в базе данных
blank - указывает на то, что поле может быть пустым (True - может быть пустым, False - не может быть пустым) в форме (админка, форма регистрации, форма авторизации)
default - значение по умолчанию
verbose_name - название поля в форме (админка, форма регистрации, форма авторизации)
для полей модели CharField, TextField, IntegerField, FloatField, BooleanField, DateTimeField, DateField, TimeField, ImageField, FileField можно указывать следующие аргументы:
max_length - максимальная длина поля (только для CharField)
choices - список кортежей, который содержит в себе список возможных значений для поля (только для CharField, IntegerField, FloatField, BooleanField)
upload_to - путь к папке, в которую будут загружаться файлы (только для ImageField, FileField)
auto_now_add - автоматически устанавливает текущую дату при создании объекта (только для DateTimeField, DateField, TimeField)
auto_now - автоматически устанавливает текущую дату при создании и обновлении объекта (только для DateTimeField, DateField, TimeField)
validators - список валидаторов для поля (только для CharField, TextField, IntegerField, FloatField, BooleanField) (можно создавать свои валидаторы) (подробнее в документации  https://docs.djangoproject.com/en/3.2/ref/validators/)
__str__ - метод, который возвращает строковое представление объекта (название объекта) например в админке или в консоли
class Meta - Мета класс - Это класс, который содержит дополнительную информацию о модели
OneToOne - один к одному Например: Пост и Информация поста или Пользователь и Профиль
ManyToOne - много ко многим  Например: Пост и Комментарии или Пользователь и Посты
ManyToMany - много ко многим Например: Пост и Хэштеги или Пользователь и Подписки
OneToOneField - поле для связи с другой моделью
ForeignKey - поле для связи с другой моделью
ManyToManyField - поле для связи с другой моделью (автомвтически создает промежуточную таблицу)
BaseModel - базовая модель, от которой наследуются все модели (таблицы в базе данных)
abstract = True - указывает на то, что модель является абстрактной (не создает таблицу в базе данных)
'''
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
        null=True, blank=False,
        verbose_name="Фото"
    )
    title = models.CharField(max_length=255,
                             verbose_name="Заголовок")  # Поле для ввода текста с ограничением в 255 символов
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

    class Meta:  # Мета класс - Это класс, который содержит дополнительную информацию о модели
        db_table = 'product'  # Название таблицы в базе данных (по умолчанию appname_classname (post_post))
        verbose_name = 'Продукт'  # Название модели в единственном числе
        verbose_name_plural = 'Продукты'  # Название модели во множественном числе


# class Like(BaseModel):
# pass
class Review(BaseModel):
    product = models.ForeignKey(
        "product.Product",  # Поле для связи с другой моделью
        on_delete=models.CASCADE,  # Поле для связи с другой моделью
        verbose_name="Отзыв",  # Название поля в форме (админка, форма регистрации, форма авторизации)
        related_name="Отзывы"  # Поле для обратной связи (по умолчанию appname_classname_set (post_comments_set))
    )
    text = models.TextField(null=True, blank=True, verbose_name="Текст")  # Поле для ввода текста без ограничения
