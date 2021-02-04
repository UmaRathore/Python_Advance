# Error Handling

while True:
    try:
        age = int(input('Enter your age'))
        print(f'My age is :  {50/age}')
    except ValueError:
        print('Enter a number')
# this will not be printed, as soon as interpreter reaches first ValueError it will go back to while loop
    # except ValueError:
        # print('!!!!')
    except ZeroDivisionError:
        print('Enter number other than zero')
    else:
        print('Thank You')
        break
    finally:
        print('Thank You!')
