# During an incoming call, phones usually display on the screen the number of
# the caller. If the number was previously saved in the contacts, the phone
# displays the name of the caller from the contact list instead. Your task is
# to write a function which determines what should be displayed on the phone
# screen during an incoming call.
# Write a function:
# def solution (phone_numbers, phone_owners, number)
# that, given the contact list in the form of two arrays, phone_numbers and
# phone_owners, consisting of N strings each, and a string number denoting the
# caller's number, returns the name of corresponding contact, or just number
# if the number is not present in the contact list.
# phone_numbers[J] contains the phone number of the person from
# phone_owners[J], where J is within the range [0..N - 1]

def solution(phone_numbers, phone_owners, number):
    phonebook = {phone_numbers[i]: phone_owners[i]
                 for i in range(len(phone_numbers))}

    return number if number not in phone_numbers else phonebook[number]


assert solution(
    phone_numbers=["234-567-890", "444-444-444", "321-543-234"],
    phone_owners=["Harry", "Nick", "Michael"],
    number="444-444-444"
) == "Nick"

assert solution(
    phone_numbers=["123-123-123"],
    phone_owners=["Walter"],
    number="111-111-111"
) == "111-111-111"

assert solution(
    phone_numbers=["123-456-123"],
    phone_owners=["Henry T."],
    number="123-456-123"
) == "Henry T."

assert solution(
    phone_numbers=["111-111-112", "211-111-111"],
    phone_owners=["laundry", "call center"],
    number="111-111-111"
) == "111-111-111"
