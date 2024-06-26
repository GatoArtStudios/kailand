import psutil
def memory_total() -> int:
    """
    Calcula la memoria total del sistema en gigabytes.

    Devuelve:
        int: La memoria total del sistema en gigabytes.
    """
    # Obtiene la memoria virtual del sistema
    mem = psutil.virtual_memory()

    # Calcula la memoria total en gigabytes
    memory_total = round(mem.total / (1024 ** 3))

    if memory_total <= 16:
        return memory_total

    # Si la memoria total es mayor de 16 GB, devuelve 16 GB
    return 16

def memory_divide() -> int:
    mem = memory_total()
    mem -= 2
    return mem