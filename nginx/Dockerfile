FROM nginx:latest
COPY nginx-app.conf /etc/nginx/sites-available/
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/