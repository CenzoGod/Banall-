import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "28255147"))
    API_HASH = os.getenv("API_HASH", "8113960fe67c0cc815e6acce2aefb410")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7382235042:AAFv5nrAHJEnq3cuJUOTCGLKYdVDeIaYZnE")
    sudo = os.getenv("6663845789 6698364560")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
