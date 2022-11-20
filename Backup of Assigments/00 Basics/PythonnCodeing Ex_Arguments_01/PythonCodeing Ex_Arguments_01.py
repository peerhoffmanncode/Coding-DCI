# The application in this file will read the command line options using `sys.argv`.
# If one of the options is `--help`, it should output a small help text.
# If one of the options is `--fast` is should print the text "fast mode enabled" to the command line.
# If `--fast` is not one of the options it should print the text "slow mode enabled" to the command line.

import sys

script = sys.argv[0]
fast_mode = False

for arg in sys.argv[1:]:
    if arg == '--fast':
        fast_mode = True
    if arg == '--help':
        print("====================")
        print("=== HELP MENU ======")
        print("====================")
        print("\nUsage:")
        print("\n  --fast : to enable fast mode")

if fast_mode is True:
    print ("\nfast mode enabled")
else:
    print ("\nslow mode enabled")