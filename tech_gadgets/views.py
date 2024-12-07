from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, Http404

from .dummy_data import gadgets, manufacturers
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
from django.views.generic.base import RedirectView

# Create your views here.

def start_page_view(request):
    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})




class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"

    url=""

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwargs = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)


def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponse("not found")


def single_manufacturer_int_view(request, manufacturer_id):
    if len(manufacturers) > manufacturer_id:
        new_slug = slugify(manufacturers[manufacturer_id]["name"])
        new_url = reverse("manufacturer_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponse("not found")


class RedirectToManufacturerView(RedirectView):
    pattern_name = "manufacturer_slug_url"
    url = ""

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(manufacturers[kwargs.get("manufacturer_id", 0)]["name"])
        new_kwargs = {"manufacturer_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)



class GadgetView(View):
    def get (self, request, gadget_slug):
        gadget_match = None

        for gadget in gadgets:
            if slugify(gadget["name"])==gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404
    
    def post(self, request, gadget_slug):
        try: 
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "did work"})
        except:
            return JsonResponse({"response": "did not work"})
    


class ManufacturerView(View):
    def get(self, request, manufacturer_slug):
        manufacturer_match = None

        for manufacturer in manufacturers:
            if slugify(manufacturer["name"])==manufacturer_slug:
                manufacturer_match = manufacturer
        
        if manufacturer_match:
            return JsonResponse(manufacturer_match)
        raise Http404
    

    def post(self, request, manufacturerslug):
        try: 
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "did work"})
        except:
            return JsonResponse({"response": "did not work"})
    



def single_gadget_view(request, gadget_slug):
    
    if request.method == "GET":
        gadget_match = None

        for gadget in gadgets:
            if slugify(gadget["name"])==gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404


    if request.method == "POST":
            try: 
                data = json.loads(request.body)
                print(f"rescieved data: {data}")
                return JsonResponse({"response": "did work"})
            except:
                return JsonResponse({"response": "did not work"})



def single_gadget_post_view(request):
    if request.method == "POST":
        try: 
            data = json.loads(request.body)
            print(f"rescieved data: {data}")
            return JsonResponse({"response": "did work"})
        except:
            return JsonResponse({"response": "did not work"})
    