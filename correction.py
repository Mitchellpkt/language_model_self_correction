from loguru import logger
from chatgpt_wrapper import ChatGPT

# Init
bot = ChatGPT()


def ask_and_copyedit(bot, query, verbose=True):
    # Ask the bot the first question
    success, response, message = bot.ask(query)

    # If verbose is True, log the original response
    if verbose:
        logger.debug(f"\nchatGPT original response:\n{response}")

    # Ask bot to copyedit its own response
    copyedit_query = f"Please copyedit this response:\n\n{response}"
    success, copyedited_response, message = bot.ask(copyedit_query)

    return copyedited_response


delimiter = "=" * 50 + "\n"


def main():
    print("Welcome! Type 'exit' as your [User] prompt to quit")

    # Ask if wants verbose, defaulting to False
    verbose_str = input(
        "Diagnostics mode (shows intermediate replies)? [default off] (y/n): "
    )
    if "y" in verbose_str.lower():
        verbose: bool = True
    else:
        verbose: bool = False

    while True:
        # Get user's query
        user_str = input(f"{delimiter}[User]: ")
        print("--> (sent)")

        # If the user types 'exit', break the loop
        if user_str.lower() == "exit":
            break

        # Get and print copyedited response
        response = ask_and_copyedit(bot, user_str, verbose=verbose)
        print(f"{delimiter}[ChatGPT]: {response}\n")


if __name__ == "__main__":
    main()
