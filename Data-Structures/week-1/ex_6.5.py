text = "X-DSPAM-Confidence:    0.8475";

text = text [text.find('0'):]
text = float(text)
print (text)