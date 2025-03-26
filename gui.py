import RPi.GPIO as GPIO
import tkinter as tk


GPIO.setmode(GPIO.BCM)
RED_LED = 36 
GREEN_LED = 12 
BLUE_LED = 15 
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)


def turn_on_led(color):
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)

    if color == "red":
        GPIO.output(RED_LED, GPIO.HIGH)
    elif color == "green":
        GPIO.output(GREEN_LED, GPIO.HIGH)
    elif color == "blue":
        GPIO.output(BLUE_LED, GPIO.HIGH)

# GUI Setup
root = tk.Tk()
root.title("LED Control")

# Radio Buttons
selected_color = tk.StringVar(value="None")

tk.Radiobutton(root, text="Red", variable=selected_color, value="red", command=lambda: turn_on_led("red")).pack()
tk.Radiobutton(root, text="Green", variable=selected_color, value="green", command=lambda: turn_on_led("green")).pack()
tk.Radiobutton(root, text="Blue", variable=selected_color, value="blue", command=lambda: turn_on_led("blue")).pack()

# Exit Button
tk.Button(root, text="Exit", command=lambda: (GPIO.cleanup(), root.quit())).pack()

root.mainloop()
