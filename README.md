# CRM-система

Практикум Skillbox «Разработка CRM-системы» — веб-приложение для автоматизации
работы с клиентами: учёт услуг, рекламные кампании, потенциальные и активные
клиенты, контракты, статистика по рекламным кампаниям.

## Стек

- Python 3.12, Django 5.2
- PostgreSQL
- Bootstrap 5 (готовый frontend от куратора)
- Pylint, mypy, Pytest — контроль качества кода

## Роли пользователей

- **Администратор** — создаёт пользователей и назначает роли (через `/admin/`)
- **Оператор** — ведёт потенциальных клиентов (лидов)
- **Маркетолог** — ведёт услуги и рекламные кампании
- **Менеджер** — ведёт контракты, лидов, переводит потенциальных клиентов в активные

Все роли видят статистику по рекламным кампаниям.

## Установка и запуск (Windows, PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt

# создать БД и пользователя PostgreSQL (пример):
# createdb crm_system
# psql -c "CREATE USER crm_system WITH PASSWORD 'crm_system';"
# psql -c "GRANT ALL PRIVILEGES ON DATABASE crm_system TO crm_system;"
# psql -d crm_system -c "GRANT ALL ON SCHEMA public TO crm_system;"
# (начиная с PostgreSQL 15 обычная роль не может создавать таблицы в схеме
# public без этого GRANT — без него migrate упадёт с "нет доступа к схеме public")

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Проверка качества кода

```powershell
pylint --rcfile .pylintrc products advertisements leads contracts customers users crm_system
mypy .
pytest
```

## Мониторинг

- `/metrics` — метрики Prometheus (django-prometheus), работает всегда.
- Sentry (отслеживание ошибок) включается, если в `.env` задать `SENTRY_DSN`;
  без него ничего не активируется.
