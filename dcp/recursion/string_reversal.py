def string_reversal(ip):
    if ip == "":
        return ""

    return string_reversal(ip[1:]) + ip[0]


if __name__ == "__main__":
    ip = "chitrank"
    print(string_reversal(ip))
