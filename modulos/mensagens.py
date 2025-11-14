def sucesso(msg):
    print(f"\n\033[1;32m{msg}\033[0;0m\n")


def erro(msg):
    print(f"\033[1;31m{msg}\033[0;0m\n")


def titulo(msg):
    print("\n\033[1;36m", "-" * 10, f"{msg}", "-" * 10, "\033[0;0m\n")


def info(msg):
    print(f"\033[1;33m{msg}\033[0;0m")