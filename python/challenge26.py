def int32_to_ip(int32):
    # Get the first octet (bits 24-31)
    octet1 = (int32 >> 24) & 0xFF

    # Get the second octet (bits 16-23)
    octet2 = (int32 >> 16) & 0xFF

    # Get the third octet (bits 8-15)
    octet3 = (int32 >> 8) & 0xFF

    # Get the fourth octet (bits 0-7)
    octet4 = int32 & 0xFF

    # Convert each octet to a string
    string1 = str(octet1)
    string2 = str(octet2)
    string3 = str(octet3)
    string4 = str(octet4)

    # Join them with dots to form the IPv4 address
    ipv4_address = string1 + "." + string2 + "." + string3 + "." + string4

    # Return the result
    return ipv4_address
