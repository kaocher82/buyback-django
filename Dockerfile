FROM python
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY buyspy/ app/

VOLUME /app/media/
VOLUME /app/static/

# make static and media accessible to nginx and create secret key

RUN chmod -R 777 /app/media/ && chmod -R 777 /app/static/ && chmod a+x /app/bin/start.sh

EXPOSE 8000
CMD /app/bin/start.sh
