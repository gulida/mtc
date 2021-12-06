from .bcolors import BColors


def running_time_counter(start, end, method_name):
    if (end - start) < 5:
        print(f' {BColors.RESET}{method_name}\n{BColors.OK}Running time of script: {end - start}. The script is running normal!')
    elif (end - start) < 10:
        print(f'{BColors.RESET}{method_name}\n{BColors.WARNING}Running time of script: {end - start}. !!! Warning: The script '
              f'is running normal!')
    else:
        print(f'{BColors.RESET}{method_name}\n{BColors.FAIL}Running time of script: {end - start}. !!! Run time fail: The '
              f'script runs too long!')
