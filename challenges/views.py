from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect # this is class

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

def monthly_challenge_by_number(request , month):
    months = list(monthly_challenges.keys()) # gives list of dictinary keys 
    try:
        months_values = months[month-1] # to avoid starting index 0 means 1 is january not february
        return HttpResponseRedirect("/challenges/" + months_values) # this will redirect to given dictonary values
    except:
        return HttpResponseNotFound("Invalid Month number ")


# above is too old fashion to have lot of if and else statements , below we will do it more dynamically


def monthly_challenge(request , month):
    try:
        challenges_text = monthly_challenges[month]
        return HttpResponse(challenges_text)
    except:    
        return HttpResponseNotFound("Error = number not found")
    