# Usar una imagen base de Python
FROM python:3.11

WORKDIR /listas_negras

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /listas_negras

# Comando para ejecutar la aplicación Flask
CMD ["python", "-m", "src.main"]