FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Set working directory
RUN mkdir -p /usr/src/App
WORKDIR /usr/src/App

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Add app and export it to PYTHONPATH
COPY ./App ./App

CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "80"]

