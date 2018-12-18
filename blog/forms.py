from django import forms
from blog.models import snippet

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your name'}))
	email = forms.EmailField(label='E-Mail',
							widget=forms.TextInput(attrs={'placeholder':'Your E-mail'}))
	subject = forms.CharField(required=False,
							widget=forms.TextInput(attrs={'placeholder':'Subject'}))
	body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message','rows':4}))


class SnippetForm(forms.ModelForm):
	
	class Meta:
		model = snippet
		fields = ('email','name','subject','body')
		widgets = {
				'email': forms.TextInput(attrs={'placeholder':'Your e-mail'}),
				'name':forms.TextInput(attrs={'placeholder':'Your name'}),
				'subject':forms.TextInput(attrs={'placeholder':'Subject'}),
				'body':forms.Textarea(attrs={'placeholder':'Message','rows':4})
		}
