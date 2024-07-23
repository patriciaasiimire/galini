# disorders/views.py
from django.shortcuts import render, get_object_or_404
from .models import MentalDisorder


def disorder_list(request):
    disorders = MentalDisorder.objects.all()
    return render(
        request, "mentalDisorders/disorder_list.html", {"disorders": disorders}
    )


def disorder_detail(request, pk):
    disorder = get_object_or_404(MentalDisorder, pk=pk)
    return render(
        request, "mentalDisorders/disorder_detail.html", {"disorder": disorder}
    )
