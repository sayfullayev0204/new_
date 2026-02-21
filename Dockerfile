FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir python-decouple gunicorn

COPY . .

# Agar static fayllar bo'lsa (collectstatic kerak bo'lsa)
RUN python manage.py collectstatic --noinput --clear || true

# Gunicorn bilan ishga tushirish
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]