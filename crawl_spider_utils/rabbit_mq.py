# -*- coding:utf-8 -*-
"""
File Name: log
Version:
Description:
Author: liuxuewen
Date: 2018/1/8 14:23
"""
import pika
import time
import string
import json

host = '99.48.58.244'
username = 'admin'  # 指定远程rabbitmq的用户名
pwd = '12345'  # 密码
queue_name = 'test'  # 队列名
user_pwd = pika.PlainCredentials(username, pwd)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host, port=5672,
                              credentials=user_pwd))  # 创建连接

channel = connection.channel()  # 连接上创建一个频道

# durable 表示是否持久化,
# exclusive是否排他，如果为True则只允许创建这个队列的消费者使用,
# auto_delete 表示消费完是否删除队列
channel.queue_declare(queue=queue_name, durable=True, exclusive=False,
                      auto_delete=False)  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行


# 生产者，发送消息
def send_message(data):
    # 需要将字典dumps成字符串
    channel.basic_publish(exchange='',  # 交换机
                          routing_key=queue_name,  # 路由键，写明将消息发往哪个队列，本例是将消息发往队列queue_name

                          body=json.dumps(data),  # 生产者要发送的消息
                          properties=pika.BasicProperties(
                              delivery_mode=2, )  # 设置消息持久化，将要发送的消息的属性标记为2，表示该消息要持久化)
                          )


# 消费者，接收消息
def receive_message():
    # prefetch_count设置为3，表示同一时刻，只接受最多三个消息
    channel.basic_qos(prefetch_count=3)
    channel.basic_consume(callback, queue=queue_name)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.close()
        connection.close()


def callback(ch, method, properties, body):
    result = handle_data(body)
    if result == 1:
        print(" [消费者] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)  # 接收到消息后会给rabbitmq发送一个确认
    else:
        print(" [x] handle data error")
        ch.basic_reject(delivery_tag=method.delivery_tag)


# 代写接口,处理下一步的数据
def handle_data(body):
    try:
        data = json.loads(body)
        print(" [消费者] Received {}".format(data))
        time.sleep(10)
    except:
        return 0
    else:
        return 1


if __name__ == '__main__':
    send = False
    # 发送数据
    if send:
        message = [{k: v} for k, v in enumerate(string.ascii_lowercase)]
        for m in message:
            print(m)
            send_message(data=m)

    # 接受数据
    else:
        receive_message()
