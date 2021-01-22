# Telegram-Object-Detection-Bot

This projects aims to make a [Telegram](https://telegram.org) bot that takes in an image and then tries to classify the objects that can be seen.

## Credits

This is based on:
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [SightSeer](https://github.com/rish-16/sight)
- [TensorFlow](https://www.tensorflow.org/)

## How do I run this?

**This code is tested on python 3.7.9 and uses tensorflow 1.15**

1. Install Anaconda or Miniconda
2. `conda create --name <env> --file requirements.txt`
3. `conda activate <env>`
4. Run it `python main.py`

**The program will download the weights needed when it's ran for the first time, this may take a while.**


## API Keys

You'll need a Telegram Bot Token, you can get it via BotFather ([more info here](https://core.telegram.org/bots)).
Then change the telegram_bot_token variable inside the **main.py** file to your own bot token.

## TO-DO

- Fix the model so that it gets loaded before a picture is sent.
- Fix the model so that it runs faster.
- Return a matplotlib graph that shows that objects.