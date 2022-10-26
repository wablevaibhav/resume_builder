from django.shortcuts import render
from .forms import ContactForm

def home(request):
	return render(request, 'home.html', {})

def info(request):
	form=ContactForm()
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			email=form.cleaned_data['email']
			github = form.cleaned_data['github']
			linkedin = form.cleaned_data['linkedin']
			skills=form.cleaned_data['skills']
			objective = form.cleaned_data['objective']
			degree = form.cleaned_data['degree']
			college = form.cleaned_data['college']
			percentage = form.cleaned_data['percentage']
			projectname = form.cleaned_data['projectname']
			projectdesc = form.cleaned_data['projectdesc']
			projectlink = form.cleaned_data['projectlink']
			certificate1 = form.cleaned_data['certificate1']
			certificate2 = form.cleaned_data['certificate2']
			certificate3 = form.cleaned_data['certificate3']

			data={'name':name}
			data['email']=email
			data['github']=github
			data['linkedin']=linkedin
			data['skills']=skills
			data['objective'] = objective
			data['degree'] = degree
			data['college'] = college
			data['percentage'] = percentage
			data['projectname'] = projectname
			data['projectdesc'] = projectdesc
			data['projectlink'] = projectlink
			data['certificate1'] = certificate1
			data['certificate2'] = certificate2
			data['certificate3'] = certificate3
			


			return render(request,'home.html',data)
			#to add more go to : forms.py
			# print(name,email)
	return render(request,'info.html',{'form':form})