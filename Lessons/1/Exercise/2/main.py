inputSeconds = remainderSeconds = int(input("Введите секунды: "))
hour = remainderSeconds // (60 * 60)
remainderSeconds = remainderSeconds % (60 * 60)
minutes = remainderSeconds // 60
seconds = remainderSeconds % 60
print(F'Результат перевода секунд {inputSeconds} в чч:мм:сс {hour:02}:{minutes:02}:{seconds:02}')
