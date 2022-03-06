FROM python:3.7.4

WORKDIR /app

ENV FLASK_APP=app.py 

ENV FLASK_ENV=development

RUN python3 -m venv /opt/venv

COPY ./requirements.txt .

RUN . /opt/venv/bin/activate

RUN python -m pip install --upgrade pip
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]