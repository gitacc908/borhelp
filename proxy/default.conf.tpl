server {
    listen 8000 ssl;

    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;

    location /test/ {
        root /var/www;
    }

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass             app:9000;
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}