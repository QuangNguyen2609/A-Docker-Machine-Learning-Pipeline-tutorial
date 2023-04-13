FROM python:3.8-slim

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip install --no-cache-dir -r requirement.txt

COPY . .

CMD ["bash", "./pipe.bash"]
