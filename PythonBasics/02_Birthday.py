length = int(input())
width = int(input())
height = int(input())
percent_occupied_volume = float(input())

volume = length * width * height #cm3
total_liters = volume * 0.001  #liters

percent = percent_occupied_volume * 0.01

needed_liters = total_liters * (1-percent)

print(f'{needed_liters:.3f}')