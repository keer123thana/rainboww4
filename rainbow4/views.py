from django.shortcuts import render

# Create your views here.
def home(request):
    colors=["#FF0000","#FF7F00","#FFFF00","#00FF00","#0000FF","#4B0082","#9400D3"]
    return render(request,'rainbow4/index.html',{'param1':colors})