FROM python:3.10-slim

WORKDIR /app

# Install system-level dependencies (needed for scikit-learn)
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy code and model files
COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files (for using the admin panel)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Run app using Gunicorn
CMD ["gunicorn", "digital_twin.wsgi:application", "--bind", "0.0.0.0:8000"]
