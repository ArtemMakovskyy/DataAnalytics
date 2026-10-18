# DataAnalytics API

FastAPI-додаток: когортний аналіз через REST API.

## Запуск у Cursor (перший запуск після git clone)

Потрібен лише встановлений Python 3.12+.

1. Клонувати та відкрити папку в Cursor:
```powershell
git clone <repo-url>
cd DataAnalytics
```
2. Cursor при відкритті сам запропонує **створити віртуальне оточення (venv)** — погодитись (один клік).
3. Cursor запропонує **встановити залежності (`requirements.txt`)** — погодитись (Install, один клік).
4. Відкрити `app/main.py` і запустити зеленою стрілкою (▶, F5).

Сервер: `http://127.0.0.1:8000/docs` у браузері.
Порт зайнятий (error 10048)? — десь висить старий сервер, зупини його (Ctrl+C у його консолі).

Далі кожен запуск — просто зелена стрілка, лише як хтось новий додав бібліотеку до `requirements.txt`, один раз повтори встановлення залежностей (крок 3).

## Запуск

1. Активувати venv:
```powershell
.\.venv\Scripts\Activate.ps1
```

2. Запустити сервер:
```powershell
uvicorn app.main:app --reload
```
(або зеленою стрілочкою в PyCharm — `app\main.py`)

3. Сервер: `http://127.0.0.1:8000`
Порт зайнятий (error 10048)? — десь висить старий сервер, зупини його (Ctrl+C у його консолі).

## Swagger UI

`http://127.0.0.1:8000/docs` — інтерактивна документація всіх endpoint'ів зі можливістю виклику з браузера.

## Endpoint'и

| Метод | Шлях | Опис |
|---|---|---|
| GET | `/api/test/health` | перевірка живості |
| GET | `/api/cohort-analysis/retention` | retention-звіт (JSON); попутно перезаписує CSV і heatmap у `product/frameworks/cohort/` |

## Структура

```
app/
├── main.py                  # bootstrap: FastAPI + підключення контроллерів
├── controllers/             # endpoint'и (аналог @RestController)
├── services/                # бізнес-логіка (аналог @Service)
├── models/                  # Pydantic DTO
└── data/                    # дані
```
