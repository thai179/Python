import pyttsx3
import speech_recognition as sr
import webbrowser 
from datetime import datetime 
import wikipedia
import playsound 
from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import subprocess
import psutil
import time
import json



current_language = 'vi'
now = datetime.now()
API_KEY_Wheather = 'fe0f841be9afcc9885474c401c22308b'
TODOIST_API_TOKEN = 'b9899f79698230d98f2f5b443585d4d2ec9200fe'
TODOIST_API_URL = "https://api.todoist.com/rest/v2/tasks"
def change_language(lang):
    global current_language
    if lang == 'en':
        
        current_language = lang
    else:
        
        current_language = lang
    
def speak(text):
    lang = 'en' if current_language == 'en' else 'vi'  # Xác định ngôn ngữ theo current_language
    tts = gTTS(text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)# Khởi tạo engine TTS
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        #thu âm thanh
        if current_language == 'vi':
            print("Hãy nói gì đó")
        else:
            print("Recognezi...")
        r.pause_threshold = 1
        audio_date = r.listen(source)
        #biến âm thanh thành txt
        try:
            text = r.recognize_google(audio_date,language="vi")
        except:
            return ""
    return text
def openVideo(video_name):
    # Tìm kiếm video trên YouTube
    search_url = f"https://www.youtube.com/results?search_query={video_name.replace(' ', '+')}"

    # response = requests.get(search_url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # Tìm link video đầu tiên
    webbrowser.open(search_url)
    if current_language =='vi':
        speak("Mở video "+video_name+" trên YouTube.")
    else:
        speak("open video "+video_name+" on Youtube")
    while is_chrome_running():
        time.sleep(1)

def translate_text(text,target_language='en'):
    if current_language =='vi':
        try:
            translated = GoogleTranslator(source='vi', target=target_language).translate(text)
            return translated
        except Exception as e:
                return "Không thể dịch."
    else:
        try:
            translated = GoogleTranslator(source='en', target=target_language).translate(text)
            return translated
        except Exception as e:
            return "Cannot be translated."

def translate_mode():
    while True:
        if current_language == 'vi':
            text= takeCommand().lower()
            if "thoát chế độ dịch" in text:
                speak("chế độ dịch đã thoát")
                break
            elif text=="":
                continue
            else:
                print("Đang dịch...")
                translated_text = translate_text(text, target_language='en')  # Dịch sang tiếng Anh
                print("Bản dịch:", translated_text)
                change_language('en')
                speak(translated_text)
                change_language('vi')
        else:
            text= takeCommand().lower()
            if "stop translate mode" in text:
                speak("translation mode has exited.")
                break
            elif text=="":
                continue
            else:
                print("translating...")
                translated_text = translate_text(text, target_language='vi')  # Dịch sang tiếng Việt
                print("translation:", translated_text)
                change_language('vi')
                speak(translated_text)
                change_language('en')


# city_translation = {
#     "Hà Nội": "Ha Noi",
#     "Thành phố Hồ Chí Minh": "Ho Chi Minh City",
#     "Đà Nẵng": "Da Nang","Long Xuyên":"Long Xuyen","Cần Thơ":"Can Tho"
#     # Thêm các thành phố khác nếu cần
# }

# def translate_city(city):
#     return city_translation.get(city, city)

weather_translation = {
    "clear sky": "trời quang đãng",
    "few clouds": "mây ít",
    "scattered clouds": "mây rải rác",
    "broken clouds": "mây che phủ",
    "shower rain": "mưa rào",
    "light rain": "mưa nhẹ",
    "rain": "mưa",
    "thunderstorm": "bão điện",
    "snow": "tuyết",
    "mist": "sương mù",
    # Thêm các mô tả khác nếu cần
}

def translate_weather_desc(desc):
    return weather_translation.get(desc, desc)

def get_weather(city):
    # city = translate_city(city)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_Wheather}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Trích xuất thông tin thời tiết
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        weather_VN = translate_weather_desc(weather_desc)
        
        # Tạo thông báo thời tiết
        if current_language=='vi':
            return f"Thời tiết tại {city}: {weather_VN}, nhiệt độ: {temp}°C, độ ẩm: {humidity}%."
        else:
            return f"The weather in {city}: {weather_desc}, temperature: {temp}°C, humidity: {humidity}%"
    else:
        if current_language == 'vi':
            return "Không thể lấy thông tin thời tiết. Vui lòng kiểm tra tên thành phố."
        else:
            return "Unable to retrieve weather information. Please check the city name."


def is_chrome_running():
    # Kiểm tra xem Chrome có đang chạy không
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == 'chrome.exe':  # Hoặc 'Google Chrome' tùy vào hệ điều hành
            return True
    return False

