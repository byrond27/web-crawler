FROM python:3

ADD . .

ENV PYTHONPATH "${PYTHONPATH}:/usr/lib/python3"

RUN pip install -r requirements.txt

CMD [ "python3", "src/application/Scraper.py" ]