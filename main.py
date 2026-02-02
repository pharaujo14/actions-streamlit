from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# Lista de URLs digitadas diretamente no código
STREAMLIT_URLS = [
    "https://centurydata.streamlit.app/",
    "https://dashboard-dsr.streamlit.app/",
    "https://joy-force-system.streamlit.app/"
]

def main():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        for url in STREAMLIT_URLS:
            print(f"\nAbrindo {url}")
            driver.get(url)

            wait = WebDriverWait(driver, 15)
            try:
                button = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(text(),'Yes, get this app back up')]")
                    )
                )
                print("Wake-up button encontrado. Clicando...")
                button.click()

                wait.until(
                    EC.invisibility_of_element_located(
                        (By.XPATH, "//button[contains(text(),'Yes, get this app back up')]")
                    )
                )
                print("App acordado ✅")

            except TimeoutException:
                print("Nenhum botão encontrado. App já estava ativo ✅")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        exit(1)
    finally:
        driver.quit()
        print("\nScript finalizado.")

if __name__ == "__main__":
    main()
