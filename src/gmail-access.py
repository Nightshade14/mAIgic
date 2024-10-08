"""Module for accessing Gmail using the simplegmail library."""

from datetime import datetime

from simplegmail import Gmail


class GmailAccessModule:

    """A class to handle Gmail access operations."""

    def __init__(self) -> None:
        """Initialize the GmailAccessModule."""
        self.gmail: Gmail | None = None
        self.AuthError = "Not authenticated. Call authenticate() first."

    def authenticate(self) -> None:
        """Authenticate the user and set up the Gmail connection."""
        self.gmail = Gmail()

    def get_starred_messages(self) -> None:
        """Get and print starred messages."""
        if not self.gmail:
            raise ValueError(self.AuthError)

        messages = self.gmail.get_starred_messages()
        self._print_messages(messages)

    def check_latest_emails(self, count: int = 10) -> None:
        """Check the latest emails.

        Args:
            count (int): Number of emails to retrieve. Defaults to 10.

        """
        if not self.gmail:
            raise ValueError(self.AuthError)

        messages = self.gmail.get_messages(max_results=count)
        self._print_messages(messages)

    def check_emails_after_date(
        self, start_date: datetime, max_results: int | None = None,
    ) -> None:
        """Check emails after a specific date.

        Args:
            start_date (datetime): The start date for email retrieval.
            max_results (Optional[int]): Maximum number of results to retrieve.

        """
        if not self.gmail:
            raise ValueError(self.AuthError)

        query = f"after:{start_date.strftime('%Y/%m/%d')}"
        messages = self.gmail.get_messages(query=query, max_results=max_results)
        self._print_messages(messages)

    def filter_emails_by_words(self, words: list[str]) -> None:
        """Filter emails by specific words.

        Args:
            words (list[str]): list of words to filter emails by.

        """
        if not self.gmail:
            raise ValueError(self.AuthError)

        query = " OR ".join(words)
        messages = self.gmail.get_messages(query=query)
        self._print_messages(messages)

    @staticmethod
    def _print_messages(messages: list) -> None:
        """Print message details.

        Args:
            messages (list): list of message objects to print.

        """
        for message in messages:
            print(f"To: {message.recipient}")
            print(f"From: {message.sender}")
            print(f"Subject: {message.subject}")
            print(f"Date: {message.date}")
            print(f"Preview: {message.snippet}")
            print("---")


def main() -> None:
    """Test the GmailAccessModule by fetching and printing starred emails.

    This function creates an instance of GmailAccessModule, authenticates
    the user, and then retrieves and displays the starred messages from
    the user's Gmail account.

    Note:
        This function requires proper Gmail API credentials and
        user authentication to function correctly.

    Raises:
        ValueError: If authentication fails or if there's an issue
            retrieving the starred messages.

    """
    # Create an instance of GmailAccessModule
    gmail_module = GmailAccessModule()

    # Authenticate
    gmail_module.authenticate()

    # Get and print starred messages
    print("Fetching starred messages:")
    gmail_module.get_starred_messages()


if __name__ == "__main__":
    main()
