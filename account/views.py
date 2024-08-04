from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login_view')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'is_admin') and user.is_admin:
                    return redirect('dashboard')
                elif hasattr(user, 'is_manager') and user.is_manager:
                    return redirect('dashboard')
                elif hasattr(user, 'is_agent') and user.is_agent:
                    return redirect('showLead')
                else:
                    msg = 'User does not have a valid role'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

@login_required
@user_passes_test(lambda u: u.is_manager or u.is_admin)
def manager(request):
    return render(request, 'dashboard.html')

@login_required
@user_passes_test(lambda u: u.is_agent)
def agent(request):
    return render(request, 'show.html')

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     permission_classes = [IsAdminUser]


# class AuthUserLoginView(APIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:
#             status_code = status.HTTP_200_OK

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User logged in successfully',
#                 'email': serializer.data['email'],
#                 'role': serializer.data['role']
                
#             }
            
#             return Response(response, status=status_code)