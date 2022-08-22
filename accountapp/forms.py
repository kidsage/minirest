from django.contrib.auth.forms import UserCreationForm

class AccountCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = '- 특수문자는 @ . + - _만 가능합니다.'
        self.fields['password1'].help_text = ('- 8글자 이상 입력해주세요.\r - 영문과 숫자를 섞어 주세요.')
        self.fields['password2'].help_text = '- 위 비밀번호와 동일하게 입력해주세요.'


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)

        self.fields['username'].disabled = True # username 비활성화
        self.fields['username'].help_text = '- 특수문자는 @ . + - _만 가능합니다.'
        self.fields['password1'].help_text = '- 8글자 이상 입력해주세요.\n- 영문과 숫자를 섞어 주세요.'
        self.fields['password2'].help_text = '- 위 비밀번호와 동일하게 입력해주세요.'