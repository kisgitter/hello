try:
    print('try...')
    if 1==0:
        raise ValueError('当然这是不可能的了哈哈哈')
    r = 10 / int('a')
    print('result:', r)
except Exception as e:
    print('Exception:',e)
except  (ValueError,TypeError) as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error')
finally:
    print('finally...')
print('END')
