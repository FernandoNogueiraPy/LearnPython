FROM python:3.11.8
RUN useradd -m -s /bin/bash guest_user
USER guest_user
WORKDIR /code
COPY requirements.txt /code/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT [ "python","main.py" ]