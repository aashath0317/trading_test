From ubuntu:latest
COPY requirements.txt .
RUN apt-get install -y tesseract-ocr
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash", "start.sh"]
