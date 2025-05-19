# pdp

## Запуск проекта

Из директoрии проекта выполнить команду

`docker compose  -p pdp up -d --build`

После запуска апи будет доступна по [http://0.0.0.0:8000/docs#/default/send_message_send_message_post](http://0.0.0.0:8000/docs#/default/send_message_send_message_post)

UI интерфейс кафки по [http://0.0.0.0:8090/](http://0.0.0.0:8090/)

Отправив сообщение через апи оно попадет в кафку после будет получено 2мс из топика send_message.
2мс отправит сообщение в другой топик кафки received_message. 
Сообщение можно будет увидеть в UI кафки.