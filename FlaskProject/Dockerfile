FROM python:3.13-slim
WORKDIR /FlaskProject
COPY . . 
RUN pip install -r requirements.txt
ENV FLASK_APP=flaskr/hello.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]