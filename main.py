import yaml
from yaml import SafeLoader

from servers import *
from servers.OpLegends import OpLegends
from servers.StarnixMC import StarnixMC
import global_variables


class Main:

    def __init__(self) -> None:
        option = webdriver.ChromeOptions()
        if global_variables.config_data['is_show_captcha'] is False:
            option.add_argument("--headless")
            option.add_argument("--no-sandbox")
            option.add_argument("--disable-dev-shm-usage")
            option.add_argument("--disable-gpu")
            option.add_argument("--window-size=1920,1080")
        option.add_experimental_option('useAutomationExtension', False)
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-blink-features=AutomationControlled")

        if 'OpLegends' in global_variables.config_data['server']:
            OpLegends(option)

        if 'StarnixMC' in global_variables.config_data['server']:
            StarnixMC(option)


if __name__ == "__main__":
    with open('config.yaml', 'r') as config:
        global_variables.config_data = dict(list(yaml.load_all(config, Loader=SafeLoader))[0])

        raw_config_server_data = {}
        for i in global_variables.config_data['server']:
            raw_config_server_data[i] = global_variables.config_data['server'][i].split(' ')

    for i in raw_config_server_data:
        global_variables.config_server_data[i] = []
        if global_variables.config_data['is_show_captcha'] is False:
            for j in raw_config_server_data[i]:
                if j[len(j)-2]+j[len(j)-1] != '.c':
                    global_variables.config_server_data[i].append(j[1:])
        else:
            for j in raw_config_server_data[i]:
                global_variables.config_server_data[i].append(j[1:])

    Main()
