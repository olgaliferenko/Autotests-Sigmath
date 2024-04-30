pytest test_simple_session.py - для запуска конкретного теста
pytest - это запустит все тесты из этой папки

history - просмотреть историю,т.е. все команды вверх
playwright codegen *здесь url сайта, который тестирую*- записывать тест (плейрайт кодген)
PWDEBUG=1 pytest -s test_example.py = запуск теста пошагово
pytest test_guest.py --browser chromium --browser firefox - запустить тест в разніх браузерах
--device="iPhone 11 Pro" - запустить тест на мобилніх устройствах (айфон напр)
page.screenshot(path= f"screenshot_{email}.png") - часть кода для изготовления скриншота

https://pytest-docs-ru.readthedocs.io/ru/latest/usage.html годная документация