inp=input()
print('Execution Started.')
try:
    if not inp:
        raise Exception('No input. Stopping execution.')
except Exception as e:
    print(e)
else:
    
