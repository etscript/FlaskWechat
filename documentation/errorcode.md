200 OK -- [GET]
消费者向服务请求数据，并且服务找到了对应的数据（幂等）
201 CREATED -- [POST/PUT/PATCH]
消费者给服务发送数据，并且服务创建了资源
204 NO CONTENT -- [DELETE]
消费者请求服务删除资源，并且服务成功删除了资源
400 INVALID REQUEST -- [POST/PUT/PATCH]
消费者给服务发送了错误的数据，服务没有进行任何处理（幂等）
404 NOT FOUND -- [*]
消费者请求了一个不存在的资源或者集合，服务没有进行任何处理（幂等）
500 INTERNAL SERVER ERROR -- [*]
服务器发生错误，消费者不清楚请求是否成功