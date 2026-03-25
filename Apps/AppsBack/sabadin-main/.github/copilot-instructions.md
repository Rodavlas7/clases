# Workspace Instructions - Proyecto Normalón

## Project Overview

**Proyecto Normalón** is a Django-based bank management system in early development stages. It provides an admin/dashboard interface for managing bank entities.

- **Type**: Django 6.0.3 web application
- **Database**: SQLite3 (`db.sqlite3`)
- **Status**: Core bank model implemented, URL routing and API endpoints incomplete
- **Current Focus**: Stabilizing core models, wiring up views to URLs, building API layer

---

## Architecture & App Structure

### Core Apps

| App | Purpose | Status |
|-----|---------|--------|
| **core/** | Bank model & admin interface | Active - contains Bank model, admin registration, ListBank view |
| **home/** | Homepage/landing page | Skeleton - awaiting implementation |
| **api/** | REST API endpoints (future) | Skeleton - no endpoints wired yet |

### Key Model: Bank (`core/models.py`)

- `name`: Bank identifier (CharField, 32 chars max)
- `level`: Bank hierarchy level (IntegerField, nullable)
- `status`: Active/inactive flag (BooleanField)
- `weight`: Priority weight (FloatField)
- `timestamp`: Auto-created timestamp
- `updated`: Auto-updated timestamp
- `user`: ForeignKey to User (tracks creator)

### Current View: `ListBank` (`core/views.py`)

- Class-based view (inherits from `generic.View`)
- Retrieves all Bank objects: `bank.objects.all()`
- Renders: `templates/core/list.html`
- **Status**: Implemented but NOT wired to any URL route (see Issues below)

---

## URL Structure

### Current State

```
Main URLs (proyecto_normalon/urls.py):
├── /admin/          → Django admin
└── (no other routes configured)
```

### Issues to Fix

- ⚠️ **ListBank view exists but is unreachable** - no URL route defined
- ⚠️ **No app-level urls.py files** - all apps lack internal URL configuration
- ⚠️ **Home app has no routes** - landing page not accessible
- ⚠️ **API app is empty** - no endpoints defined

---

## Development Workflow

### Initial Setup

```bash
# Activate virtual environment
source venv/bin/activate

# Apply Django migrations
python manage.py migrate

# Create superuser for admin interface
python manage.py createsuperuser

# Run development server (default: http://127.0.0.1:8000)
python manage.py runserver
```

### Common Commands

```bash
# Create a new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django admin
# URL: http://127.0.0.1:8000/admin/

# Create test data via shell
python manage.py shell

# Run tests (currently empty)
python manage.py test core home api
```

### If Dependencies File is Needed

```bash
# Install from requirements file (if created)
pip install -r requirements.txt

# Generate requirements from current environment
pip freeze > requirements.txt
```

---

## Code Conventions

### Django Patterns

- **Views**: Use class-based views (CBVs) preferring `generic.View` or other mixins
- **Models**: Define in app `models.py`, register in `admin.py`
- **Templates**: Store in `templates/<app_name>/` directory
- **URLs**: Create `urls.py` per app, include in main `urls.py` with `include()`

### Admin Interface

All models should be registered in respective `admin.py`:
```python
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'level', 'timestamp']
    list_filter = ['status', 'timestamp']
```

### Template Location Convention

- `templates/base/base.html` - Base template with site-wide layout
- `templates/<app_name>/<view_name>.html` - App-specific templates (e.g., `templates/core/list.html`)

---

## Known Issues & Gaps

### Critical Issues

1. **ListBank view unreachable** - View exists but no URL route
   - Solution: Add `path('banks/', ListBank.as_view(), name='bank_list')` to main urls.py or core app urls.py

2. **No requirements.txt** - Dependencies not tracked
   - Suggestion: Create `requirements.txt` with Django 6.0.3 and any additional packages

3. **API app is a skeleton** - No REST framework or endpoints
   - Decision pending: Add Django REST Framework (DRF) or custom API solution?

4. **Static/media files unconfigured** - No STATIC_URL or MEDIA_URL handling
   - Needed if adding file uploads or static assets

### Minor Issues

- Each app has empty `tests.py` - no test coverage yet
- Home app has no templates or views
- No custom forms or validation logic in models

---

## Development Guidelines

### When Adding Features

1. **New models**: Add to app `models.py`, create migrations, register in `admin.py`
2. **New endpoints**: Create view in `views.py`, add to app's `urls.py`, include in main `urls.py`
3. **New templates**: Place in `templates/<app_name>/` subdirectory
4. **Database changes**: Always run `python manage.py makemigrations` then `migrate`

### When Debugging

- Check `core/admin.py` to see if model is registered
- Verify URL routing in both main `urls.py` and app-level `urls.py`
- Look at template rendering in `templates/` directory structure
- Test views in Django shell: `python manage.py shell`

### Common Pitfalls

- **Forgetting to migrate**: New models won't work until `python manage.py migrate` is run
- **Unreachable views**: View exists but not connected to URLs (e.g., ListBank)
- **Template not found**: Ensure template path matches app name convention
- **Static files**: Configure STATIC_ROOT and STATICFILES_DIRS if needed
- **No requirements.txt**: Makes environment setup difficult for others

---

## Quick File Reference

```
proyecto_normalon/
├── settings.py          # Django configuration (DB, apps, middleware)
├── urls.py              # Main URL routing (incomplete - needs app includes)
├── asgi.py             # ASGI server entry point
├── wsgi.py             # WSGI server entry point
│
├── core/                # Bank management app
│   ├── models.py        # Bank model definition
│   ├── views.py         # ListBank view (not yet routed)
│   ├── admin.py         # BankAdmin interface registration
│   └── migrations/      # Database schema migrations
│
├── home/                # Homepage app (skeleton)
├── api/                 # API app (skeleton)
│
├── templates/
│   ├── base/base.html   # Base template layout
│   └── list.html        # Bank list template
│
└── db.sqlite3           # SQLite database file
```

---

## Next Steps Recommended

1. **Fix URL routing** - Connect ListBank view to accessible URL
2. **Create app-level urls.py** - Organize routes by app (core/urls.py, home/urls.py, api/urls.py)
3. **Implement home app** - Add landing page view and template
4. **Choose API solution** - Decide on Django REST Framework vs custom API
5. **Add requirements.txt** - Track dependencies for reproducible setup
6. **Write tests** - Implement unit tests in each app's `tests.py`

---

## Questions Before Getting Started?

If working on the API layer, knowing whether to use **Django REST Framework** or a custom solution would help guide recommendations. Similarly, clarifying the exact scope of the **home app** and **api app** will help avoid suggesting incomplete solutions.
