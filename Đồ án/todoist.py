import requests
import json
from config import TODOIST_API_TOKEN, TODOIST_API_URL, current_language
from voice_assistant import speak



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