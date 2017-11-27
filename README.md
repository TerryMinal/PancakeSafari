# CLEVER GIF, brought to you PancakeSafari
**Adam Abbas, Terry Guan, Irene Lam, Shannon Lau**

## Overview
Welcome to Clevergiph! In this site, we've fused the Cleverbot and Giphy APIs. Visitors will be able to talk to a Cleverbot (via API calls), while gifs will pop up based on the context of the conversation. The user can save his/her favorite gif, which can be updated throughout the conversation. Once the user quits the conversation, the conversation history will also be saved alongside the favorite gif. All conversation histories can be accessed at any time, but the user will not be able to respond to the conversation.

## Dependencies
- Python 2.7
- Flask
- Requests
- HTML/CSS

## Launching the Program

#### Installing Your Virtual Environment/Flask/Requests
Flask needs to be installed in order to run this program. It is ideally stored in a virtual environment (venv). 

To install a venv (with the name <name>), run these commands in your terminal:

```
$ pip install virtualenv
$ virtualenv <name>
```
On Mac/Linux, start up your venv with:
```
$ . <name>/bin/activate
```
On Windows:
```
$ . <name>/Script/activate
```
In your activated venv, run the following:
```
$ pip install flask
$ pip install requests
```

#### Acquiring API Keys
Procure your [Cleverbot](https://www.cleverbot.com/api/) API key:
1. Add *API 5K Free Trial* to your cart.
2. Fill out billing details, including name, email address, phone, address, and user password.
3. Your key will appear after placing the order.

For your [Giphy](https://developers.giphy.com):
1. Click *Create an App*.
2. Enter account credentials.
3. Enter app name and description (CLEVERGIF, an application that generates GIFs wwhile chatting with Cleverbot)
4. Your key will appear on your dashboard.

#### Run It!
1. Clone the repo by running:
```
$ git clone git@github.com:slau8/PancakeSafari.git
```
2. With your virtual environment activated, run these commands:
```
$ cd PancakeSafari
$ python app.py
```
3. Add your API keys in their corresponding location in ``` keys.txt ```. For example:
```
Cleverbot: abc123
Giphy: def456
```
4. You can then view the webpage by opening the URL `localhost:5000` in a web browser.
