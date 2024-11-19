from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def init_browser():
    """Инициализация браузера Chrome и переход на Википедию."""
    driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    driver.get("https://ru.wikipedia.org/")
    return driver

def search_article(driver, query):
    """Поиск статьи на Википедии."""
    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

def list_paragraphs(driver):
    """Вывод параграфов текущей статьи."""
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    for i, p in enumerate(paragraphs, start=1):
        if p.text.strip():
            print(f"\nПараграф {i}:\n{p.text}")
            cont = input("Нажмите Enter для следующего параграфа или 'q' для выхода: ").strip()
            if cont.lower() == "q":
                break

def navigate_to_link(driver):
    """Перейти на одну из связанных страниц."""
    links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    for i, link in enumerate(links, start=1):
        if link.text.strip():
            print(f"{i}: {link.text}")
    choice = input("Введите номер ссылки для перехода или '0' для отмены: ").strip()
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(links):
            links[choice - 1].click()
            time.sleep(2)
        else:
            print("Неверный выбор.")
    else:
        print("Возвращаемся к текущей статье.")

def main():
    """Основной цикл программы."""
    driver = init_browser()
    try:
        while True:
            query = input("Введите запрос для поиска на Википедии (или 'exit' для выхода): ").strip()
            if query.lower() == "exit":
                print("Программа завершена.")
                break
            search_article(driver, query)
            while True:
                print("\nЧто вы хотите сделать?")
                print("1. Листать параграфы текущей статьи.")
                print("2. Перейти на одну из связанных страниц.")
                print("3. Вернуться к главному меню.")
                choice = input("Ваш выбор: ").strip()
                if choice == "1":
                    list_paragraphs(driver)
                elif choice == "2":
                    navigate_to_link(driver)
                elif choice == "3":
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()



