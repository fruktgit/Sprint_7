Sprint_7/
├── tests/
│   ├── test_create_courier.py
│   ├── test_login_courier.py
│   ├── test_create_order.py
│   ├── test_get_orders_list.py
├── utils/
│   ├── api_client.py
│   ├── data_generator.py
│   ├── config.py
├── requirements.txt
└── README.md

Чтобы сгенерировать Allure-отчёт, введи в терминале PyCharm:

python -m pytest --alluredir allure-results 

Теперь нужно сформировать отчёт в формате веб-страницы. Напиши в терминале PyCharm:

allure serve allure-results 