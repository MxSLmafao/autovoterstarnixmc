from servers import *
from servers.changeproxy import ChangeProxy


class StarnixMC:
    def __init__(self, option, mmp_server="server/346812/vote/",
                 msn_server="details/StarnixMC/", ms_server="server/677380",
                 topg_server="server-674622", tms_server="vote/41289",
                 mcs_server="vote/5999", mcl_server="66958-play-starnixmc-xyz-indian-based-cracked-surv/vote",
                 mcst_server="server-starnixmc.2736/vote") -> None:
        self.user = global_variables.config_data["username"]
        self.option = option
        self.driver = uc.Chrome(options=self.option, use_subprocess=False)
        self.is_proxy_change = global_variables.config_data["is_proxy_change"]

        self.mmp_server = mmp_server
        self.msn_server = msn_server
        self.ms_server = ms_server
        self.topg_server = topg_server
        self.tms_server = tms_server
        self.mcs_server = mcs_server
        self.mcl_server = mcl_server
        self.mcst_server = mcst_server

        if 'minecraft_mp_com' in global_variables.config_server_data['StarnixMC']:
            self.minecraft_mp_com()

        if 'minecraft_server_net' in global_variables.config_server_data['StarnixMC']:
            self.minecraft_server_net()

        if 'minecraftservers_org' in global_variables.config_server_data['StarnixMC']:
            self.minecraftservers_org()

        if 'topg_org' in global_variables.config_server_data['StarnixMC']:
            self.topg_org()

        if 'topminecraftservers_org' in global_variables.config_server_data['StarnixMC']:
            self.topminecraftservers_org()

        if 'mc_servers_com' in global_variables.config_server_data['StarnixMC']:
            self.mc_servers_com()

        if 'mclist_io' in global_variables.config_server_data['StarnixMC']:
            self.mclist_io()

        if 'mcservertime_com' in global_variables.config_server_data['StarnixMC']:
            self.mcservertime_com()

        self.driver_close()

    def minecraft_mp_com(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get("https://minecraft-mp.com/" + self.mmp_server)
        text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'nickname')))
        time.sleep(2)
        text.send_keys(self.user)
        time.sleep(1)
        check_box = driver.find_element(By.XPATH, '//*[@id="accept"]')
        check_box.click()
        time.sleep(1)
        button = driver.find_element(By.XPATH, '//*[@id="voteBtn"]')
        button.click()
        time.sleep(2)
        if EC.presence_of_element_located((By.XPATH, '/html/body/div')):
            print("StarnixMC: Minecraft MP: Captcha arise!! Solve it!!")
            time.sleep(10)
        time.sleep(5)
        try:
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="vote_form"]/div[1]')))
            global_variables.web_results.append(result.text)
        except Exception:
            result = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/p[1]/strong')))
            global_variables.web_results.append(result.text)
        print("StarnixMC: Minecraft MP:", global_variables.web_results[-1])

    def minecraft_server_net(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get('https://minecraft-server.net/' + self.msn_server)
        try:
            # Wait for vote button
            vote_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "vote") or contains(text(), "Vote")]')))
            time.sleep(2)
            vote_button.click()
            time.sleep(2)
            # Enter username
            text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            text.send_keys(self.user)
            time.sleep(1)
            # Submit vote
            submit_button = driver.find_element(By.XPATH, '//button[@type="submit"] | //input[@type="submit"]')
            submit_button.click()
            time.sleep(5)
            # Get result
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "message") or contains(@class, "alert")]')))
            global_variables.web_results.append(result.text)
            print("StarnixMC: Minecraft Server Net:", global_variables.web_results[-1])
        except Exception as e:
            print(f"StarnixMC: Minecraft Server Net: Error - {str(e)}")

    def minecraftservers_org(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get('https://minecraftservers.org/' + self.ms_server)
        try:
            result = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="error-message"]')))
            print("StarnixMC: Minecraft servers:", result.text)
        except Exception:
            check_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="checkbox"]')))
            time.sleep(3)
            check_box.click()
            time.sleep(2)
            text = driver.find_element(By.XPATH, '//*[@id="vote-form"]/ul/li/input')
            text.send_keys(self.user)
            time.sleep(1)
            button = driver.find_element(By.XPATH, '//*[@id="vote-btn"]')
            button.click()
            result = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="error-message"]')))
            print("StarnixMC: Minecraft servers:", result.text)

    def topg_org(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get('https://topg.org/minecraft-servers/' + self.topg_server)
        try:
            # Click vote button
            vote_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "vote") or contains(text(), "Vote")]')))
            time.sleep(2)
            vote_button.click()
            time.sleep(2)
            # Enter username
            text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'ign')))
            text.send_keys(self.user)
            time.sleep(1)
            # Submit
            submit_button = driver.find_element(By.XPATH, '//button[@type="submit"] | //input[@type="submit"]')
            submit_button.click()
            time.sleep(5)
            # Get result
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "message") or contains(@class, "success") or contains(@class, "error")]')))
            global_variables.web_results.append(result.text)
            print("StarnixMC: TopG:", global_variables.web_results[-1])
        except Exception as e:
            print(f"StarnixMC: TopG: Error - {str(e)}")

    def topminecraftservers_org(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get('https://topminecraftservers.org/' + self.tms_server)
        try:
            # Enter username
            text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            time.sleep(2)
            text.send_keys(self.user)
            time.sleep(1)
            # Submit vote
            button = driver.find_element(By.XPATH, '//button[contains(text(), "Vote")] | //input[@value="Vote"]')
            button.click()
            time.sleep(5)
            # Get result
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "message") or contains(@class, "alert")]')))
            global_variables.web_results.append(result.text)
            print("StarnixMC: Top Minecraft Servers:", global_variables.web_results[-1])
        except Exception as e:
            print(f"StarnixMC: Top Minecraft Servers: Error - {str(e)}")

    def mc_servers_com(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get('https://mc-servers.com/' + self.mcs_server)
        try:
            # Enter username
            text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            time.sleep(2)
            text.send_keys(self.user)
            time.sleep(1)
            # Click vote button
            button = driver.find_element(By.XPATH, '//button[contains(text(), "Vote")] | //input[@type="submit"]')
            button.click()
            time.sleep(5)
            # Get result
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "message") or contains(@class, "alert")]')))
            global_variables.web_results.append(result.text)
            print("StarnixMC: MC Servers:", global_variables.web_results[-1])
        except Exception as e:
            print(f"StarnixMC: MC Servers: Error - {str(e)}")

    def mclist_io(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get('https://mclist.io/server/' + self.mcl_server)
        try:
            # Enter username
            text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            time.sleep(2)
            text.send_keys(self.user)
            time.sleep(1)
            # Submit vote
            button = driver.find_element(By.XPATH, '//button[contains(text(), "Vote")] | //button[@type="submit"]')
            button.click()
            time.sleep(5)
            # Get result
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "message") or contains(@class, "alert") or contains(@class, "success")]')))
            global_variables.web_results.append(result.text)
            print("StarnixMC: MCList.io:", global_variables.web_results[-1])
        except Exception as e:
            print(f"StarnixMC: MCList.io: Error - {str(e)}")

    def mcservertime_com(self):
        driver = ChangeProxy.change_proxy(option=self.option) if self.is_proxy_change is True else self.driver
        driver.get('https://mcservertime.com/' + self.mcst_server)
        try:
            # Enter username
            text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            time.sleep(2)
            text.send_keys(self.user)
            time.sleep(1)
            # Submit vote
            button = driver.find_element(By.XPATH, '//button[contains(text(), "Vote")] | //input[@type="submit"]')
            button.click()
            time.sleep(5)
            # Get result
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "message") or contains(@class, "alert")]')))
            global_variables.web_results.append(result.text)
            print("StarnixMC: MC Server Time:", global_variables.web_results[-1])
        except Exception as e:
            print(f"StarnixMC: MC Server Time: Error - {str(e)}")

    def driver_close(self) -> None:
        self.driver.close()
