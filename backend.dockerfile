FROM python:3.7

LABEL maintainer="Pyworks Asia Team <opensource@pyworks.asia>"

# Set working directory
RUN mkdir -p /usr/src/App
WORKDIR /usr/src/App

RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Start scripts
COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

# COPY ./gunicorn_conf.py /gunicorn_conf.py

# Add app and export it to PYTHONPATH
COPY ./App ./App

# CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "80"]

#===== Set environment variables =====
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

#Export your app to Python environment
ENV PYTHONPATH=/usr/src/App

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]
