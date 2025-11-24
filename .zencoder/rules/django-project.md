# Zencoder Rules for P2's Spice Company - Django Project

## Project Overview
P2's Spice Company is a Django 5.2.6 web application for a spice business with landing pages and REST API support.

## Key Apps & Structure
- **landing** - Landing/public pages
- **rest_framework** - REST API support

## Code Conventions

### Python & Django Standards
- Python 3.12+
- Line length: 88 characters
- Format: Black formatter
- Linting: Ruff

### Django Patterns
- Use Django ORM with PostgreSQL
- Models: Define in `models.py`
- Views: Class-based views preferred
- Forms: Define in `forms.py`
- URLs: Namespace apps in `urls.py`
- Templates: Use base.html inheritance from `templates/base.html`
- Admin: Register models in `admin.py`

### Project Structure
```
app_name/
├── migrations/          # Auto-generated
├── templates/
│   └── app_name/
├── models.py           # Database models
├── views.py            # Views
├── forms.py            # Forms
├── urls.py             # URL routing
├── admin.py            # Admin interface
├── apps.py             # App config
├── tests.py            # Tests
└── __init__.py
```

### Database Patterns
- Use PostgreSQL (`DATABASE_URL` env var)
- Run migrations: `python manage.py makemigrations && python manage.py migrate`
- Use descriptive model field names

### Testing
- Test files: `tests.py` in each app
- Run tests: `python manage.py test`

### Deployment
- Uses GitHub Actions: `.github/workflows/deploy.yml`
- Collect static files: `python manage.py collectstatic`
- Environment: PostgreSQL, Gunicorn/WSGI
- Requires: SECRET_KEY, DATABASE_URL, ALLOWED_HOSTS env vars

## Security Best Practices
- Never commit `.env` files
- Use `django-environ` for configuration
- CSRF protection: Enabled by default
- SQL Injection: Protected by Django ORM

## Common Tasks

### Adding a New Feature
1. Create models in `app/models.py`
2. Create views in `app/views.py`
3. Create templates in `app/templates/app/`
4. Add URLs in `app/urls.py`
5. Run migrations
6. Test locally
7. Commit and push

## Dependencies
- Django 5.2.6
- PostgreSQL (psycopg2-binary)
- Django REST Framework
- Django Filter
- Black, Ruff
- Markdown

## Environment Variables
- `SECRET_KEY` - Django secret key (required)
- `DEBUG` - Boolean, default False
- `DATABASE_URL` - PostgreSQL connection
- `ALLOWED_HOSTS` - Comma-separated hosts
