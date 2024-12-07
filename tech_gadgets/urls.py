from django.urls import path
from .views import start_page_view, single_gadget_int_view, GadgetView, RedirectToGadgetView, RedirectToManufacturerView, ManufacturerView, single_manufacturer_int_view




urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),

    path('<int:manufacturer_id>', RedirectToManufacturerView.as_view()),
    path('manufacturer/', ManufacturerView.as_view()),
    path('manufacturer/<int:manufacturer_id>', single_manufacturer_int_view),
    path('manufacturer/<slug:manufacturer_slug>', ManufacturerView.as_view(), name="manufacturer_slug_url")

]
