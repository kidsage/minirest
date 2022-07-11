from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs): # 전체상속
        super().__init__(*args, **kwargs) # 초기화

        self.fields['username'].disabled = True # username 비활성화