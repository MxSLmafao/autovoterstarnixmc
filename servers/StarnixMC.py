from servers import *
from servers.changeproxy import ChangeProxy


class StarnixMC:
    """Automation workflow for every StarnixMC vote endpoint."""

    def __init__(self, option,
                 mp_route="server/346812/vote/",
                 msnet_route="vote/StarnixMC/",
                 ms_org_route="server/677380",
                 topg_route="minecraft-servers/server-674622",
                 top_mc_route="vote/41289",
                 mc_servers_route="vote/5999",
                 mclist_route="server/66958-play-starnixmc-xyz-indian-based-cracked-surv/vote",
                 mcservertime_route="server-starnixmc.2736/vote") -> None:
        self.user = global_variables.config_data["username"]
        self.option = option
        self.driver = webdriver.Chrome(service=Service('./chromedriver'), options=self.option)
        self.is_proxy_change = global_variables.config_data["is_proxy_change"]

        self.mp_route = mp_route
        self.msnet_route = msnet_route
        self.ms_org_route = ms_org_route
        self.topg_route = topg_route
        self.top_mc_route = top_mc_route
        self.mc_servers_route = mc_servers_route
        self.mclist_route = mclist_route
        self.mcservertime_route = mcservertime_route

        config = global_variables.config_server_data.get('StarnixMC', [])
        if 'minecraft_mp_com.c' in config:
            self.minecraft_mp_com()
        if 'minecraft_server_net.c' in config:
            self.minecraft_server_net()
        if 'minecraftservers_org.c' in config:
            self.minecraftservers_org()
        if 'topg_org.c' in config:
            self.topg_org()
        if 'topminecraftservers_org.c' in config:
            self.topminecraftservers_org()
        if 'mc_servers_com.c' in config:
            self.mc_servers_com()
        if 'mclist_io' in config:
            self.mclist_io()
        if 'mcservertime_com.c' in config:
            self.mcservertime_com()

        self.driver_close()

    def _driver_for_vote(self):
        return ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change else self.driver

    def _store_result(self, label, message):
        global_variables.web_results.append(message)
        print(f"StarnixMC: {label}: {message}")

    def minecraft_mp_com(self):
        driver = self._driver_for_vote()
        driver.get(f"https://minecraft-mp.com/{self.mp_route}")
        text = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'nickname')))
        time.sleep(2)
        text.clear()
        text.send_keys(self.user)
        time.sleep(1)
        try:
            check_box = driver.find_element(By.ID, 'accept')
            check_box.click()
        except Exception:
            pass
        button = driver.find_element(By.ID, 'voteBtn')
        button.click()
        time.sleep(5)
        try:
            result = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#vote_form div.alert, #vote_form div.alert-success')))
            self._store_result('Minecraft-MP', result.text)
        except TimeoutException:
            self._store_result('Minecraft-MP', 'Submission sent - solve any captcha shown in the browser window.')

    def minecraft_server_net(self):
        driver = self._driver_for_vote()
        driver.get(f"https://minecraft-server.net/{self.msnet_route}")
        username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'mc_user')))
        username.clear()
        username.send_keys(self.user)
        time.sleep(1)
        try:
            star = driver.find_element(By.ID, 'rate-10')
            driver.execute_script("arguments[0].click();", star)
        except Exception:
            pass
        print("StarnixMC: minecraft-server.net requires solving the visible reCAPTCHA before submitting.")
        button = driver.find_element(By.ID, 'voteButton')
        driver.execute_script("arguments[0].click();", button)
        try:
            result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.alert, .alert-success, .alert-danger')))
            self._store_result('Minecraft-Server.net', result.text)
        except TimeoutException:
            self._store_result('Minecraft-Server.net', 'Vote submitted - confirm captcha challenge in the browser.')

    def minecraftservers_org(self):
        driver = self._driver_for_vote()
        driver.get(f'https://minecraftservers.org/{self.ms_org_route}')
        try:
            result = WebDriverWait(driver, 8).until(
                EC.presence_of_element_located((By.ID, 'error-message')))
            self._store_result('MinecraftServers.org', result.text)
            return
        except TimeoutException:
            pass
        check_box = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'checkbox')))
        check_box.click()
        time.sleep(2)
        text = driver.find_element(By.CSS_SELECTOR, '#vote-form input[type="text"]')
        text.clear()
        text.send_keys(self.user)
        time.sleep(1)
        button = driver.find_element(By.ID, 'vote-btn')
        button.click()
        try:
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'error-message')))
            self._store_result('MinecraftServers.org', result.text)
        except TimeoutException:
            self._store_result('MinecraftServers.org', 'Submission sent - finish captcha if requested.')

    def topg_org(self):
        driver = self._driver_for_vote()
        driver.get(f'https://topg.org/{self.topg_route}')
        open_modal = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'openModal')))
        driver.execute_script("arguments[0].click();", open_modal)
        username = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'game_user')))
        username.clear()
        username.send_keys(self.user)
        print("StarnixMC: topg.org uses a Cloudflare Turnstile captcha. Solve it when prompted before submitting.")
        submit = driver.find_element(By.ID, 'submit')
        submit.click()
        try:
            result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.alert, .alert-success, .alert-danger')))
            self._store_result('TopG', result.text)
        except TimeoutException:
            self._store_result('TopG', 'Vote attempted - verify captcha/Turnstile result manually.')

    def topminecraftservers_org(self):
        driver = self._driver_for_vote()
        driver.get(f'https://topminecraftservers.org/{self.top_mc_route}')
        selectors = [
            'form[action*="/vote/41289"] input[name="playername"]',
            'form[action*="/vote/41289"] input[name="username"]',
            'form[action*="/vote/41289"] input[name="ign"]',
            'form[action*="/vote/41289"] input[type="text"]',
        ]
        text_box = None
        for selector in selectors:
            try:
                text_box = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                break
            except TimeoutException:
                continue
        if text_box is None:
            self._store_result('TopMinecraftServers', 'Unable to locate the username field - complete this vote manually.')
            return
        text_box.clear()
        text_box.send_keys(self.user)
        print("StarnixMC: topminecraftservers.org is protected by Cloudflare. Complete any verification challenges in the opened tab.")
        try:
            submit = driver.find_element(By.CSS_SELECTOR, "form[action*='/vote/41289'] button[type='submit'],"
                                                 "form[action*='/vote/41289'] input[type='submit']")
            driver.execute_script("arguments[0].click();", submit)
        except Exception:
            pass
        try:
            result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.alert, .alert-success, .alert-danger')))
            self._store_result('TopMinecraftServers', result.text)
        except TimeoutException:
            self._store_result('TopMinecraftServers', 'Vote submitted - confirm success inside the browser window.')

    def mc_servers_com(self):
        driver = self._driver_for_vote()
        driver.get(f'https://mc-servers.com/{self.mc_servers_route}')
        username = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'username')))
        username.clear()
        username.send_keys(self.user)
        print("StarnixMC: mc-servers.com relies on a Turnstile captcha. Approve it before submitting the vote.")
        try:
            submit = driver.find_element(By.CSS_SELECTOR, "form button[type='submit']")
            driver.execute_script("arguments[0].click();", submit)
        except Exception:
            pass
        try:
            result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.alert, .alert-success, .alert-danger')))
            self._store_result('MC-Servers.com', result.text)
        except TimeoutException:
            self._store_result('MC-Servers.com', 'Vote submitted - wait for on-page confirmation after captcha.')

    def mclist_io(self):
        driver = self._driver_for_vote()
        driver.get(f'https://mclist.io/{self.mclist_route}')
        username = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'nickname')))
        username.clear()
        username.send_keys(self.user)
        button = driver.find_element(By.CSS_SELECTOR, 'form button[type="submit"]')
        driver.execute_script("arguments[0].click();", button)
        try:
            result = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.alert, .alert-success, .alert-danger, .notification')))
            self._store_result('MCList.io', result.text)
        except TimeoutException:
            self._store_result('MCList.io', 'Vote submitted - check the site for confirmation.')

    def mcservertime_com(self):
        driver = self._driver_for_vote()
        driver.get(f'https://mcservertime.com/{self.mcservertime_route}')
        username = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'username')))
        username.clear()
        username.send_keys(self.user)
        try:
            review_box = driver.find_element(By.NAME, 'review_text')
            review_box.clear()
            review_box.send_keys('Great community and amazing survival experience!')
        except Exception:
            pass
        print("StarnixMC: mcservertime.com includes a reCAPTCHA widget that must be solved manually.")
        try:
            submit = driver.find_element(By.CSS_SELECTOR, '#main-content button[type="submit"]')
            driver.execute_script("arguments[0].click();", submit)
        except Exception:
            pass
        try:
            result = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.ui.message, .alert, .alert-success, .alert-danger')))
            self._store_result('MCServerTime', result.text)
        except TimeoutException:
            self._store_result('MCServerTime', 'Vote submitted - confirm captcha/success message in the browser.')

    def driver_close(self) -> None:
        self.driver.close()
