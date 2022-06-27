def int32_to_ip(int32):
    first = int(int32 / 16777216) % 256
    second = int(int32 / 65536) % 256
    third = int(int32 / 256) % 256
    fourth = int(int32) % 256
    return '%(first)s.%(second)s.%(third)s.%(fourth)s' % locals()


if __name__ == "__main__":
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"
