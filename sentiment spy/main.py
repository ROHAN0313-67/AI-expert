import colorama
from colorama import Fore, Style
from textblob import TextBlob


colorama.init()

print(f"{Fore.CYAN} welcome to sentiment spy! {Style.RESET_ALL} ")

user_name = input(f"{Fore.MAGENTA} please enter your name:{Style.RESET_ALL}").strip()
if not user_name:
    user_name = "mystery agent"
conversation_history = []

print(f"\n{Fore.CYAN} hello,agent{user_name}!{Style.RESET_ALL}")
print("type a sentence and i will analyze your sentences with TextBlob and show you the sentiment.")
print(
    f"Type{Fore.YELLOW}'reset'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN},"
    f"or{Fore.YELLOW}'exit'{Fore.CYAN}to quit.{Style.RESET_ALL}\n"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED} please enter some valid text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() =='exit':
            print(f"{Fore.BLUE} exiting,bye!.{user_name}!{Style.RESET_ALL}")
            break
    

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN} ALL converstion history cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}no conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}ðŸ“œ Conversation History:{Style.RESET_ALL}")
            for text, polarity, sentiment in conversation_history:
                print(f"- \"{text}\" â†’ {sentiment} ({polarity})")
                continue


    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
            sentiment = 'positive'
            color = Fore.GREEN
    elif polarity < 0:
            sentiment = 'negetive'
            color = Fore.RED
    else:
            sentiment = 'neutral'
            color = Fore.YELLOW


    conversation_history.append((user_input, polarity,sentiment))
    print(f"{color}sentiment:{sentiment}, | polarity score:{polarity}{Style.RESET_ALL}")
    