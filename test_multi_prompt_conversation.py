from loguru import logger
from chatgpt_wrapper import ChatGPT

query_str_1: str = "What color is grass, typically?"
query_str_2: str = "What type of plant did I ask about previously?"

# Init
bot = ChatGPT()

# Ask the bot the first question
success, response, message = bot.ask(query_str_1)
logger.info(f"user query: {query_str_1}")
logger.info(f"chatGPT response: {response}")

# Check if we got a meaningful response
if len(response)> 20 and "green" in response.lower():
    logger.info(f"Mitchell test script tentative success(?) - Got a {len(response.split())} word response that included 'green'!")
else:
    logger.info("Mitchell test script tentative failure - Response did not include the word green!")

# Ask the bot the followup question
success, response, message = bot.ask("What type of plant did I ask about previously?")
logger.info(f"user query: {query_str_2}")
logger.info(f"chatGPT response: {response}")



