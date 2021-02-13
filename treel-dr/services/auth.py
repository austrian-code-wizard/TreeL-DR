import msal
from logging import Logger, getLogger
from config import CLIENT_ID, CLIENT_SECRET, AUTHORITY, REDIRECT_PATH, APP_URL, SCOPE

class AuthService:
    def __init__(self, session, logger: Logger = None):
        self._session = session
        self._TOKEN_CACHE = "token_cache"
        if not logger:
            logger = getLogger("AuthServiceLogger")

    def load_cache(self):
        cache = msal.SerializableTokenCache()
        if self._session.get(self._TOKEN_CACHE):
            cache.deserialize(self._session[self._TOKEN_CACHE])
        return cache

    def loads_cache(self, serialized_cache):
        cache = msal.SerializableTokenCache()
        cache.deserialize(serialized_cache)
        self.save_cache(cache)
        return cache

    def save_cache(self, cache):
        if cache.has_state_changed:
            self._session[self._TOKEN_CACHE] = cache.serialize()

    def dumps_cache(self ,cache):
        return cache.serialize()

    def build_msal_app(self, cache=None, authority=None):
        return msal.ConfidentialClientApplication(
            CLIENT_ID, authority=AUTHORITY,
            client_credential=CLIENT_SECRET, token_cache=cache)

    def build_auth_code_flow(self, authority=None):
        #url = url_for("authorized", _external=True)
        msal_app = self.build_msal_app(authority=authority).initiate_auth_code_flow(
            SCOPE, redirect_uri=f"{APP_URL}{REDIRECT_PATH}")
        self._session["flow"] = msal_app
        return self._session["flow"]["auth_uri"]


    def get_token_from_cache(self):
        cache = self.load_cache()  # This web app maintains one cache per session
        cca = self.build_msal_app(cache=cache)
        accounts = cca.get_accounts()
        if accounts:  # So all account(s) belong to the current signed-in user
            result = cca.acquire_token_silent(SCOPE, account=accounts[0])
            self.save_cache(cache)
            return result

    def get_access_token(self, new_token): 
        cache = self.load_cache()
        result = self.build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            self._session.get("flow", {}), new_token)
        self._session["user"] = result.get("id_token_claims")
        self.save_cache(cache)
        token = self.get_token_from_cache()
        return token['access_token']

    def get_access_token_from_serialized(self, serialized_token):
        cache = self.loads_cache(serialized_token)  # This web app maintains one cache per session
        cca = self.build_msal_app(cache=cache)
        accounts = cca.get_accounts()
        if accounts:  # So all account(s) belong to the current signed-in user
            result = cca.acquire_token_silent(SCOPE, account=accounts[0])
            self.save_cache(cache)
            return result['access_token']