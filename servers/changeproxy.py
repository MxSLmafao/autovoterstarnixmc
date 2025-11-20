from servers import *
from servers.SSLproxies import NewProxy


class ChangeProxy:
    @staticmethod
    def change_proxy(option):
        driver = uc.Chrome(options=option, use_subprocess=False)
        proxy = NewProxy.proxy(driver=driver)
        print(proxy)
        option.add_argument(f'--proxy-server={proxy}')
        driver = uc.Chrome(options=option, use_subprocess=False)
        return driver
