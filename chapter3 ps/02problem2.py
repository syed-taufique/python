letter = '''Dear harry <|Name|>,
                You are selected!
                <|date|>'''

print(letter.replace("<|Name|>", "Harry").replace("<|date|>","24 july"))