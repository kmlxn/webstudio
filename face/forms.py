from django import forms
from captcha.fields import ReCaptchaField


class CaptchaFormRussian(forms.Form):
    captcha = ReCaptchaField(attrs={'lang': 'ru'})
    

class CaptchaFormEnglish(forms.Form):
    captcha = ReCaptchaField(attrs={'lang': 'en'})


def get_captcha_form(request):
    if request.LANGUAGE_CODE == 'ru':
        CaptchaFormClass = CaptchaFormRussian
    else:
        CaptchaFormClass = CaptchaFormEnglish
    
    if request.method == 'POST':
        return CaptchaFormClass(request.POST)
    return CaptchaFormClass()
