#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    # jeśli nie ma parametru to koniec
    if len(sys.argv) < 2:
        sys.exit(0)

    # ustal maksymalną wartość jasności
    with open('/sys/class/backlight/intel_backlight/max_brightness', 'r') as max_file:
        max_brightness = int(max_file.readline().strip())

        # ustal bieżącą wartość jasności
        with open('/sys/class/backlight/intel_backlight/brightness', 'r+') as cur_file:
            cur_brightness = int(cur_file.readline().strip())

            # ustaw wartość domyślną dla nowej jasności
            new_brightness = cur_brightness
            ten_percent = (0.1 * max_brightness)

            if sys.argv[1] == 'inc':
                # podnieś jasność o 10%
                new_brightness += ten_percent
                if new_brightness > max_brightness:
                    new_brightness = max_brightness
            elif sys.argv[1] == 'dec':
                # zmniejsz jasność o 10%
                new_brightness -= ten_percent
                if new_brightness < 1:
                    new_brightness = 1

            # ustaw
            cur_file.write(str(round(new_brightness)))
