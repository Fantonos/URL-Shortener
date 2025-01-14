import pyshorteners

long_user_url = input("Enter the URL: ")
type_tiny = pyshorteners.Shortener()
short_user_url = type_tiny.tinyurl.short(long_user_url)

print("The Shortened URL: " + short_user_url)
