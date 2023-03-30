import random
import time

print('\033[36mVAMOS JOGAR JOKEMPO!\033[m')
time.sleep(1)
print('\033[36mPODE ESCOLHER ENTRE \033[m')
time.sleep(0.5)
print('\033[36m[PEDRA - PAPEL - TESOURA]\033[m')
print('\n')
possible_choices = ['pedra', 'papel', 'tesoura']
user_choice = str(input('\033[33mQual você escolhe: \033[m')).lower()
computer_choice = random.choice(possible_choices)


if user_choice == computer_choice:
    print('-----EMPATE-----')
    print('\033[33mUsuário:\033[m {}'.format(user_choice))
    print('\033[33mComputador:\033[m {}'.format(computer_choice))
    print('-----EMPATE-----')
elif user_choice == 'tesoura' and computer_choice == 'papel':
    print('-----VENCEDOR-----')
    print('\033[33mUsuário:\033[m {}'.format(user_choice))
    print('\033[33mComputador:\033[m {}'.format(computer_choice))
    print('-----VENCEDOR-----')
elif user_choice == 'tesoura' and computer_choice == 'pedra':
    print('-----PERDEDOR-----')
    print('\033[33mUsuário:\033[m {}'.format(user_choice))
    print('\033[33mComputador:\033[m {}'.format(computer_choice))
    print('-----PERDEDOR-----')
elif user_choice == 'papel' and computer_choice == 'pedra':
    print('-----VENCEDOR-----')
    print('\033[33mUsuário:\033[m {}'.format(user_choice))
    print('\033[33mComputador:\033[m {}'.format(computer_choice))
    print('-----VENCEDOR-----')
elif user_choice == 'papel' and computer_choice == 'tesoura':
    print('-----PERDEDOR-----')
    print('\033[33mUsuário:\033[m {}'.format(user_choice))
    print('\033[33mComputador:\033[m {}'.format(computer_choice))
    print('-----PERDEDOR-----')
elif user_choice == 'pedra' and computer_choice == 'tesoura':
    print('-----VENCEDOR-----')
    print('\033[33mUsuário:\033[m {}'.format(user_choice))
    print('\033[33mComputador:\033[m {}'.format(computer_choice))
    print('-----VENCEDOR-----')
elif user_choice == 'pedra' and computer_choice == 'papel':
    print('-----PERDEDOR-----')
    print('\033[33mUsuário:\033[m {}'.format(user_choice))
    print('\033[33mComputador:\033[m {}'.format(computer_choice))
    print('-----PERDEDOR-----')
else:
    print('Error')
