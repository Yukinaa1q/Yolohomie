import paho.mqtt.client as mqtt
import time
import uart

class MQTTController:
    def __init__(self, server, port, username, password,topic_pub, topic_sub = None):
        self.MQTT_SERVER = server
        self.MQTT_PORT = port
        self.MQTT_USERNAME = username
        self.MQTT_PASSWORD = password
        self.MQTT_TOPIC_PUB = topic_pub
        self.MQTT_TOPIC_SUB = topic_sub
        self.mqttClient = mqtt.Client()
        self.mqttClient.username_pw_set(username, password)
        self.mqttClient.connect(server, int(port), 60)
        self.mqttClient.on_connect = self.mqtt_connected
        self.mqttClient.on_subscribe = self.mqtt_subscribed
        self.mqttClient.on_message= self.mqtt_recv_message

        # self.mqttClient.on_publish = self.mqtt_published
        self.mqttClient.loop_start()

    def declare_topic(self, new_topic):
        self.MQTT_TOPIC_PUB.append(new_topic)
        print(f"Subscribed to topic: {new_topic}")
    
    def get_all_topics(self):
        return self.MQTT_TOPIC_PUB

    def mqtt_connected(self, client, userdata, flags, rc):
        # print("Connected successfully!!")
        client.subscribe(self.MQTT_TOPIC_SUB)

    def mqtt_subscribed(self, client, userdata, mid, granted_qos):
        # print("Subscribed to Topic!!!")
        pass

    # def mqtt_published(self, client, userdata, mid):
    #     print("Message published with mid: " + str(mid))
    
    def mqtt_recv_message(self,client, userdata, message):
        if "led" in message.topic:
            if(message.payload.decode("utf-8") == "11"):#turn on LED1
                uart.write_data(11)
            elif(message.payload.decode("utf-8") == "12"):#turn on LED2
                uart.write_data(12)
            elif(message.payload.decode("utf-8") == "13"):#turn on LED3
                uart.write_data(13)
            elif(message.payload.decode("utf-8") == "14"):#turn on LED4
                uart.write_data(14)
            elif(message.payload.decode("utf-8") == "21"):#turn off LED1
                uart.write_data(21)
            elif(message.payload.decode("utf-8") == "22"):#turn off LED2
                uart.write_data(22)
            elif(message.payload.decode("utf-8") == "23"):#turn off LED3
                uart.write_data(23)
            elif(message.payload.decode("utf-8") == "24"):#turn off LED4
                uart.write_data(24)
        if "door" in message.topic:
            if(message.payload.decode("utf-8") == "31"):#open the door
                uart.write_data(31)
            elif(message.payload.decode("utf-8") == "32"):#close the door
                uart.write_data(32)
        if "fan" in message.topic:
            if(message.payload.decode("utf-8") == "40"):#fan off
                uart.write_data(40)
            elif(message.payload.decode("utf-8") == "425"):#fan on 25
                uart.write_data(425)
            elif(message.payload.decode("utf-8") == "450"):#fan on 50
                uart.write_data(450)
            elif(message.payload.decode("utf-8") == "475"):#fan on 75
                uart.write_data(475)
            elif(message.payload.decode("utf-8") == "4100"):#fan on 100
                uart.write_data(4100)
            
        print("Received message " + message.payload.decode("utf-8")
            + " on topic " + message.topic)



    def publish(self,channel, data):
        self.mqttClient.publish(f"thinhdadn/feeds/V2/{channel}", data)


# Example usage:
# def main():
#     pass
    # counter = 5
    # while True:
    #     time.sleep(1)
    #     if counter == 0:
    #         counter = 5
    #     counter -= 1
    #     mqtt_controller.publish_data(counter, counter*2, counter*3, counter*4)

# if __name__ == "main":
    # mqtt_controller = MQTTController("mqtt.ohstem.vn", 1883, "thinhdadn", "hehe",
    #                                     "thinhdadn/feeds/V2/humidity", 
    #                                     "thinhdadn/feeds/V2/temperature",
    #                                     "thinhdadn/feeds/V2/light", 
    #                                     "thinhdadn/feeds/V2/door",
    #                                     "thinhdadn/feeds/V2/#")
    # main()
