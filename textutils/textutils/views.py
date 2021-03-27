"""Created by me
"""
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render



__author__ = "Nishant Baheti"


def home(request):
    return render(request,'home.html')

def remove_punc(request):
    form_text = request.GET.get("text","default")
    print(form_text)
    return HttpResponse("Remove punctuation")

def analyzer(request):

    form_text = request.GET.get("text","default")
    form_remove_punc = request.GET.get("removepunc","off")
    form_cap_first = request.GET.get("capitalizefirst", "off")
    form_new_line_rm = request.GET.get("newlineremove", "off")
    form_space_rm = request.GET.get("spaceremove", "off")
    form_char_count = request.GET.get("charcount", "off")
    print(form_text,form_remove_punc)

    purpose = ""

    if form_remove_punc == "on":
        punctuations = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        new_string = ""

        for c in form_text:
            if c not in punctuations:
                new_string += c
        form_text = new_string
        purpose += "| Removed Punctuations "

    if form_cap_first == "on":
        
        form_text = form_text.capitalize()

        purpose += "| Capitalize First "

    if form_new_line_rm == "on":

        new_string = ""

        for c in form_text:
            if c != "\n":
                new_string += c
        form_text = new_string
        purpose += "| Remove New Line "

    if form_space_rm == "on":
        form_text = form_text.strip()
        purpose += "| Remove Space "

    if form_char_count == "on":
        form_text = len(form_text)
        purpose += "| Character Count "   
    
    params = {
        "purpose" : purpose,
        "analyzed_text" : form_text
    }
    return render(request, "analyze.html",params)
