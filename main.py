import machine
import time
import ubinascii
import machine
import micropython
from umqttsimple2 import MQTTClient
from door import door
from dcmotor import DCMotor


def connect():
    print('Connecting to MQTT Broker...')
    client = MQTTClient(client_id, MQTT_SERVER)
    client.connect()
    print('Connected to %s MQTT broker' % (MQTT_SERVER))
    return client


def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

MQTT_SERVER = '91.121.93.94' # Replace with your MQTT Broker IP

client_id = ubinascii.hexlify(machine.unique_id())
TOPIC_PUB  = 'esp32/led'
coopDoor = door(14, 2)
MOTOR_PIN1 = machine.Pin(5, machine.Pin.OUT)
MOTOR_PIN2 = machine.Pin(4, machine.Pin.OUT)
MOTOR_FREQUENCY = 15000
MOTOR_PWM = machine.PWM(machine.Pin(13), MOTOR_FREQUENCY)
dc_motor = DCMotor(MOTOR_PIN1, MOTOR_PIN2, MOTOR_PWM)


# try:
#     client = connect()
# except OSError as e:
#     restart_and_reconnect()

while True:
    try:
        # client.check_msg()
        msg = coopDoor.get_doorState()  # get the state of the coop door
        print(msg)
        # client.publish(topic_pub, msg)
        if msg == "Open":
            dc_motor.run_forward(10, 75)
        elif msg == "Closed":
            dc_motor.run_backward(10,75)
    except OSError as e:
        restart_and_reconnect()
