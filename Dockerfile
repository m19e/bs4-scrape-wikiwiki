FROM python:3
ADD src/ ./
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "main.py" ]
