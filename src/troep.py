from gpiozero import Button

button = Button(2)

def hallo():
        print("pressed")

if button.is_pressed:
    print("pressed")

button.wait_for_press()
if button.when_pressed:
    print("gedrukt")

