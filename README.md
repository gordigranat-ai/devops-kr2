# kr2-template

Шаблон приложения контрольной работы № 2: Flask + Redis, счётчик обращений.

- `GET /` — увеличивает счётчик и возвращает строку `KR2 | <STUDENT> | container<id> | hits: <n>`
- `GET /health` — `ok`
- `GET /whoami` — заголовки, полученные приложением
