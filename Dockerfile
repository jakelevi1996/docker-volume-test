FROM python:3.6

WORKDIR /app

COPY requirements.txt . 

RUN python -m pip install -r requirements.txt

COPY . .

CMD ["python", "nnclassification.py"]
# CMD ["python", "printfs.py"]
