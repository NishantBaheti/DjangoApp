"""Created by me
"""
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render



__author__ = "Nishant Baheti"


def home(request):
    return render(request,'home.html')

def analyzer(request):

    form_text = request.POST.get("text","default")
    form_remove_punc = request.POST.get("removepunc", "off")
    form_cap_first = request.POST.get("capitalizefirst", "off")
    form_new_line_rm = request.POST.get("newlineremove", "off")
    form_space_rm = request.POST.get("spaceremove", "off")
    form_char_count = request.POST.get("charcount", "off")
    # print(form_text,form_remove_punc)

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
        form_text = form_text.replace("\n","").replace("\r","")
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
