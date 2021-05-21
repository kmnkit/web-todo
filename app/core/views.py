from django.shortcuts import render


def resolve_home(self, request):
    print("홈")
    return render(request, "home.html")
