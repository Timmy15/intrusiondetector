from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import FormOne, Attack, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from functools import wraps

# Initialize encoder globally so you can use it in multiple views if needed


# model = joblib.load('base/random_forest_model.pkl')
# Create your views here.

# Load the model when the module is imported
# model = joblib.load('path_to_your_model/random_forest_model.pkl')

# attacks = [
#     {'id': 1, 'name': 'DOS Attacks'},
#     {'id': 2, 'name': 'R2L Attacks'},
#     {'id': 3, 'name': 'U2R Attacks'},
#     {'id': 4, 'name': 'Probing Attacks'},
# ]

@login_required(login_url='login')
def dashboard(request):
    page= 'dashboard'

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    attacks = Attack.objects.filter(
        Q(severity_level__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    label = FormOne.objects.all()
    #ladel = FormOne.objects.order_by('-created').values_list('label', flat=True)[:5]
    #[0:5]
    label_count = label.count()
    
    # connection_messages = Message.objects.filter(Q(label__icontains=q))


    
    context={'page': page, 'attacks': attacks, 'label_count': label_count, 'label': label}
    return render(request, 'base/dashboard.html', context)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Username OR Password does not exist")

    context={'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'An error occurred during registration')
        
    return render(request, 'base/login_register.html', {'form': form})

@login_required(login_url='login')
def updateUser(request):
    user= request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

# # def home(request):
# #     attacks = Attack.objects.all()
# #     context = {'attacks': attacks}
# #     return render(request, 'base/home.html', context)

# def home(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''

#     attacks = Attack.objects.filter(
#         Q(severity_level__icontains=q) |
#         Q(name__icontains=q) |
#         Q(description__icontains=q)
#         )

#     labels = Label.objects.all()[0:5]
#     label_count = labels.count()
    
#     connection_messages = Message.objects.filter(Q(label__name__icontains=q))

#     context = {'attacks': attacks, 'label_count': label_count, 'connection_messages': connection_messages}
#     return render(request, 'base/home.html', context)

def has_submitted_form(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        form_id = kwargs.get('form_id')  # assuming you pass the form's ID in the URL or as a parameter
        
        if form_id:
            # If a form_id is passed, fetch that specific form instance
            form_instance = FormOne.objects.filter(id=form_id, user=request.user).first()
        else:
            # Otherwise, get the latest FormOne instance for the user
            form_instance = FormOne.objects.filter(user=request.user).order_by('-created').first()
        
        if form_instance and form_instance.is_DOS in [1, 0]:
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to form submission page if no such instance exists or if is_DOS is not 1
            return redirect('predict_dos')
    return _wrapped_view

@login_required(login_url='login')
@has_submitted_form
def attack(request, form_id=None):
    attack = Attack.objects.all()
    # If form_id is specified, it means the user clicked on a specific label
    if form_id:
        form_instance = FormOne.objects.get(id=form_id)
    # Else, the user is probably coming after submitting a form
    else:
        form_instance = FormOne.objects.filter(user=request.user).latest('created')
    context = {'attack': attack,'form_instance': form_instance}
    return render(request, 'base/attack.html', context)

@login_required(login_url='login')
@has_submitted_form
def results(request, form_id=None):
    page= 'results'
    if form_id:
        form_instance = FormOne.objects.get(id=form_id)
    # Else, the user is probably coming after submitting a form
    else:
        form_instance = FormOne.objects.filter(user=request.user).latest('created')
    # You can also pass additional context/data if needed
    context={'page': page, 'form_instance': form_instance}
    return render(request, 'base/results.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    label = user.label_set.all()
    #connection_messages = user.message_set.all()
    messages = Message.objects.all()
    context = {'user': user, 'messages': messages, 'label': label}
    return render(request, 'base/profile.html', context)



# def predict_dos(request):
#     form = RoomForm()
#     labels=FormOne.objects.all()
#     if request.method == 'POST':
#         label_name=request.POST.get('label')
#         label, created = FormOne.objects.get_or_create(name=label_name)

#         FormOne.objects.create(
#             user=request.user,
#             label=request.POST.get('label'),
#             protocol_service=request.POST.get('protocol_service'),
#             protocol_type=request.POST.get('protocol_type'),
#             src_bytes=request.POST.get('src_bytes'),
#             dst_bytes=request.POST.get('dst_bytes'),
#             the_count=request.POST.get('the_count'),
#             srv_count=request.POST.get('srv_count'),
#             dst_host_diff_srv_rate=request.POST.get('dst_host_diff_srv_rate'),
#             dst_host_same_src_port_rate=request.POST.get('dst_host_same_src_port_rate'),
#         )
#         return redirect('dashboard')

#     context={'form': form, 'labels': labels}
#     return render(request, 'base/form.html', context)


# def predict_dos(request):
    # if request.method == 'POST':
    #     form = RoomForm(request.POST)
        
    #     if form.is_valid():
    #         label_name = form.cleaned_data['label_name']
            
    #         # Check if a label with this name already exists
    #         if Label.objects.filter(name=label_name).exists():
    #             form.add_error('label', 'This label already exists. Please choose a unique label.')
    #         else:
    #             # Create a new label with the provided name
    #             new_label = Label.objects.create(name=label_name)

    #             # Attach the user and the label to the form instance and save
    #             form_instance = form.save(commit=False)
    #             form_instance.user = request.user
    #             form_instance.label = new_label
    #             form_instance.save()
                
    #             return redirect('dashboard')
    # else:
    #     form = RoomForm()

    # labels = Label.objects.all()
    # context = {'form': form, 'labels': labels}
    # return render(request, 'base/form.html', context)

@login_required(login_url='login')
def predict_dos(request):

    if request.method == 'POST':
        form = RoomForm(request.POST)
        
        if form.is_valid():
            label_name_value = form.cleaned_data['label']
            # Check if a label with this name already exists
            if FormOne.objects.filter(label=label_name_value).exists():
                form.add_error('label', 'This label already exists. Please choose a unique label.')
            else:
                # Prepare the input data for the model
                # Extract relevant fields from the form
                # Attach the user, the label, and the prediction result to the form instance and save
                form_instance = form.save(commit=False)
                form_instance.user = request.user
                # Create a new label with the provided name
                form_instance.label = label_name_value
                form_instance.save()
        
                # Now preprocess this newly saved data
                encoder = joblib.load('base/encoder.pkl')
                scaler = joblib.load('base/scaler.pkl')


                # Extract and preprocess categorical data
                other_input_data = [
                    form.cleaned_data['protocol_type'],
                    form.cleaned_data['protocol_service']
                ]

                encoded_data = encoder.transform([other_input_data]).toarray()
                encoded_columns = encoder.get_feature_names_out(['protocol_type', 'protocol_service'])
                encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

                input_data = [
                    form.cleaned_data['dst_host_diff_srv_rate'],
                    form.cleaned_data['dst_host_same_src_port_rate'],
                    form.cleaned_data['dst_bytes'],
                    form.cleaned_data['srv_count'],
                    form.cleaned_data['src_bytes'],
                    form.cleaned_data['the_count']
                ]

                
                # 2. Standardize the fields (using the same scaler logic)
                standardized_data = scaler.transform([input_data])
                standardized_df = pd.DataFrame(standardized_data, columns=['dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_bytes', 'srv_count', 'src_bytes', 'the_count'])
                # Concatenate both preprocessed data
                prediction_data = pd.concat([encoded_df, standardized_df], axis=1)

                selected_features = joblib.load('base/selected_features.pkl')
                prediction_data = prediction_data[selected_features]
                # 3. Make a prediction using the model
                model = joblib.load('base/new_random_forest_model.pkl')
                prediction = model.predict(prediction_data)
                # Here, prediction[0] will be 0 or 1, depending on the model's output
                
                
                form_instance.is_DOS = prediction[0] # Assuming you have a prediction field in your model
                form_instance.save()

                if prediction[0] == 1:
                    return redirect('attack_view', form_id=form_instance.id)
                else:
                    return redirect('results_view',form_id=form_instance.id)

    else:
        form = RoomForm()

    all_forms = FormOne.objects.all()
    context = {'form': form, 'all_forms': all_forms}
    return render(request, 'base/form.html', context)

def labelsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    ladels = FormOne.objects.order_by('-created').values_list('label', flat=True)[:5]
    labels=FormOne.objects.filter(label__icontains=q)
    return render(request, 'base/labels.html', {'labels': labels, 'ladels': ladels})

@login_required(login_url='login')
def deleteForm(request, pk):
    predict=FormOne.objects.get(id=pk)

    if request.user != predict.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        predict.delete()
        return redirect('dashboard')
    return render(request, 'base/delete.html', {'obj':predict})





# # def handle_form_submission(request):
# #     # Get data from form
# #     network_info = request.POST.get('network_info')
# #     # Pass data to ML model and get prediction
# #     predicted_attack_name = my_ml_model.predict(network_info)
# #     # Lookup the corresponding AttackType
# #     attack_type = AttackType.objects.get(name=predicted_attack_name)
# #     # Create new ThreatReport
# #     report = ThreatReport(network_info=network_info, predicted_attack=attack_type)
# #     report.save()
