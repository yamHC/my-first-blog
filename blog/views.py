from django.shortcuts import render

# Aca importamos render, que es una funcion que nos permite renderizar una plantilla HTML

def post_list(request):
    return render(request, 'blog/post_list.html', {})  # Aca llamamos a la plantilla post_list.html