from app.core.alchemy.database import Session
from app.core.alchemy.models import Topic, Subscription, Suscriber
from app.core.utils.sendMailsNotifications import Utils

class PublisherClass:
    def __init__(self):
        self.session = Session()
        self.utils = Utils()

    # ----------------------------------------------------------
    def getTopics(self) -> dict:
        """
        Returns a list of all topics available in the system.
        """
        try:
            topics = self.session.query(Topic).all()
            result = [{"id": t.id, "topic": t.topics} for t in topics]
            return {"status": 200, "content": result}
        
        except Exception as e:
            return {"status": 400, "content": f"ERROR - {e}"}
        
        finally:
            self.session.close()


    # ----------------------------------------------------------
    def _getTopicsList(self) -> list[str]:
        """
        Returns a list of all topics available in the system to use in others methods.
        """
        try:
            topicsList = []
            topics = self.session.query(Topic).all()
            for topic in topics:
                topicsList.append(topic.topics)

            return topicsList
        
        except Exception as e:
            return {"status": 400, "content": f"ERROR - {e}"}
        
        finally:
            self.session.close()
    # ----------------------------------------------------------
    def getUsersInfo(self) -> dict:
        """
        Returns all registered users with their basic information.
        """
        try:
            users = self.session.query(Suscriber).all()
            result = [{
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "created_at": user.created_at.isoformat()
            } for user in users]
            return {"status": 200, "content": result}
        
        except Exception as e:
            return {"status": 400, "content": f"ERROR - {e}"}
        
        finally:
            self.session.close()

# ----------------------------------------------------------
    def _getUsersMailList(self) -> dict:
        """
        Returns a list woth all emails of registered users.
        """
        try:
            users = self.session.query(Suscriber).all()
            result = [user.email for user in users]
            return {"status": 200, "content": result}
        
        except Exception as e:
            return {"status": 400, "content": f"ERROR - {e}"}
        
        finally:
            self.session.close()
    # ----------------------------------------------------------
    def getUsersInfoSuscribedToAtopic(self, topic: str) -> dict:
        """
        Returns all users subscribed to a specific topic (and active).
        """
        try:

            tocipsAvailables = self._getTopicsList()
            if topic not in tocipsAvailables:
                return {"status": 400, "content": f"ERROR - '{topic}' does not exist in our Topics. List of available {tocipsAvailables} topics."}

            users = (
                self.session.query(Suscriber)
                .join(Subscription, Suscriber.email == Subscription.user_email)
                .filter(Subscription.subscribed_topic == topic, Subscription.active == True)
                .all()
            )
            result = [{
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "created_at": user.created_at.isoformat()
            } for user in users]
            return {"status": 200, "content": result}
        
        except Exception as e:
            return {"status": 400, "content": f"ERROR - {e}"}
        
        finally:
            self.session.close()

    # ----------------------------------------------------------
    def getUserSuscriptions(self, email: str) -> dict:
        """
        Returns all topic subscriptions for a given user email.
        """
        try:
            mailList = self._getUsersMail()
            if email not in mailList:
                return {"status": 500, "content": f"The mail '{email}' is not in our databases. Please check it."}
            
            subscriptions = self.session.query(Subscription).filter_by(user_email=email).all()
            if not subscriptions:
                return {"status": 404, "content": f"No subscriptions found for {email}"}

            result = [{
                "id": subscription.id,
                "user_email": subscription.user_email,
                "subscribed_topic": subscription.subscribed_topic,
                "active": subscription.active,
                "created_at": subscription.created_at.isoformat() if subscription.created_at else None,
                "updated_at": subscription.updated_at.isoformat() if subscription.updated_at else None
            } for subscription in subscriptions]

            return {"status": 200, "content": result}
        
        except Exception as e:
            return {"status": 500, "content": f"Error when obtaining subscriptions: {str(e)}"}
        
        finally:
            self.session.close()

    # ----------------------------------------------------------
    def _getUsersMail(self) -> list[str]:
        """
        Returns a list of distinct emails from all subscriptions.
        """
        try:
            rows = self.session.query(Subscription.user_email).distinct().all()
            return [r[0] for r in rows]
        
        except Exception as e:
            raise Exception(f"Error when obtaining subscribers: {str(e)}")
        
        finally:
            self.session.close()

    # ----------------------------------------------------------
    def sendNotificationToAllSuscribers(self, message: str) -> dict:
        """
        Sends a notification email to all subscribed users.
        """
        try:
            users = self._getUsersMail()

            for email in users:
                self.utils._sendail(mail=email, message=message)
                print(f"Sent to {email}")

            return {"status": 200, "content": {"Users": users, "Message": message}}
        
        except Exception as e:
            return {"status": 500, "content": f"Error in the process: {str(e)}"}

    # ----------------------------------------------------------
    def _getUsersSubscribedToAtopic(self, topic: str) -> list[str]:
        """
        Returns a list of emails of users subscribed to a given topic (active only).
        """
        try:
            rows = (
                self.session.query(Subscription.user_email)
                .filter(Subscription.subscribed_topic == topic, Subscription.active == True)
                .distinct()
                .all()
            )
            return [r[0] for r in rows]
        
        except Exception as e:
            raise Exception(f"Error when obtaining topic subscribers: {str(e)}")
        finally:
            self.session.close()

    # ----------------------------------------------------------
    def sendNotificationToUsersSuscribedToATopic(self, topic: str) -> dict:
        """
        Sends a notification email to users subscribed to a specific topic.
        """
        try:
            users = self._getUsersSubscribedToAtopic(topic)
            message = f"We have added a new article in the topic: {topic}"

            for email in users:
                self.utils._sendail(mail=email, message=message)
                print(f"Sent to {email}")

            return {"status": 200, "content": {"topic": topic, "users": users, "message": message}}
        
        except Exception as e:
            return {"status": 500, "content": f"Error in the process: {str(e)}"}
