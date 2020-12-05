with open("advent20-5a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[len(input) - 1]

def seat_number(boarding_pass):
    seat_number = 0
    for i in range(10):
        seat_number += 2**(9 - i) * (boarding_pass[i] == 'B' or boarding_pass[i] == 'R')
    return seat_number

seats_taken = []
for boarding_pass in input:
    seats_taken.append(seat_number(boarding_pass))

for seat in range(2**10):
    if (seat-1) in seats_taken and (seat+1) in seats_taken and seat not in seats_taken:
        print seat
