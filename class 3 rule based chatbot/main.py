import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {

"beaches": ["Bali", "Maldives", "Phuket"],

"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

"cities": ["Tokyo", "Paris", "New York"]

}

jokes = [

"Why do programmers prefer dark mode?Because light attracts bugs",

"Why did the Maths books is always sad ? Because it has problems ",

"Why don’t secrets last in a family?Because someone always spills the tea ☕😄"

]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travelbot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "you:")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.CYAN + f"Travelbot: how about {suggestion}?")
        print(Fore.GREEN + f"do you like it?yes or no?")
        answer = input(Fore.LIGHTRED_EX + 'you:').lower()

        if answer == "yes":
            print(Fore.GREEN + f"travelbot:awesome! enjoy{suggestion}!")
        elif answer == 'no':
            print(Fore.GREEN + "travelbot: let's try another.")
        else:
            print(Fore.RED + "travelBot: let's try another.")
            recommend()
    else:
        print(Fore.RED + "travelBot: sorry, I don't have that type of destination.")

    show_help()


def packing_tips():
    print(Fore.CYAN + "TravelBot: where to/")
    location = normalize_input(input(Fore.YELLOW + "you :"))
    print(Fore.CYAN + "TravelBot: how many days?")
    days = input(Fore.YELLOW + "you: ")

    print(Fore.GREEN + f"Trvel.Bot: packing tips for {days} days in {location}:")
    print(Fore.GREEN + '- pack versatile clothes.')
    print(Fore.GREEN + '- bring charger / adapters.')
    print(Fore.GREEN + "- check the weather forecast.")


def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")


def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- suggest travel spots(say'recommendation')")
    print(Fore.GREEN + "- offer packing tips(say 'packing')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end. \n")


def chat():
    print(Fore.CYAN + 'HELLO! iam TRAVELBOT.')
    name = input(Fore.YELLOW + "whats your name:")
    print(Fore.GREEN + f"nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}:")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "paking" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif " exit" in user_input or 'bye' in user_input:
            print(Fore.CYAN + "TravelBot: safe travels! GOODbye!")
            break
        else:
            print(Fore.RED + "TravelBot: could you rephrase?")


if __name__ == "__main__":
    chat()