def google_search(query):
    # Tìm kiếm trên Google
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    if current_language=='vi':
        speak(f"Mở tìm kiếm Google cho: {query}")
    else:
        speak(f"Open Google and search for: {query}")
    while is_chrome_running():
        time.sleep(1)

def open_app(text):
    if text == "chrome":
        tmp=r"C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"
        process = subprocess.Popen(tmp)
        while is_chrome_running():
            time.sleep(1)
    elif text == "word":
        tmp = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD"
        process = subprocess.Popen(tmp)
        process.wait()
    elif text == "excel":
        tmp = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL"
        process = subprocess.Popen(tmp)
        process.wait()
    elif text == "java":
        tmp = r"C:\Users\ACER\eclipse\java-2023-062\eclipse\eclipse.exe"
        process = subprocess.Popen(tmp)
        process.wait()
    else:
        if current_language=='vi':
            speak("ứng dụng chưa được thêm vào")
        else:
            speak("Is it possible to use an app to uninstall?")
    
def add_task_to_todoist(task_name):
    headers = {"Authorization": f"Bearer {TODOIST_API_TOKEN}","Content-Type": "application/json"}
    
    task_data = {
        "content": task_name,  # Nội dung công việc
        "priority": 4  # Độ ưu tiên của công việc (1 đến 4, 4 là ưu tiên cao nhất)
    }
    
    response = requests.post(TODOIST_API_URL, headers=headers, data=json.dumps(task_data))
    
    if response.status_code == 200:
        speak(f"Đã thêm công việc: {task_name}")
        print(f"Task '{task_name}' added successfully!")
    else:
        speak("Có lỗi xảy ra khi thêm công việc.")
        print(f"Failed to add task: {response.status_code}")

def view_todoist_tasks():
    headers = {"Authorization": f"Bearer {TODOIST_API_TOKEN}"}
    
    response = requests.get(TODOIST_API_URL, headers=headers)
    
    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            task_list = [task['content'] for task in tasks]
            if current_language=='vi':
                task_message = "Danh sách công việc của bạn là: " + ", ".join(task_list)
            else:
                task_message = "your task list: " + ", ".join(task_list)
            print(task_message)
            speak(task_message)

        else:
            if current_language=='vi':
                speak("Không có công việc nào trong danh sách.")
            else:
                speak("No tasks in the list.")
    else:
        if current_language=='vi':
            speak("Không thể lấy danh sách công việc.")
        else:
            speak('Failed to fetch tasks')
        print(f"Failed to fetch tasks: {response.status_code}")
