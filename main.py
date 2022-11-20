def my_function():
    joystickbit.Vibration_Motor(100)
    radio.send_string("diamond")
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
    """)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def on_button_pressed_a():
    radio.send_number(5)
    basic.show_leds("""
        . # # # .
                # . . . #
                # # # # #
                # . . . #
                # . . . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function2():
    joystickbit.Vibration_Motor(100)
    radio.send_string("circle")
    basic.show_leds("""
        . # # # .
                # . . . #
                # . . . #
                # . . . #
                . # # # .
    """)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def on_button_pressed_ab():
    radio.send_number(7)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(6)
    basic.show_leds("""
        # # # # .
                # . . . #
                # # # # .
                # . . . #
                # # # # .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function3():
    joystickbit.Vibration_Motor(100)
    radio.send_string("smile")
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    joystickbit.Vibration_Motor(100)
    radio.send_string("heart")
    basic.show_leds("""
        . # . # .
                # . # . #
                # . . . #
                . # . # .
                . . # . .
    """)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

y = 0
x = 0
joystickbit.init_joystick_bit()
music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
radio.set_group(20)

def on_forever():
    global x, y
    x = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.X),
        1023,
        0,
        -100,
        100)
    y = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.Y),
        0,
        1023,
        -100,
        100)
    radio.send_value("x", x)
    radio.send_value("y", y)
basic.forever(on_forever)
