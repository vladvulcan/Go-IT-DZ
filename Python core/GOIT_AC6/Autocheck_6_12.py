import base64


def encode_data_to_base64(data):
    for i in range(len(data)):
        byt64 = base64.b64encode(data[i].encode())
        data[i] = byt64.decode()
    return data