FROM mcr.microsoft.com/windows-amd64
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
