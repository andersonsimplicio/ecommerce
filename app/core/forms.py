from django import forms

class ContactFrom(forms.Form):
    nome = forms.CharField(label='nome')
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label='Mensagem',widget=forms.Textarea())
    
    def __init__(self,*args,**kwargs):
        super(ContactFrom,self).__init__(*args,**kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['mensagem'].widget.attrs['class'] = 'form-control'
        