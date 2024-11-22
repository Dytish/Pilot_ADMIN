#!/bin/sh

# Подставляем переменные окружения в шаблон
envsubst '${HOST}' < /etc/nginx/templates/nginx.template.conf > /etc/nginx/conf.d/default.conf

# Запускаем nginx
exec "$@"
