# Yolohomie
# we will modify this later

## ohstem PJ link here
```
https://app.ohstem.vn/#!/share/yolobit/2eGZi5dOFd1y0OnYwPC5tWBp1Qk
```
## MQTT code 
**This is the CODE for device manual**

LED : Start with **1** for ON and **2** for OFF
CODE | Function
--- | ---
11 | ON LED 1
12 | ON LED 2
13 | ON LED 3
14 | ON LED 4
21 | OFF LED 1
22 | OFF LED 2
23 | OFF LED 3
24 | OFF LED 4

**You need to send to MQTT server with the following**
```
client.publish(f"{topicName},CODE)

EXAMPLE USAGE:
    client.publish("thinhdadn/feeds/V2/fan", 31)
```
### Function
- pir trong toilet 
    có ng -> bật đèn
    ko có ng -> tắt đèn 
    -> counter đèn bật trong 5p 

- temp < X 
    -> bật quạt
    ->tắt ngược

- rót nước -> sensor < Y
    -> bật máy bơm
    counter -> 30s

- Light SEN 
    sáng > 50 
    -> tắt đèn
    -> bật đèn

- Remote -> mật khẩu 
    -> mở cửa

- Nhận diện AI 
    -> mở cửa 

- bật tắt 4 đèn riêng lẻ

