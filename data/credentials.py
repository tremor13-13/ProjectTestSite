import os
from dotenv import load_dotenv
load_dotenv()



class Credentials:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

if __name__ == "__main__":
    print("LOGIN:", Credentials.LOGIN)
    print("PASSWORD:", Credentials.PASSWORD)
    print("Type of LOGIN:", type(Credentials.LOGIN))
