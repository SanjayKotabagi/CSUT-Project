import pwnedpasswords

def get_pawned_password(value):
    if pwnedpasswords.check(value) > 0:
        return f"Password '{value}' has been pawned in any data breach."
    else:
        return "Password has not been breached"

# def get_pawned_mail(value):
#     pass
