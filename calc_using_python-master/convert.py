
class Converter:
    @staticmethod
    def bitsbytes(bits):
        return bits / 8

    @staticmethod
    def bytesbits(bytes):
        return bytes * 8

    @staticmethod
    def byteskilobytes(bytes):
        return bytes / 1024

    @staticmethod
    def kilobytesbytes(kilobytes):
        return kilobytes * 1024

    @staticmethod
    def bytesmegabytes(bytes):
        return bytes / (1024 ** 2)

    @staticmethod
    def megabytesbytes(megabytes):
        return megabytes * (1024 ** 2)
