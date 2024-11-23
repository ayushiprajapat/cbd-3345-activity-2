FROM python:3.11 
WORKDIR /
COPY . .
RUN pip install -r requirements
EXPOSE 5000
CMD [ "python","main.py"]