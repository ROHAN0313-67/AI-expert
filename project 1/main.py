print("hello,i'm john.ur new AI assistant! what's ur name?")
name = input()
print(f"that's great....nice to meet u {name}")
print("how was your day?..good/bad")

text = input()

if text == "good!":
    print("that's great...what made it so great?")
elif text == "bad!":
    print("it's alright...tell me how can i make you feel better!")
else:
    print("it's fine!...somtimes a day can be amazing and boring")

print('HOW IS THE WEATHER?')
weather = input()
print(f"{weather}!...looks like it's perfect for an activity or a trip")

print("lets get to know about you!..what's ur favourite book? or a movie?")
book = input()
print(f" oh,{book}! that's a great choice. it's really interesting expecially the story and the visuals are exceptional.")


print("whats your favourite sport?..basketball/football/cricket")
sport = input()
if sport == "basketball":
    print("thats great, who is your favourite basketball player?")
elif sport == "football":
    print("amazing, football is really popular .who is your idol in football?")
if sport == "cricket":
    print("great pick....who is your cricket inspiration?")

fav = input()

print(f"thats fantastic..{fav} is a outstanding player known for his unique play style.")


print(f"it was fun chatting with you{name}, we'll meet tomorrow.....bye!")