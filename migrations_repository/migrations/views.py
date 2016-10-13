from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from .forms import PlanForm, CircuitForm, UserForm
from .models import Plan, Circuit
from django.template import RequestContext

# Create your views here.


CUT_SHEET_FILE_TYPE = ['.xlsx']


def create_plan (request) :

	if not request_user.is_authenticate() :
		
		return render (request, 'migrations/login.html')

	else :
	
		form = PlanForm (request.POST or None, request.FILES or None)
		if form.is_valid () :
		
			plan = form.save (commit = FALSE)
			plan.user = request.user
			plan.save()
			return render (request, 'migrations/detail.html', {'plan' : plan})

		context = {
				'form' : form,
			}
		return render (request, 'migrations/create_plan.html', context)

def create_circuit (request, plan_id) :

	form = CircuitForm (request.POST or None, request.FILES or None)
	plan = get_object_or_404 (Plan, pk = plan_id)

	if form.is_valid () :
	
		plan_circuit = plan.ciruit_set.all ()
		circuit = form.save(commit = False)
		circuit.plan = plan
		circuit.cut_file = request.FILES['cut_file']
		file_type = circuit.cut_file.url.split('.')[-1]
		file_type = file_type.lower()

		if file_type not in CUT_SHEET_FILE_TYPE :
			
			context = {'plan' : plan, 'form' : form, 'error message': 'Invalid File Type'}
			return render (request, 'migrations/create_circuit.html', context)

		circuit.save()
		return render (request, 'migrations/detail.html', {'plan' : plan })

	context = {'album': album, 'form': form}
	return render (request, 'migrations/create_circuit.html', context)


		
def detail (request, plan_id) :

	if not request.user.is_authenticated() :
		return render (request, 'migrations/login.html')

	else :
		
		user = request.user
		plan = get_object_or_404(Plan, pk = plan_id)
		return render (request, 'migrations/detail.html', {'plan':plan, 'user':user})

def index (request) :

	if not request.user.is_authenticated () :
		
		return render (request, 'migrations/login.html')

	else :
		
		plans = Plan.objects.filter (user = request.user)
		circuit_results = Circuit.objects.all()
		query = request.GET.get("q")
	
		if query :
		
			plans = plans.filter ( Q(plan_number_icontains=query) | Q(plan_type_icontains=query)).distinct()
			circuit_results = circuit_results.filter (Q(cut_date_icontains = query)).distinct()
			return render (request, 'migrations/index.html', {'plans': plans, 'songs': circuit_result})
		else :
			
			return render (request, 'migrations/index.html', {'albums' : albums})

def logout_user (request) :

	logout (request)
	form = UserForm (request.POST or None)
	context = {"form": form}

	return render (request, 'migrations/logout.html', context)

def login_user (request) :

	if request.method == "POST" :
		
		username = request.POST['username']
		password = request.POST ['password']
		user = authenticate (username = username, password = password)

	   	if user is not None :
		
			if user.is_active :

				login (request, user)
				plans = Plan.objects.filter(user = request.user)
				return render (request, 'migrations/index.html', {'albums': albums})

			else :
				return render (request,'migrations/login.html', {'error message' : 'Your account is disabled'})

		else :

			return render (request, 'migrations/login.html', {'error message' : 'Invalid Login'})
	

	return render (request, 'migrations/login.html')

def register (request) :

	form = UserForm (request.POST or None)
	if form.is_valid() :
	
		user = form.save (commit = False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save ()
		user = authenticate (username = username, password = password)
		if user is not None :
		
			if user.is_active :
			
				login (request, user)
				plans = Plan.objects.filter (user = request.user)
				return render (request, 'migrations/index.html', {'plans' : plans})
	context = {"form" : form}

	return render (request, 'migrations/register.html', context)


def circuits (request, filter_by) :

	if not request.user.is_authenticated () :

		return render (request, 'migrations/login.html')

	else :

		try :
	
			circuit_ids = []

			for plan in Plan.object.filter (user = request.user) :

				for song in plan.circuit_set.all () :

					song_ids.append (song.pk)

			users_circuit = Circuit.objects.filter (pk__in = circuit_ids)
			
		except Plan.DoesnotExist :
	
			users_circuits = []
		return render (request, 'migrations/circuits.html', {'circuit_list':users_circuits, 'filter_by':filter_by})






 
