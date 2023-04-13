import re
import os


def format_phone(string):
    lst = re.findall(r'[0-9]', string)
    formatted_number = ''
    number = ''
    for x in range(1, 5):
        formatted_number = lst[-x] + formatted_number
        number = lst[-x] + number
    formatted_number = '-' + formatted_number
    for x in range(5, 8):
        formatted_number = lst[-x] + formatted_number
        number = lst[-x] + number
    formatted_number = '-' + formatted_number
    for x in range(8, 11):
        formatted_number = lst[-x] + formatted_number
        number = lst[-x] + number
    return int(number), formatted_number


def main():
    # with open('./assets/potential-contacts.txt', 'r') as f:
    with open('./tests/content.txt', 'r') as f:
        lines = f.readlines()
    try:
        os.mkdir('content')
    except FileExistsError:
        pass
    emails = open('./content/emails.txt', 'w')
    phones = open('./content/phone_numbers.txt', 'w')

    email_r = r'\w+@\w+\.\w+'
    phone_r = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phone_dict = {}
    email_lst = []

    for line in lines:
        e = re.findall(email_r, line)
        p = re.findall(phone_r, line)
        for x in e:
            email_lst.append(x)
        for x in p:
            number, formatted_number = format_phone(x)
            phone_dict[number] = formatted_number

    sorted_numbers = sorted(phone_dict.keys())
    email_lst = sorted(email_lst)
    print(len(sorted_numbers))
    print(len(email_lst))

    for email in email_lst:
        emails.write(f'{email}\n')
    for number in sorted_numbers:
        phones.write(f'{phone_dict[number]}\n')

    emails.close()
    phones.close()


if __name__ == '__main__':
    main()
