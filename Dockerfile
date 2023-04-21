# Utilizar una imagen base de Python
FROM python:3.9

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear un directorio de trabajo
RUN mkdir /app
WORKDIR /app

# Copiar archivo .env al directorio de trabajo
COPY .env /app/

# Instalar dependencias
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copiar el proyecto
COPY . /app/

# Exponer el puerto por el que se ejecutará la aplicación
EXPOSE 8000

# Ejecutar Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "amazon_api.wsgi:application"]