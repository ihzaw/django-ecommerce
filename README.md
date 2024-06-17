# Django E-Commerce Service

Setup Instructions
*Prerequisites*
- Python 3.x installed (preferably Python 3.6+)
- Pip (Python package installer)

*Installation*
1. **Clone the repository**:

```
git clone <repository-url>
cd <repository-name>
```

2. **Create a virtual environment (optional but recommended):**

```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**

```
pip install -r requirements.txt
```

4. **Apply migrations:**

```
python manage.py makemigrations 
python manage.py migrate
```

5. **Create a superuser (if needed):**

```
python manage.py createsuperuser
```

*Running the Application*
6. **To start the Django development server:**
```
python manage.py runserver
```

The application will be accessible at http://localhost:8000.
