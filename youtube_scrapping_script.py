from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
channel_name=str(input("Please enter the name of the channel :"))
driver=webdriver.Firefox(service=Service(executable_path="./geckodriver"))
driver.implicitly_wait(10)
def main():
    driver.get(f"https://www.youtube.com/results?search_query={channel_name}")
    driver.implicitly_wait(10)
    video_count=driver.find_element(By.CSS_SELECTOR,"span[id='video-count']").text
    # getting the main link of the channel
    main_link=driver.find_element(By.CSS_SELECTOR,"a[id='main-link']").get_attribute('href')
    print("Channel main link : "+main_link)
    main_channel_details(main_link,video_count)
    # quit all of the tabs
    driver.quit()

def main_channel_details(main_link,video_count):
    driver.get(main_link+"/about")
    driver.implicitly_wait(10)
    # getting the name of the channel
    official_name=driver.find_element(By.CSS_SELECTOR,"yt-formatted-string[id='text']").text
    print("Channel Name : "+official_name)
    #printing the video count
    print("The total number of videos posted : "+video_count)
    # getting the subscriber count of the channel
    sub_count=driver.find_element(By.XPATH,"//*[@id='subscriber-count']").text
    print("Subscribers count : "+sub_count)
    # getting the logo of the channel
    #open file in write and binary mode
    with open('Logo.png', 'wb') as file:
    #identify image to be captured
       l = driver.find_element(By.CSS_SELECTOR,"img[id='img']")
    #write file
       file.write(l.screenshot_as_png)
    


if __name__=="__main__":
    main()

