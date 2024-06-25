import pywhatkit as kit

text = input("Enter the text you want to convert to handwriting:\n")
kit.text_to_handwriting(text, "handwriting.png", [255, 0, 0])

print(f"Handwriting image saved to handwriting.png")


