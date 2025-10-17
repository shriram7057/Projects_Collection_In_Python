# url_shortener.py
import pyshorteners
url = input("Enter URL: ")
short = pyshorteners.Shortener().tinyurl.short(url)
print("🔗 Shortened URL:", short)
