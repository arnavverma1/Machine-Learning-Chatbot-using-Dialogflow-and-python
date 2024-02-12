import os
from google.cloud import dialogflow

class BloodTestCenterChatbot:
    def __init__(self):
        # Set up Dialogflow
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_dialogflow_credentials.json"  # Placeholder for dialogflow credentials path
        self.project_id = "your_project_id"  # Placeholder for your project ID
        self.session_id = "unique-session-id"
        self.language_code = "en-US"
        self.session_client = dialogflow.SessionsClient()

    def detect_intent(self, text):
        session = self.session_client.session_path(self.project_id, self.session_id)
        text_input = dialogflow.TextInput(text=text, language_code=self.language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = self.session_client.detect_intent(request={'session': session, 'query_input': query_input})
        return response.query_result

    def respond(self, user_input):
        dialogflow_response = self.detect_intent(user_input)
        fulfillment_text = dialogflow_response.fulfillment_text
        return fulfillment_text

if __name__ == "__main__":
    chatbot = BloodTestCenterChatbot()

    print("Welcome to the Metropolis Chatbot!")
    print("You can ask about available tests, their prices, or additional information.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! Have a great day.")
            break

        response = chatbot.respond(user_input)
        print("BloodBot:", response)
