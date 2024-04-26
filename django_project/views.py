import requests
from django.shortcuts import render
from django.http import JsonResponse
import random
from django.conf import settings

def index(request):
    return render(request, 'index.html')

#API for random uselessfacts
def get_random_fact(request):
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = response.json()
    fact = data["text"]
    return JsonResponse({"fact": fact})


# API to ranomize the students
def get_random_student(request):
    response = requests.get("https://freetestapi.com/api/v1/students")
    students = response.json()
    random_student = random.choice(students)

    student_name = random_student["name"]
    student_age = random_student["age"]
    gender = random_student["gender"]
    address = random_student["address"]
    email = random_student["email"]
    phone = random_student["phone"]
    course = random_student["courses"]
    gpa = random_student["gpa"]

    formatted_address = f"{address.get('street', '')},  {address.get('country', '')}"
    if gender == "Male":
        avatar_image = settings.STATIC_URL + "images/male_avatar.jpg"
    else:
        avatar_image = settings.STATIC_URL + "images/female_avatar.jpg"

    return JsonResponse(
        {
            "student_name": student_name,
            "student_age": student_age,
            "gender": gender,
            "address": formatted_address,
            "email": email,
            "phone": phone,
            "course": course,
            "gpa": gpa,
            "avatar_image": avatar_image,
        }
    )

#Dog API
def get_random_dog(request):
    r3 = requests.get("https://dog.ceo/api/breeds/image/random")
    res3 = r3.json()
    dog = res3["message"]
    return JsonResponse({"dog": dog})


def get_random_dog_by_breed(request, breed):
    if breed:
        r = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    else:
        r = requests.get("https://dog.ceo/api/breeds/image/random")
    res = r.json()
    dog = res["message"]
    return JsonResponse({"dog": dog})


def get_random_dog_by_sub_breed(request, breed, sub_breed):
    if breed and sub_breed:
        r = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
    else:
        r = requests.get(f"https://dog.ceo/api/breeds/image/random")
    res = r.json()
    dog = res["message"]
    return JsonResponse({"dog": dog})
