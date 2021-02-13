from logging import Logger, getLogger
from datetime import datetime, timedelta
from schemas.user import UserSchema


class UserService:
    def __init__(self, db, logger: Logger = None):
        self._COLLECTION_NAME = u'users'
        self._db = db
        self._collection = self._db.collection(self._COLLECTION_NAME)
        if not logger:
            logger = getLogger("UserServiceLogger")
        self._logger = logger

    def upsertUser(self, userInputDTO: UserSchema):
        doc_ref = self._collection.document(userInputDTO.email)
        doc_ref.set(userInputDTO.dict())
        return True

    def getUser(self, email: str):
        doc_ref = self._collection.document(email)
        doc = doc_ref.get()
        return UserSchema(**doc.to_dict())

    def getUsersToProcess(self):
        docs = self._collection.where(u'nextJob', u'<', datetime.now()).stream()
        return [UserSchema(**doc.to_dict()) for doc in docs]

    def updateUser(self, updateData: UserSchema, email: str):
        doc_ref = self._collection.document(email)
        doc_ref.set(updateData.dict())
        return True