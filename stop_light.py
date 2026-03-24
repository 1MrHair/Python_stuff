# Raspberry Pi Global Setting
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import RGBLED
from gpiozero import Servo
from time import sleep



right_eye_led = RGBLED(red="BOARD3", green="BOARD5", blue="BOARD7")
left_eye_led = RGBLED(red="BOARD8", green="BOARD10", blue="BOARD12")

green_led = LED('BOARD11')
yellow_led = LED('BOARD13')
red_led = LED('BOARD16')

SERVO_PIN = "BOARD32"   # GPIO pin connected to servo signal wire

def servo_wave(servo):
    """Move servo through min, mid, and max positions."""
    wait = 2 # sleep time in between each movement
    
    print("Moving to MIN...")
    servo.min()
    sleep(wait)

    print("Moving to MID...")
    servo.mid()
    sleep(wait)

    print("Moving to MAX...")
    servo.max()
    sleep(wait)

    print("Back to MID...")
    servo.mid()
    sleep(wait)
    
    print("Moving to MIN...")
    servo.min()
    sleep(wait)
    
    print("Moving to MAX...")
    servo.max()
    sleep(wait)

    servo.detach()   # Stop sending signal — reduces idle jitter

def RGB_255_to_1(rgb):
    r,g,b = rgb
    r_convert = (r/255)
    g_convert = (g/255)
    b_convert = (b/255)
    print(r_convert, g_convert, b_convert)
    return(r_convert, g_convert, b_convert)

def blink(light,wait = 1):
  print("on")
  light.on()
  sleep(wait)
  light.off()
  print("off")

def run_boot_test():
    print("running boot test")
    execute_left_eye()
    execute_rgb_led()
    execute_stop_light()
    
    servo = Servo(SERVO_PIN)
    servo_wave(servo)
    print("Done.")
    
def get_stop_light_command(a):
    b = a["features"]["stop_light"]["traffic"]
    print(b)
    return b
        
def stop_light(a = 0):
    if(a == "stop"):
        blink(red_led)
    if(a == "caution"):
        blink(yellow_led)
    if(a == "go"):
        blink(green_led)
    if(a == "cycle"):
        r,y,g = a
        blink(red_led,r)
        blink(yellow_led,y)
        blink(greenled,g)
        
def execute_stop_light():
    command = {"robot": "Bob", "features": {"stop_light": {"traffic": "stop"}}}
    command = get_stop_light_command(command)
    stop_light(command)
    
    command = {"robot": "Bob", "features": {"stop_light": {"traffic": "caution"}}}
    command = get_stop_light_command(command)
    stop_light(command)
    
    command = {"robot": "Bob", "features": {"stop_light": {"traffic": "go"}}}
    command = get_stop_light_command(command)
    stop_light(command)
    
    command = {"robot": "Bob", "features": {"stop_light": {"traffic": {"mode": "cycle", "red_duration": 5000, "yellow_duration": 2000, "green_duration": 4000}}}}
    command = get_stop_light_command(command)
    mode,r,y,g = command["mode"],command["red_duration"],command["yellow_duration"],command["green_duration"]
    blink(red_led, r/1000)
    blink(yellow_led, y/1000)
    blink(green_led, g/1000)
        
def execute_left_eye():
    command = {"robot": "Bob",  "features": {"eyes": {"set_right_rgb_eye_color": [255, 0, 0]}}}
    eye_command = {"set_left_rgb_eye_color": [30, 17, 55]}
    print(eye_command)
    
    # eye_rgb = (22, 56, 0)
    
    eye_rgb = eye_command["set_left_rgb_eye_color"]
    eye_rgb = RGB_255_to_1(eye_rgb)

    left_eye_led.color = eye_rgb
    sleep(1)
    left_eye_led.color = (0,0,0)
    sleep(1)
    
    eye_rgb = command["features"]["eyes"]["set_right_rgb_eye_color"]
    eye_rgb = RGB_255_to_1(eye_rgb)
    
    left_eye_led.color = eye_rgb
    sleep(1)
    left_eye_led.color = (0,0,0)
    
def execute_rgb_led():
    w = 1
    right_eye_led.color = (1,0,0)
    left_eye_led.color = (1,0,0)
    sleep(w)
    right_eye_led.color = (0,1,0)
    left_eye_led.color = (0,1,0)
    sleep(w)
    right_eye_led.color = (0,0,1)
    left_eye_led.color = (0,0,1)
    sleep(w)
    right_eye_led.color = (0,0,0)
    left_eye_led.color = (0,0,0)


def main():
    print("Starting Program")
    
    run_boot_test()
    
    print("Ending Program")
main()
