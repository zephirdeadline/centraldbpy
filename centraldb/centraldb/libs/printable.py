def print_warning(str):
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    print(WARNING + str + ENDC + '\n')


def print_error(str):
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    print(FAIL + str + ENDC + '\n')


def print_success(str):
    SUCCESS = '\033[92m'
    ENDC = '\033[0m'
    print(SUCCESS + str + ENDC + '\n')
