def blank_receipt(cash_receipt, charged_to, received_to, softuni):
    print(cash_receipt)
    print('------------------------------')
    print(f'{charged_to}____________________')
    print(f'{received_to}___________________')
    print('------------------------------')
    print(f'© {softuni}')

blank_receipt('CASH RECEIPT', 'Charged to', 'Received by', 'SoftUni')