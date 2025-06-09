from datetime import datetime
import time

class Utils:
    def __init__(self):
        pass

    def _sendail(self, mail:str, message:str) -> str:
        """
        Method used to send mails to users
        """

        time.sleep(2)
        return f"Notification sent to user {mail} on day {datetime.now()}"
