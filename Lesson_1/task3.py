from datetime import datetime
timestamp = int(input('Введіть кількість секунд: '))
dt = datetime.fromtimestamp( timestamp )
print( dt )
