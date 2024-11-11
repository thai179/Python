import os
import time
import requests
import wikipedia
import playsound
from gtts import gTTS
from datetime import datetime
from deep_translator import GoogleTranslator
import subprocess
import psutil
from config import current_language, API_KEY_Wheather
import speech_recognition as sr
import webbrowser
from todoist import *

now = datetime.now()


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
        print(text)

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
        elif "change language" in text:
            speak(f"The language has been changed to Vietnamese")
            change_language('vi')
            break
        else:
            assistant = "What do you mean? I don't understand."
            speak(assistant)
    return True
