calls = 0
def count_calls():
    global  calls
    calls += 1
def string_info(string):
    kort = str((len(string)))
    high =string.upper()
    low = string.lower()
    count_calls()
    return kort, high, low
def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    count_calls()
    return result
print(string_info('Privet Medved'))
print(string_info('Zdarova Korova'))
print(is_contains('123', ['Banana', ' Kric', 'Privet']))
print(is_contains('PRiv', ['Priv', 'Prime', 'priv']))
print(calls)



