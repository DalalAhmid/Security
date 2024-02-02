# 2.2
from part1 import vigenere_cipher

# frequancy analysis of characters using included dictionary
def frequency_analysis(input_string):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    freq_dict = {char: 0 for char in symbols}

    total_characters = len(input_string)
    for char in input_string:
        if char.upper() in freq_dict:
            freq_dict[char.upper()] += 1

    for char, count in freq_dict.items():
        freq_dict[char] = count / total_characters

    return freq_dict

# Example usage:
input_text = "AB CD"
result_frequency_analysis = frequency_analysis(input_text)

for char, freq in result_frequency_analysis.items():
    print(f"{char}: {freq}")

# 2.3
set_1 = {'A': 0.012, 'B': 0.003, 'C': 0.01, 'D': 0.1, 'E': 0.02, 'F': 0.001}
set_2 = {'A': 0.001, 'B': 0.012, 'C': 0.003, 'D': 0.01, 'E': 0.1, 'F': 0.02}
set_3 = {'A': 0.1, 'B': 0.02, 'C': 0.001, 'D': 0.012, 'E': 0.003, 'F': 0.01}

# calculate cross-correlation
def cross_correlation(set_x, set_y):
    correlation = sum(set_x[val] * set_y[val] for val in set_x)
    return correlation

# cross-correlation between Set 1 and Set 2
correlation_12 = cross_correlation(set_1, set_2)

# Calculate cross-correlation between Set 1 and Set 3
correlation_13 = cross_correlation(set_1, set_3)

print("Cross-correlation between Set 1 and Set 2:", correlation_12)
print("Cross-correlation between Set 1 and Set 3:", correlation_13)

# 2.4
#get caesar shift using the cross correlation of different shifts 
def get_caesar_shift(enc_message, expected_dist):
    def cross_correlation(set_x, set_y):
        correlation = sum(set_x[val] * set_y[val] for val in set_x)
        return correlation

    def shift_dict(input_dict, shift):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        shifted_dict = {}
        for key, value in input_dict.items():
            if key == ' ':
                new_key = ' '
            else:
                index = (alphabet.index(key) + shift) % 26
                new_key = alphabet[index]
            shifted_dict[new_key] = value
        return shifted_dict

    max_correlation = -1
    likely_shift = 0

    for shift in range(27):  # increase the range to 27 to account for the space character
        # Shift the expected distribution
        shifted_dist = shift_dict(expected_dist, shift)

        # cross-correlation with the shifted expected distribution
        correlation = cross_correlation(shifted_dist, frequency_analysis(enc_message))

        # Update max correlation and likely shift
        if correlation > max_correlation:
            max_correlation = correlation
            likely_shift = shift

    return likely_shift

# Example usage (ciphertext is from geeksforgeeks):
enc_message = "EXXEGOEXSRGI"
expected_dist = {' ': 0.1828846265, 'E': 0.1026665037, 'T': 0.0751699827, 'A': 0.0653216702, 'O': 0.0615957725, 'N': 0.0571201113, 'I': 0.0566844326, 'S': 0.0531700534, 'R': 0.0498790855, 'H': 0.0497856396, 'L': 0.0331754796, 'D': 0.0328292310, 'U': 0.0227579536, 'C': 0.0223367596, 'M': 0.0202656783, 'F': 0.0198306716, 'W': 0.0170389377, 'G': 0.0162490441, 'P': 0.0150432428, 'Y': 0.0142766662, 'B': 0.0125888074, 'V': 0.0079611644, 'K': 0.0056096272, 'X': 0.0014092016, 'J': 0.0009752181, 'Q': 0.0008367550, 'Z': 0.0005128469}

shift = get_caesar_shift(enc_message, expected_dist)
print("Likely Caesar shift:", shift)

# attempt at vigenere keyword method, uses logic in instructions but I couldnt decrypt the messages as none of the identified  keywords worked
def get_vigenere_keyword(enc_message, size, expected_dist):
    # Divide the encrypted message into separate messages
    messages = ['' for _ in range(size)]
    for i, char in enumerate(enc_message):
        messages[i % size] += char

    # Find the shift for each message and convert to character
    keyword = ''
    for message in messages:
        shift = get_caesar_shift(message, expected_dist)
        keyword += chr((shift % 26) + ord('A'))

    return keyword

enc_message = "TEZHRAIRGMQHNJSQPTLNZJNEVMQHRXAVASLIWDNFOELOPFWGZ UHSTIRGLUMCSW GTTQCSJULNLQK OHL MHCMPWLCEHTFNUHNPHTSFFADJHTLNBYORWEFRYE PIISO K ZQR GMPTLQCSPRMOCMKESMTYLUTFRMIEOWXXFMWECCLWSQGWUASSWFGTTMYSGU L QNQGEFGTTIDSWMOAGMKEOQL U KOVN AMZHZRGACMKHZRHSQLKLBMJAXTKLVRGFCBTLNAM SMYAHEGIEHTKNFOELNBMWFGORHWTPAY MVOSGUVUSPD"
key_size = 10  #must try different key sizes

keyword = get_vigenere_keyword(enc_message, key_size, expected_dist)
print("Probable Vigenere Keyword:", keyword)
decrypted_message2 = vigenere_cipher(enc_message, keyword, encrypt=False)
print(decrypted_message2)

