from django.shortcuts import HttpResponse

def home_page(request):
    html_response = """
        <style>
        h1 {
            color: #fff;
            background-color: blue;
        }
        </style>
        <h1>Blog site</h1>
    """
    return HttpResponse(html_response)
