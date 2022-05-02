FROM python:3.7-alpine
 
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
# RUN pip install -r /requirements.txt
# RUN apk del .tmp-build-deps

RUN mkdir /app
COPY ./app /app
COPY ./scripts /scripts
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # apk add --update --no-cache --virtual .tmp-build-deps \
    # gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-build-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts 

RUN apk add gettext
ENV PATH="/scripts:/py/bin:$PATH"
EXPOSE 8000
CMD ["run.sh"]