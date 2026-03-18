#!/usr/bin/env python3

import re

# Replace every white-space character with the number 9
txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)

# Replace the first 2 occurrences
x = re.sub(r"\s", "9", txt, 2)
print(x)

# Formatting Phone Numbers
number = "(254) 710-507710"
formatted_number = re.sub(r"\D", '', number)
print(formatted_number)

# Anonymizing Chat User Mentions
chat = '''
@bree: "I think I love Regex"
@Chloe: "Aren't you married?"
@Yvone123: "It's not just the same"
@Peter: "They better not see this"
'''

anon_chat = re.sub(r"@[\w-]+", "@user-anon", chat)
print(anon_chat)
