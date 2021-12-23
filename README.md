# microservices
##Задача
Есть 4 сервиса(Rest API):
1) gateway
2) stateless -- получает запрос с текстом и герерирует продолжение данного текста(на основе rugpt-3 large)
3) archiever -- mysql
4) stateful -- Хранит статистику по запросам(самые частые темы для герерации и тд)

##Стек технологий:
Flask, Torch, Mysql
