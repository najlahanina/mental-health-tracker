from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306240055',
        'name': 'Nisa Najla Hanina Hasanah',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
