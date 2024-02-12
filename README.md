# Blood Test Center Chatbot
Welcome to the Blood Test Center Chatbot! This chatbot is designed to assist users inquiring about available blood tests, their prices, and additional information related to blood tests.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Setting Up Dialogflow](#setting-up-dialogflow)
  - [Running the Chatbot](#running-the-chatbot)
- [Customizing and Extending](#customizing-and-extending)
  - [Adding Intents to Dialogflow](#adding-intents-to-dialogflow)
  - [Extending the Chatbot Functionality](#extending-the-chatbot-functionality)
- [Contributing](#contributing)
- [License](#license)

## Overview
This repository contains Python code for a PyQt5-based graphical user interface (GUI) for interacting with the Blood Test Center Chatbot. The chatbot utilizes Google's Dialogflow for natural language processing.

## Features
- Graphical user interface (GUI) for easy interaction with the chatbot.
- Integration with Google Dialogflow for natural language understanding.
- Simple and intuitive user experience.

## Prerequisites
Before running the chatbot, ensure you have the following installed and set up:
- Python 3.x installed on your system.
- A Google Cloud account with Dialogflow enabled.
- The `google-cloud` Python library installed (install using `pip install google-cloud`).
- The PyQt5 library installed (install using `pip install PyQt5`).

## Setup
### Setting Up Dialogflow
1. Create a new Dialogflow agent in the Dialogflow Console.
2. Obtain the service account key JSON file for your Dialogflow agent.
3. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to point to your service account key JSON file.

### Running the Chatbot
1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Run the following command to start the chatbot GUI:
   ```bash
   python chatbot_ui.py
