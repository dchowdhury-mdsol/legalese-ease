from UserPackage import User
import argparse
from SetupLogger import setup_logging

class Lawyer(User):

    """
    A class to represent a lawyer in an AI chat application.

    This class extends the User class, adding specific functionalities for lawyers,
    such as handling new query cards and reviewing AI-generated responses.

    Attributes:
    - new_query_cards (list): A list to store new query cards for the lawyer to review.

    Methods:
    - view_new_query_cards(): Displays the new query cards.
    - review_response(question, ai_response, approval_status, improved_response): Allows the lawyer to review and approve or reject AI responses.
    - add_new_query_card(query): Adds a new query card to the lawyer's list.
    """

    def __init__(self, username):

        """
        Constructor for the Lawyer class.

        Inherits from the User class and initializes the new query cards list.

        Parameters:
        - username (str): Username of the lawyer.
        """

        super().__init__(username)
        self.new_query_cards = []

    def view_new_query_cards(self):

        """
        Method to display the lawyer's new query cards.

        Iterates over the new query cards list and prints each query.
        """

        for query in self.new_query_cards:
            print(query)

    def review_response(self, question, ai_response, approval_status, improved_response=None):
        
        """
        Method for the lawyer to review and approve or reject AI-generated responses.

        Parameters:
        - question (str): The question related to the response.
        - ai_response (str): The AI-generated response to be reviewed.
        - approval_status (str): The lawyer's decision on the response ('approve' or 'reject').
        - improved_response (str, optional): The lawyer's improved response if the original is rejected.
        """

        if approval_status == "approve":
            print(f"Response to '{question}' approved. Response was: '{ai_response}'")
        elif approval_status == "reject":
            print(f"Response to '{question}' rejected. Original response was: '{ai_response}'. Improved response: {improved_response}")

    def add_new_query_card(self, query):
    
        """
        Method to add a new query card to the lawyer's list.

        Parameters:
        - query (str): The new query to be added.
        """

        self.new_query_cards.append(query)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Interact with an AI chat system as a lawyer.")
    parser.add_argument("username", type=str, help="Username of the lawyer.")
    parser.add_argument("question", type=str, help="Question to ask the AI model.")
    parser.add_argument("ai_model", type=str, help="AI model to use for generating a response.")
    parser.add_argument("approval_status", type=str, choices=["approve", "reject"], help="Approval status for the AI response.")
    parser.add_argument("--improved_response", type=str, default=None, help="Improved response provided by the lawyer.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Set up logging
    logger = setup_logging()

    # Create an instance of the Lawyer class with the provided username
    lawyer = Lawyer(args.username)

    # Simulate asking a question to the AI model
    response = lawyer.ask_question(args.question, args.ai_model)

    # Log and review the response
    logger.info("AI Response: %s", response)
    print("AI Response:", response)
    lawyer.review_response(args.question, response, args.approval_status, args.improved_response)

    # Log and optionally view the entire message history
    logger.info("Complete Message History:")
    print("\nComplete Message History:")
    lawyer.view_message_history()