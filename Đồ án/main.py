from voice_assistant import xuLy, handle_command
from config import current_language

if __name__ == '__main__':
    print("Các từ cần có trong lệnh:")
    print("xin chào                     hello")
    print("ngày mấy                     what's the date")
    print("mấy giờ                      what time is it")
    print("thoát                        stop program")
    print("mở video                     open video")
    print("thời tiết                    weather")
    print("chế độ dịch                  translation mode")
    print("thêm công việc               add task")
    print("danh sách công việc          task list")
    print("hoàn thành công việc         complete the task")
    print("xóa công việc                delete task")
    print("mở                           open")
    print("tìm kiếm                     search")
    print("wikipedia                    wikipedia")
    print("chuyển ngôn ngữ              change language")
    
    tmp = True
    while tmp:
        if current_language == "vi":
            tmp = xuLy()
        else:
            tmp = handle_command()