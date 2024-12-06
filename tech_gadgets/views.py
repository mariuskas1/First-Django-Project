from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, Http404

from .dummy_data import gadgets
import json
from django.utils.text import slugify
from django.urls import reverse

# Create your views here.

def start_page_view(request):
    return HttpResponse("Das hat funktioniert")

def single_gadget_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponse("not found")


def single_gadget_slug_view(request, gadget_slug):
    gadget_match = {"result": "nothing"}

    for gadget in gadgets:
        if slugify(gadget["name"])==gadget_slug:
            gadget_match = gadget

    if gadget_match:
        return JsonResponse(gadget_match)
    raise Http404

def single_gadget_post_view(request):
    if request.method == "POST":
        try: 
            data = json.loads(request.body)
            print(f"rescieved data: {data}")
            return JsonResponse({"response": "did work"})
        except:
            return JsonResponse({"response": "did not work"})
    