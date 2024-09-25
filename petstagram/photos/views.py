from django.shortcuts import render

def photo_add_page(request):
    return render(request, 'photos/photo-add-page.html')

def photo_detail_page(request, pk: int):
    return render(request, 'photos/photo-details-page.html')

def photo_edit_page(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')

