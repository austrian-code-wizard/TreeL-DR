from logging import Logger, getLogger
from datetime import datetime, timedelta
from schemas.user import UserSchema
from utils import remove_none_from_dict


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
        doc_ref.set(remove_none_from_dict(userInputDTO.dict()))
        return True

    def getUser(self, email: str):
        doc_ref = self._collection.document(email)
        doc = doc_ref.get()
        return UserSchema(**doc.to_dict())

    def getUsersToProcess(self):
        docs = self._collection.where(u'nextJob', u'<', datetime.utcnow()).stream()
        return [UserSchema(**doc.to_dict()) for doc in docs]

    def updateUser(self, updateData: UserSchema, email: str):
        doc_ref = self._collection.document(email)
        doc_ref.update(remove_none_from_dict(updateData.dict()))
        return True