
import configparser
import email

config=configparser.RawConfigParser()
config.read("Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getEmail():
        password=config.get('common info','email')
        return email