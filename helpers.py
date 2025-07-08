import random
import string


class HelpersMethods:

    @staticmethod
    def generate_user_data():
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@example.ru'
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 8)))
        password = ''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(random.randint(8, 10)))
        return {
            "email": email,
            "password": password,
            "name": username
        }

    @staticmethod
    def clean_order_number(text):
        return text.replace('#', '').lstrip('0').strip()