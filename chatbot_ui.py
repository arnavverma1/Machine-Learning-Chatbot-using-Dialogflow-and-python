import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser, QLineEdit, QPushButton, QCompleter, QLabel
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QMovie
from PyQt5.QtCore import Qt
from threading import Thread
from blood_test_center_chatbot import BloodTestCenterChatbot

class ChatbotUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create an instance of the BloodTestCenterChatbot
        self.chatbot = BloodTestCenterChatbot()

        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        main_layout = QVBoxLayout()

        # Text browser for chat history
        self.chat_history = QTextBrowser()
        self.chat_history.setFont(QFont("Adria Sans", 14))  # Change font to Adria Sans
        self.chat_history.setStyleSheet("background-color: white; color: black;")  # Set background to white, text color to black
        main_layout.addWidget(self.chat_history, 1)

        # Input field for user messages and Send button
        input_layout = QHBoxLayout()
        self.user_input = QLineEdit()
        self.user_input.setFont(QFont("Adria Sans", 12))  # Change font to Adria Sans

        # Set the text color to white in the input field
        input_palette = QPalette()
        input_palette.setColor(QPalette.Text, Qt.white)
        self.user_input.setPalette(input_palette)

        # Autocomplete completer
        completer = QCompleter(["what tests are available", "how are you", "hello", "i want to give blood test", "i want to give blood test from home", "tell me about the sugar test", "how much is the blood sugar test", "Customer Service", "Booking", "test10", "test11", "test12", "test13", "test14", "test15", "test16", "test17", "test18", "test19", "test20", "test21", "test22", "test23", "test24", "test25"]) 
        completer_popup = completer.popup()
        completer_popup.setFont(QFont("Adria Sans", 12))  # Change font to Adria Sans
        self.user_input.setCompleter(completer)

        input_layout.addWidget(self.user_input)

        send_button = QPushButton()
        send_button.setIcon(QIcon("path_to_icon.png"))  # Placeholder for icon path
        send_button.clicked.connect(self.send_message)
        send_button.setFixedSize(80, 30)  # Set the size of the button
        input_layout.addWidget(send_button)

        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

        # Connect the returnPressed signal to the send_message method
        self.user_input.returnPressed.connect(self.send_message)

        # Make the "Send" button the default button
        self.user_input.setPlaceholderText("Type your message here...")
        self.user_input.setFocus()
        self.user_input.setMaxLength(1000)  # Set an appropriate maximum length for the input

        send_button.setDefault(True)

        # Display welcome message
        self.display_message("Welcome to the Metropolis Chatbot!\n"
                             "You can ask about available tests, their prices, or additional information.\n"
                             "Type 'exit' to end the conversation.\n", is_user=False)

        self.setWindowTitle('Blood Test Center Chatbot')
        self.setGeometry(100, 100, 800, 600)

        # Apply style to the UI
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;  /* Black background */
            }
            QLineEdit {
                background-color: #111111;  /* Dark gray for user input */
                border: 1px solid #333333;  /* Dark gray border */
                padding: 8px;
                margin: 2px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #42474A;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 5px;
                font-size: 12px;   
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.show()

    def send_message(self):
        user_input = self.user_input.text()
        self.display_message(user_input, is_user=True)

        if user_input.lower() in ['exit', 'quit', 'bye']:
            self.display_message("Goodbye! Have a great day.", is_user=False)
            self.close()
            return

        # Display the loading GIF
        loading_label = QLabel()
        movie = QMovie("path_to_loading.gif")  # Placeholder for loading GIF path
        loading_label.setMovie(movie)
        movie.start()
        self.chat_history.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(loading_label)

        # Use threading to run the chatbot processing in the background
        thread = Thread(target=self.process_chatbot_response, args=(user_input,))
        thread.start()

    def process_chatbot_response(self, user_input):
        response = self.chatbot.respond(user_input)
        self.update_ui_with_response(response)

        # Clear user input
        self.user_input.clear()

    def update_ui_with_response(self, response):
        # Remove the loading GIF
        for i in reversed(range(self.layout().count())):
            item = self.layout().itemAt(i).widget()
            if isinstance(item, QLabel):
                item.deleteLater()

        # Set alignment back to normal
        self.chat_history.setAlignment(Qt.AlignLeft)

        # Update chat history with chatbot response
        self.display_message(response, is_user=False)

    def display_message(self, message, is_user=False):
        formatted_message = f"You: {message}\n" if is_user else f"BloodBot: {message}\n"
        alignment = Qt.AlignRight if is_user else Qt.AlignLeft
        self.chat_history.setAlignment(alignment)

        # Set the text color to blue in the chat history for user input
        history_palette = QPalette()
        history_palette.setColor(QPalette.Text, Qt.blue)
        self.chat_history.setPalette(history_palette)

        self.chat_history.append(formatted_message)
        self.chat_history.verticalScrollBar().setValue(self.chat_history.verticalScrollBar().maximum())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatbotUI()
    sys.exit(app.exec_())
