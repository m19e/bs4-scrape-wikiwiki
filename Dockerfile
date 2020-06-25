FROM python:3
ADD src/ /src/
WORKDIR /src/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "main.py" ]
