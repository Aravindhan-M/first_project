from functools import wraps
from .utils import re_captcha_validation


def check_re_captcha(view_func):
    @wraps(view_func)
    def _wrapped_view(self, form, *args, **kwargs):
        self.request.re_captcha_is_valid = None
        if self.request.method == 'POST':
            re_captcha_response = self.request.POST.get('g-recaptcha-response')
            self.request.re_captcha_is_valid = re_captcha_validation(re_captcha_response)
        return view_func(self, form, *args, **kwargs)
    return _wrapped_view
