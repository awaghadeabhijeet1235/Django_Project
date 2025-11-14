from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect # this is class
from django.urls import reverse
from django.template.loader import render_to_string # will be used to convert HTml code into string
# Create your views here.

"""
def january(request):
    return HttpResponse("This Works for january!")

def february(request):
    return HttpResponse("This Works for february!")

def march(request):
    return HttpResponse("This Works for march!")

def april(request):
    return HttpResponse("This Works for april!")
"""
#we dont need above explicit functions, below we have done it dynamically
'''
def monthly_challenge(request , month): # this month is exact keyword used in url.py
    text = None;
    if month == "january":# or month == '1': # if 1 is string
        text = "This is Janaury"
    elif month == "february":
        text = "This is february"
    elif month == "march":
        text = "This is March"
    elif month == "april":
        text = "This is April"
    elif month == "may":
        text = "This is May"
    elif month == "june":
        text = "This is June"
    elif month == "july":
        text = "This is July"
    elif month == "august":
        text = "This is August"
    elif month == "september":
        text = "This is September"
    elif month == "october":
        text = "This is October"
    elif month == "november":
        text = "This is November"
    elif month == "december":
        text = "This is December"
    else:
        return HttpResponseNotFound("Error = This is something else month")
    return HttpResponse(text)
'''

monthly_challenges = {
    "january": "This is January",
    "february": "This is February",
    "march": "This is March",
    "april": "This is April",
    "may": "This is May",
    "june": "This is June",
    "july": "This is July",
    "august": "This is August",
    "september": "This is September",
    "october": "This is October",
    "november": "This is November",
    "december": "This is December"
}
    
def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize() #first letter to make it capital
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>" #\is used to allow next word, double quotes we can not used it twice  
    # this for loop will create list items side by side
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request , month):
    months = list(monthly_challenges.keys()) # gives list of dictinary keys 
    try:
        months_values = months[month-1] # to avoid starting index 0 means 1 is january not february
        redirect_path = reverse("month-challenge", args=[months_values]) # it will build the path like /challenge/january
        #return HttpResponseRedirect("/challenge/" + months_values) # this will redirect to given dictonary values
        return HttpResponseRedirect(redirect_path) #used for redirecting to another url, basically avoids hard coding the url path as above
    except:
        return HttpResponseNotFound("Invalid Month number ")


# above is too old fashion to have lot of if and else statements , below we will do it more dynamically


def monthly_challenge(request , month):
    try:
        challenges_text = monthly_challenges[month]
        #response_data = f"<h1>{challenges_text}</h1>" #html header
        response_data = render_to_string("challenges/challenge.html") #converts entire html file into string to pass to httpresponse
        return HttpResponse(response_data)
    except:    
        return HttpResponseNotFound("<h1>Error = number not found</h1>")
    