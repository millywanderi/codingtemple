#!/usr/bin/env python3

# Search for the first white-space character in the string
 txt = "The rain in Spain"
 x = re.search("\s", txt)
 print("The first white-space character is located in position:", x.start())
