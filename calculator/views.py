from django.shortcuts import render

def home(request):
    return render(request,'calculator/home.html')

def calculate(request):

    c1 = int(request.POST['c1'])
    g1 = int(request.POST['g1'])

    c2 = int(request.POST['c2'])
    g2 = int(request.POST['g2'])

    c3 = int(request.POST['c3'])
    g3 = int(request.POST['g3'])

    total_points = c1*g1 + c2*g2 + c3*g3

    total_credits = c1+c2+c3

    cgpa = round(total_points/total_credits,2)

    return render(
        request,
        'calculator/result.html',
        {'cgpa':cgpa}
    )