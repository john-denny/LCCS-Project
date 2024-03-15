serial.set_baud_rate(BaudRate.BAUD_RATE115200)

def on_forever():
    if input.acceleration(Dimension.STRENGTH) > 1500:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        serial.write_string("1\\n")
        basic.clear_screen()
        basic.pause(5000)
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
