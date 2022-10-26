from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row



class ContactForm(forms.Form):
	name=forms.CharField()#required=False
	email=forms.EmailField(label='E-Mail')
	github = forms.CharField(
		label='GitHub Link',
		required=False
	)
	linkedin = forms.CharField(
		label='LinkedIn Link',
		required=False
	)
	skills=forms.CharField()
	objective = forms.CharField()
	degree = forms.CharField()
	college = forms.CharField()
	percentage = forms.CharField()
	projectname = forms.CharField(
		label='Project Name',
		required=False,
	)
	projectdesc = forms.CharField(
		label='Project Description',
		required=False,
	)
	projectlink = forms.CharField(
		label='Project(GitHub) Link',
		required=False,
	)
	certificate1 = forms.CharField(
		label='Add Certificate 1',
		required=True,
	)
	certificate2 = forms.CharField(
		label='Add Certificate 2',
		required=True,
	)
	certificate3 = forms.CharField(
		label='Add Certificate 3',
		required=True,
	)

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper
		self.helper.form_class = ' container justify-content-center '
		# self.helper.label_class = ''
		# self.helper.field_class = 'col-md-6 col-xs-9'
		self.helper.form_method="post"
		self.helper.layout=Layout(
			Row(
                Column('name', css_class='form-group col-md-5  mb-10'),
                Column('email', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('objective'),
                css_class='form-row  center'
			),
			Row(
				Column('github'),
				Column('linkedin'),
			),
			Row(
                Column('skills'),
                css_class='form-row  center'
			),
			Row(
				Column('degree'),
				Column('college'),
				Column('percentage'),
			),
			Row(
				Column('projectname'),
				Column('projectdesc'),
				Column('projectlink'),
			),
			Row(
				Column('certificate1'),
				Column('certificate2'),
				Column('certificate3'),
			),
			Submit('submit','Submit',css_class="btn-success")
			)