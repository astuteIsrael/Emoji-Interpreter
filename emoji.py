import emoji

def text_to_emoji(text):
    return emoji.emojize(text, use_aliases=True)

input_text = input("Enter text with emoji aliases (e.g., I am feeling :smile: today): ")

converted_text = text_to_emoji(input_text)

print("Converted Text with emojis:", converted_text)
