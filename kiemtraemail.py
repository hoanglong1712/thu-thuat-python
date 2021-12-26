# %%
# ham kiem tra email hop le

# ten@ten.duoi

#  phai co 1 ky tu @
# phai co 1 dau .
# @ dung truoc . 
# khoang cach giua @ va . >= 1
# @ khong phai la ky tu dau tien cua email
# . khong phai la ky tu cuoi cung

def kiem_tra_email(email_):
    if email_ is None:
        return False
    #   2@4.6
    if len(email_) <  6:
        return False
    at = email_.find('@')
    period = email_.find('.')

    if at < 0:
        return False
    if period < 0:
        return False
    if at > period:
        return False
    if period - at < 2:
        return False
    if at == 0:
        return False
    
    if period == len(email_) - 1:
        return False

    return True

print(kiem_tra_email('hoanglong1712@yahoo.com'))
print(kiem_tra_email('@yahoo.com'))
print(kiem_tra_email('hoanglong1712@yahoo.'))
print(kiem_tra_email('hoanglong1712yahoo.com'))
print(kiem_tra_email('hoanglong1712@yahoocom'))
print(kiem_tra_email('hoanglong1712@.com'))




