FROM mcr.microsoft.com/windows/nanoserver:1803-amd64
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
