FROM python:3.11-slim-bullseye

# Устанавливаем утилиты и Chrome
RUN apt-get update && \
    apt-get install -y wget gnupg2 unzip && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Получаем актуальную версию Chrome и устанавливаем совместимый ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}') && \
    CHROME_MAJOR_VERSION=$(echo $CHROME_VERSION | cut -d'.' -f1) && \
    wget -q -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip /usr/local/bin/chromedriver-linux64

WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

CMD ["pytest", "-v", "--alluredir=allure-results"]



#FROM python:3.11-slim-bullseye
## старая версия которая не  узнает какой хром загружен и вызывает ошибку загрузки вебдрайвера
## Устанавливаем утилиты и Chrome
#RUN apt-get update && \
#    apt-get install -y wget gnupg2 unzip && \
#    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
#    apt-get update && \
#    apt-get install -y google-chrome-stable && \
#    rm -rf /var/lib/apt/lists/*
#
## Устанавливаем ChromeDriver
#RUN wget -q -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.185/linux64/chromedriver-linux64.zip" && \
#    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
#    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/ && \
#    chmod +x /usr/local/bin/chromedriver && \
#    rm -rf /tmp/chromedriver.zip
#
#WORKDIR /app
#
## Копируем и устанавливаем зависимости
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
## Копируем весь проект
#COPY . .
#
#CMD ["pytest", "-v", "--alluredir=allure-results"]