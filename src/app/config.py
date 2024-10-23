import configparser
import os

config = configparser.ConfigParser()


def init_config(path):
    config.optionxform = str
    config.read(path)
