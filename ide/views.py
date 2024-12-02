import subprocess
import sys
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .converter import process_code, convert_to_malayalam
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "ide/home.html")

def intro(request):
    return render(request, "ide/intro.html")

def keywords(request):
    return render(request, "ide/keywords.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")  # Corrected variable name

        if password != repassword:
            return render(request, "ide/register.html", {"error": "Passwords do not match."})

        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            # Automatically log the user in after registration
            login(request, user)
            return redirect("ide")  # Redirect to the IDE page
        except Exception as e:
            return render(request, "ide/register.html", {"error": str(e)})

    return render(request, "ide/register.html")

def user_login(request):
    if request.method == "POST":
        name = request.POST.get("name")  # Corrected variable name
        password = request.POST.get("password")

        user = authenticate(username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect("ide")  # Redirect to the IDE page
        else:
            return render(request, "ide/register.html", {"error": "You are not registered."})

    return render(request, "ide/login.html")

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required
def ide(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "ide/index.html")

@login_required
def run_code(request):
    """
    Process Malayalam code, translate it to Python, execute it, and return the output.
    """
    if request.method == "POST":
        malayalam_code = request.POST.get("code", "")  # Get the submitted Malayalam code

        try:
            # Step 1: Translate the Malayalam code into Python
            translated_code = process_code(malayalam_code)

            # Debugging: Print the translated code
            print("Translated Code:")
            print(translated_code)

            # Step 2: Use the system's Python executable
            result = subprocess.run(
                [sys.executable, "-c", translated_code],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=5,
            )

            # Step 3: Get the output
            output = result.stdout if result.stdout else result.stderr

            # Step 4: Convert Manglish output back to Malayalam
            malayalam_output = convert_to_malayalam(output)

            # Return the output to the frontend as JSON
            return JsonResponse({"output": malayalam_output})
        except subprocess.TimeoutExpired:
            print("Error: Code execution timed out.")
            return JsonResponse({"error": "കോഡ് പ്രവർത്തിക്കാൻ ദൈർഘ്യമേറിയ സമയം എടുത്തു. ദയവായി കോഡ് പരിശോധിക്കുക."})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": f"പിശക്: {str(e)}"})

    # Return error for invalid request methods
    return JsonResponse({"error": "അസാധുവായ അഭ്യർത്ഥന രീതിയ്"}, status=400)
