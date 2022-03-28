from django.contrib.auth.forms import PasswordChangeForm

class psw_ch(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(psw_ch, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None
