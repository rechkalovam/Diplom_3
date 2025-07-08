
# 🧪 Автоматизированные UI-тесты для Stellar Burgers

Проект для проверки веб-интерфейса сайта [stellarburgers.nomoreparties.site](https://stellarburgers.nomoreparties.site) с использованием Selenium и Allure.

## 📌 Стек технологий

- Python 3.9+
- [Selenium WebDriver](https://www.selenium.dev/)
- [Pytest](https://docs.pytest.org/)
- [Allure Reports](https://docs.qameta.io/allure/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- [Firefox GeckoDriver](https://github.com/mozilla/geckodriver)

---
## 🚀 Запуск тестов

### По умолчанию:

```bash
pytest -v --alluredir=allure_results
```

### Запуск с указанием браузера:

```bash
pytest -v --browser=chrome --alluredir=allure_results
pytest -v --browser=firefox --alluredir=allure_results
```
---

## 📊 Генерация Allure-отчета

### Генерация и открытие отчета:

```bash
allure serve allure_results
```

### Только генерация:

```bash
allure generate allure_results --clean -o allure-report
```

### Открытие ранее сгенерированного отчета:

```bash
allure open allure-report
```

---

## 🧪 Структура проекта

```bash
.
├── pages/                 # Page Object Model
├── tests/                 # Тесты
├── locators/              # Локаторы элементов
├── helpers.py             # Вспомогательные функции
├── requirements.txt       # Зависимости
├── data.py                # Вспомогательные данные
├── conftest.py            # Фикстуры
├── urls.py                # Урлы
└── README.md              # Документация
```

---

## ✅ Покрытие тестами

- Авторизация (логин/логаут)
- Переход по меню
- Работа с заказами
- Работа со списком заказов
- Личный кабинет
- Проверка модальных окон
