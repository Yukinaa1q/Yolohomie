# Yolohomie
# we will modify this later

## ohstem PJ link here
```
https://app.ohstem.vn/#!/share/yolobit/2eGZi5dOFd1y0OnYwPC5tWBp1Qk
```
## MQTT code 
**This is the CODE for device manual**

*LED* : Start with **1** for ON and **2** for OFF

*DOOR* : Start with **3**

*FAN* : Start with **4**
LED | Function  |       | DOOR  | Function  |       | FAN | Function
--- | ---       | ---   | ---   | ---       | ---   | --- | ---
11  | ON LED 1  |       | 31    | Opendoor  |       | 40  | Fan OFF
12  | ON LED 2  |       | 32    | closedoor |       | 425 | Fan 25%
13  | ON LED 3  |       |       |           |       | 450 | Fan 50% 
14  | ON LED 4  |       |       |           |       | 475 | Fan 75%
21  | OFF LED 1 |       |       |           |       | 4100| Fan 100%
22  | OFF LED 2 |       |       |           |       |   |
23  | OFF LED 3 |       |       |           |       | |
24  | OFF LED 4 |       |       |           |       | |

**You need to send to MQTT server with the following**
```python
#python
#client.publish(f"{topicName},CODE)

#EXAMPLE USAGE:
client.publish("thinhdadn/feeds/V2/led", 12)
client.publish("thinhdadn/feeds/V2/led", 24)
client.publish("thinhdadn/feeds/V2/door",31)
client.publish("thinhdadn/feeds/V2/fan", 475)
```
## APP function
- TOGGLE LED[1:4]
- Fan control
- Door open
- Chart water
- Display room temp/humi
- Auth




## Function
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

