from django import forms


class LoginForm(forms.Form):
    # username, password를 받을 수 있도록 함
    # password는 widget에 PasswordInput을 사용하기
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )