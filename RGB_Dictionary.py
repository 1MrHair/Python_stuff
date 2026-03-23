from gpiozero import RGBLED
from time import sleep

right_eye_led = RGBLED(red="BOARD3", green="BOARD5", blue="BOARD7")
left_eye_led = RGBLED(red="BOARD8", green="BOARD10", blue="BOARD12")

def RGB_255_to_1(rgb):
    r,g,b = rgb
    r_convert = (r/255)
    g_convert = (g/255)
    b_convert = (b/255)
    print(r_convert, g_convert, b_convert)
    return(r_convert, g_convert, b_convert)

def main():
    print("Starting Program")
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
    
    

    print("Ending Program")

main()
