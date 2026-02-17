try:

    print('Hello, this is a game guess the word;')
    print('-' *  35)
    user_0 = str(input('go to play'))

    if user_0 == '':
        num = 0

        user_1 = str(input('guess a word;\n'))

        user_2 = str(input('wont to give me a hint?\n'))
        max_num = int(input('enter, after how many attempts will a hint be given?\n'))
        print('-' * 35)
        user_22 = str(input('do you wont to give a second hint?\n'))
        max_num_22 = int(input('enter, after how many attempts will a second hint be given?\n'))

        for i in range(1, 101, 1):
            print(i)
            print('-' * 35)

        while True:

            user_3 = str(input('enter, the mystery word\n'))
            if user_3 == user_1:
                print('-' *35)
                print('HOORAY!')
                print('-' * 35)
                print('VICTORY !!!')
                print('-' * 35)
                break
            else:
                print('no, this is not the right word.')
                print('-' *  35)

                num += 1
                if num == max_num:
                    print('-',  35)
                    print('clue', user_2)

                if num == max_num_22:
                    print('-' * 35)
                    print('second clue', user_22)

                if user_3 == 'i give up':
                    print('you lost;')
                    print('mustery word', user_1)
                    break
except:
    print(ValueError)
    print('something is wrong.')
    print('restart the program')
    print('-' * 35)