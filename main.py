#AI chat bot
print("hello!, i'm john...ur new ai chatbot. what's your name?....")
name = input()

print(f"nice to meet you,{name}")

print("how was your day?...good or bad?")
day = input().lower()

if day =="good":
    print("that's great...seems like you had a great day!")
elif day =="bad":
    print("that's alright...sometimes your day might not be fun, you don't need to be sad.")
else:
    print("i see, sometimes it's hard to express how our day was in words.")

print(f"it was really fun chatting with you,{name}")