#lấy tasks id
def get_task_id_by_name(task_name):
    # Gửi yêu cầu GET để lấy danh sách công việc
    url = TODOIST_API_URL
    headers = {"Authorization": f"Bearer {TODOIST_API_TOKEN}","Content-Type": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tasks = response.json()  # Dữ liệu trả về là một danh sách các công việc
        if tasks:
            for task in tasks:
                task_content = task['content']
                task_id = task['id']
                
                # Kiểm tra nếu tên công việc trùng với task_name
                if task_name.lower() in task_content.lower():
                    return task_id  # Trả về task_id của công việc tìm thấy
            if current_language=='vi':
                print(f"Không tìm thấy công việc với tên '{task_name}'.")
            else:
                print(f"No task found with the name '{task_name}'.")
        else:
            if current_language=='vi':
                print("Không có công việc nào trong Todoist.")
            else:
                print("There are no tasks in Todoist.")
    else:
        if current_language=='vi':
            print(f"Không thể lấy công việc. Mã lỗi: {response.status_code} - {response.text}")
        else:
            print(f"Unable to fetch the task. Error code: {response.status_code} - {response.text}")

    return None 

def mark_task_completed(task_name):
    task_id = get_task_id_by_name(task_name)
    if task_id == None:
        return
    url = f"{TODOIST_API_URL}/{task_id}/close"
    
    headers = {"Authorization": f"Bearer {TODOIST_API_TOKEN}"}
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 204:
        if current_language=='vi':
            speak(f"Công việc {task_name} đã được đánh dấu là hoàn thành.")
        else:
            speak(f"The task {task_name} has been marked as completed.")
    else:
        if current_language=='vi':
            speak("Có lỗi xảy ra khi đánh dấu công việc là hoàn thành.")
        else:
            speak("An error occurred while marking the task as completed.")
        print(f"Failed to mark task {task_name} as completed: {response.status_code}")

# Xóa công việc khỏi Todoist
def delete_task_from_todoist(task_name):
    task_id = get_task_id_by_name(task_name)
    if task_id == None:
        return
    url = f"{TODOIST_API_URL}/{task_id}"
    
    headers = {
        "Authorization": f"Bearer {TODOIST_API_TOKEN}"
    }
    
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        if current_language=='vi':
            speak(f"Công việc {task_name} đã được xóa khỏi danh sách.")
        else:
            speak(f"The task {task_name} has been removed from the list.")

    else:
        if current_language=='vi':
            speak("Có lỗi xảy ra khi xóa công việc.")
        else:
            speak("An error occurred while deleting the task.")
        print(f"Failed to delete task {task_name}: {response.status_code}")



    
def xuLy():
    while True:
        text = takeCommand().lower()
        
        if "xin chào" in text:
            assistant = "Chào bạn tôi có thể giúp gì cho bạn?"
            speak(assistant)
            continue
        elif "ngày mấy" in text:
            assistant = now.strftime("Hôm nay là ngày: %d tháng %m năm %Y")
            speak(assistant)
            continue
        elif "mấy giờ" in text:
            assistant = now.strftime("%H:%M phút")
            speak(assistant)
            continue
        elif "thoát" in text:
            assistant = "Chương trình sẽ thoát. Tạm biệt bạn!"
            speak(assistant)
            return False
        elif "mở video" in text:
            video_name = text.replace("mở video", "").strip()
            print(text)  
            openVideo(video_name)
            continue
        elif "thời tiết" in text:
            city = text.split("thời tiết")[-1].strip()
            assistant = get_weather(city)
            speak(assistant)
        elif "chế độ dịch" in text:
            assistant = "chế độ dịch đã được bật"
            speak(assistant)
            translate_mode()
            continue
        elif "thêm công việc" in text:
            task_name = text.replace("thêm công việc", "").strip()
            add_task_to_todoist(task_name)
            continue
        elif "danh sách công việc" in text:
            view_todoist_tasks()
            continue
        elif "hoàn thành công việc" in text:
            task_id = text.replace("hoàn thành công việc", "").strip()
            mark_task_completed(task_name)
            continue
        elif "xóa công việc" in text:
            task_id = text.replace("xóa công việc", "").strip()
            delete_task_from_todoist(task_name)
            continue
        
        elif "mở" in text:
            assistant = text.replace("mở", "").strip()
            print(assistant)
            speak(assistant+" sẽ được mở")
            open_app(assistant)
            continue

        elif "tìm kiếm" in text:
            query = text.replace("tìm kiếm", "").strip()
            google_search(query)
            continue

        elif "wikipedia" in text:
            wikipedia.set_lang("vi")
            assistant = "Theo Wikipedia "+wikipedia.summary(text, sentences=1)
            print(assistant)
            speak(assistant)
            continue
        elif "chuyển ngôn ngữ" in text:
            speak(f"Ngôn ngữ đã chuyển sang tiếng Anh")
            change_language('en')
            break
        else:
            assistant = "ý bạn là gì tôi không hiểu bạn đang nói gì cả"
            speak(assistant)
    return True

def handle_command():
    while True:
        text = takeCommand().lower()

        if "hello" in text:
            assistant = "Hello, how can I help you?"
            speak(assistant)
        elif "what's the date" in text:
            assistant = now.strftime("Today's date is: %d/%m/%Y")
            speak(assistant)
        elif "what time is it" in text:
            assistant = now.strftime("It's %H:%M")
            speak(assistant)
        elif "stop program" in text:
            assistant = "The program will exit. Goodbye!"
            speak(assistant)
            return False
        elif "open video" in text:
            video_name = text.replace("open video", "").strip()
            openVideo(video_name)
        elif "weather" in text:
            city = text.split("weather")[-1].strip()
            assistant = get_weather(city)
            speak(assistant)
        elif "translation mode" in text:
            assistant = "Translation mode has been activated."
            speak(assistant)
            translate_mode()

        elif "add task" in text:
            task_name = text.replace("add task", "").strip()
            add_task_to_todoist(task_name)
            continue
        elif "task list" in text:
            view_todoist_tasks()
            continue
        elif "complete the task" in text:
            task_id = text.replace("complete the task", "").strip()
            mark_task_completed(task_name)
            continue
        elif "delete task" in text:
            task_id = text.replace("delete task", "").strip()
            delete_task_from_todoist(task_name)
            continue

        elif "open" in text:
            app_name = text.replace("open", "").strip()
            open_app(app_name)
        elif "search" in text:
            query = text.replace("search", "").strip()
            google_search(query)
        elif "wikipedia" in text:
            assistant = "According to Wikipedia " + wikipedia.summary(text, sentences=1)
            print(assistant)
            speak(assistant)
        elif "change language Vietnamese" in text:
            speak(f"The language has been changed to Vietnamese")
            change_language('vi')
            break
        else:
            assistant = "What do you mean? I don't understand."
            speak(assistant)
    return True

if __name__== '__main__':
    tmp=True
    while tmp==True:
        if current_language == "vi":
            tmp=xuLy()
        else:
            tmp=handle_command()

#todoist