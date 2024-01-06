from passlib.context import CryptContext
pdw_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(password: str):
    return pdw_context.hash(password)

def verify(plaid_password, hashed_password):
    return pdw_context.verify(plaid_password, hashed_password)