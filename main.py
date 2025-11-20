import yaml
from yaml import SafeLoader

from servers import *
from servers.StarnixMC import StarnixMC
import global_variables


class Main:

    def __init__(self) -> None:
        option = webdriver.ChromeOptions()
        if global_variables.config_data['is_show_captcha'] is False:
            option.add_argument("headless")
        option.add_experimental_option('useAutomationExtension', False)

        if 'StarnixMC' in global_variables.config_data['server']:
            StarnixMC(option)


if __name__ == "__main__":
    with open('config.yaml', 'r') as config:
        global_variables.config_data = dict(list(yaml.load_all(config, Loader=SafeLoader))[0])

        raw_config_server_data = {}
        for i in global_variables.config_data['server']:
            raw_value = global_variables.config_data['server'][i]
            if isinstance(raw_value, list):
                raw_config_server_data[i] = raw_value
            else:
                raw_config_server_data[i] = str(raw_value).split(' ')

    for i in raw_config_server_data:
        global_variables.config_server_data[i] = []
        for j in raw_config_server_data[i]:
            server_key = j.lstrip('-')
            if global_variables.config_data['is_show_captcha'] is False and server_key.endswith('.c'):
                continue
            global_variables.config_server_data[i].append(server_key)

    Main()
