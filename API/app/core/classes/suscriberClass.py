from app.core.alchemy.database import Session
from app.core.alchemy.models import Suscriber, Subscription
from app.core.security import hash_password, verify_password
from app.core.classes.publisherClass import PublisherClass

class SuscriberClass:
    def __init__(self):
        self.session = Session()
        self.publisher = PublisherClass()


#--------------------------------------------------------------------------------------------------------
    def addNewSuscriber(self, name: str, email: str, password: str) -> dict:
        """
        Registers a new user if email doesn't exist. 
        Also creates one inactive subscription per topic.
        """
        try:
            # Check if user already exists
            if self.session.query(Suscriber).filter_by(email=email).first():
                return {"status": 400, "content": "User already exists"}

            # Create new subscriber
            new_user = Suscriber(
                name=name,
                email=email,
                password=hash_password(password)
            )
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)

            # Fetch topics to create subscriptions
            try:
                topics = self.publisher.getTopics()["content"]
            except Exception as e:
                self.session.rollback()
                return {
                    "status": 500,
                    "content": f"Error fetching topics: {str(e)}"
                }

            # Create one inactive subscription per topic
            subscriptions = []
            for topic in topics:
                if isinstance(topic, dict) and "topic" in topic:
                    subscriptions.append(Subscription(
                        user_email=email,
                        subscribed_topic=topic["topic"],
                        active=False
                    ))

            if subscriptions:
                self.session.add_all(subscriptions)
                self.session.commit()

            return {"status": 200,"content": "User and subscriptions created successfully"}

        except Exception as e:
            self.session.rollback()
            return {"status": 500, "content": f"Error registering user: {str(e)}"}

        finally:
            self.session.close()


#--------------------------------------------------------------------------------------------------------
    def checkCredentials(self, email: str, password: str) -> dict:
        """
        Authenticates a user based on email and password.
        """
        try:
            user = self.session.query(Suscriber).filter_by(email=email).first()

            if not user:
                return {"status": 400, "content": "User not found"}
            
            if not verify_password(password, user.password):
                return {"status": 400, "content": "Incorrect password"}

            return {"status": 200, "content": f"Welcome, {user.name}"}

        except Exception as e:
            return {"status": 500,"content": f"Error verifying credentials: {str(e)}"}

        finally:
            self.session.close()


#--------------------------------------------------------------------------------------------------------
    def activateSubscription(self, subscription_id: int) -> dict:
        """
        Activates a subscription given its ID.
        """
        try:
            sub = self.session.query(Subscription).filter_by(id=subscription_id).first()

            if not sub:
                return {"status": 404, "content": "Subscription not found"}

            sub.active = True
            self.session.commit()

            return {"status": 200,"content": f"Subscription {subscription_id} activated successfully"}

        except Exception as e:
            self.session.rollback() 
            return {"status": 500, "content": f"Error activating subscription: {str(e)}"}

        finally:
            self.session.close()


#--------------------------------------------------------------------------------------------------------
    def deactivateSubscription(self, subscription_id: int) -> dict:
        """
        Deactivates a subscription given its ID.
        """
        try:
            sub = self.session.query(Subscription).filter_by(id=subscription_id).first()

            if not sub:
                return {"status": 404, "content": "Subscription not found"}

            sub.active = False
            self.session.commit()
            return {"status": 200, "content": f"Subscription {subscription_id} deactivated successfully"}

        except Exception as e:
            self.session.rollback()
            return {"status": 500,"content": f"Error deactivating subscription: {str(e)}"}

        finally:
            self.session.close()
