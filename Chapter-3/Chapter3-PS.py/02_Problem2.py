letter = '''Dear <|Name|>
you are selected
<|Date|>'''

print(letter.replace("<|Name|>)", "Waseem").replace("<|Date|>", "24 Jan 2050"))