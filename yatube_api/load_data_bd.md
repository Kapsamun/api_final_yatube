# Проверка миграций
В терминале ввести команду
```bash
python yatube_api/manage.py makemigrations
```

# Применение миграций
В терминале ввести команду
```bash
python yatube_api/manage.py migrate
```

# Загрузка данных из Json
В терминале ввести команду
``` bash
python yatube_api/manage.py loaddata yatube_api/data.json
```

# Создание админа
В терминале ввести команду
``` bash
python yatube_api/manage.py createsuperuser
```
Далее ввести следующие команды (можно целиком скопировать и вставить):
```bash
root
root@root.com
5eCretPaSsw0rD
5eCretPaSsw0rD
```

# Создание тестового пользователя regular_user
В терминале ввести команду
``` bash
python yatube_api/manage.py shell
```

Далее ввести следующие команды (можно целиком скопировать и вставить):

```bash
from django.contrib.auth.models import User

# Создаем пользователя regular_user
username_text = 'regular_user'
password_text = 'iWannaBeAdmin'
user, created = User.objects.get_or_create(
    username=username_text,
    defaults={
        'email': f'{username_text}@example.com',
        'is_active': True
    }
)

if created:
    user.set_password(password_text)
    user.save()
    print(f"Пользователь {username_text} создан с паролем {password_text}")
else:
    print(f"Пользователь {username_text} уже существует")
    # Если существует, обновляем пароль
    user.set_password(password_text)
    user.save()
    print(f"Пароль обновлен на {password_text}")
    
    quit()
```

# Создание тестового пользователя second_user
В терминале ввести команду
``` bash
python yatube_api/manage.py shell
```

Далее ввести следующие команды (можно целиком скопировать и вставить):

```bash
from django.contrib.auth.models import User

# Создаем пользователя regular_user
username_text = 'second_user'
password_text = 'password123'
user, created = User.objects.get_or_create(
    username=username_text,
    defaults={
        'email': f'{username_text}@example.com',
        'is_active': True
    }
)

if created:
    user.set_password(password_text)
    user.save()
    print(f"Пользователь {username_text} создан с паролем {password_text}")
else:
    print(f"Пользователь {username_text} уже существует")
    # Если существует, обновляем пароль
    user.set_password(password_text)
    user.save()
    print(f"Пароль обновлен на {password_text}")
    
    quit()
```

# Создание подписок (при необходимости)
В терминале ввести команду
``` bash
python yatube_api/manage.py shell
```

Далее ввести следующие команды (можно целиком скопировать и вставить):

``` bash
from django.contrib.auth.models import User
from posts.models import Follow

# Получаем всех пользователей
users = User.objects.all()
print("Доступные пользователи:")
for user in users:
    print(f"- {user.username} (id: {user.id})")

# Создаем подписки
for user in users:
    # Исключаем текущего пользователя и выбираем 2 других
    authors_to_follow = [u for u in users if u != user][:2]
    for author in authors_to_follow:
        # Пробуем разные варианты имени поля
        try:
            # Вариант 1: если поле называется 'following'
            follow, created = Follow.objects.get_or_create(user=user, following=author)
            if created:
                print(f"{user.username} подписан на {author.username}")
        except:
            try:
                # Вариант 2: если поле называется 'author'
                follow, created = Follow.objects.get_or_create(user=user, author=author)
                if created:
                    print(f"{user.username} подписан на {author.username}")
            except Exception as e:
                print(f"Ошибка при создании подписки: {e}")

print("Подписки созданы!")

quit()
```