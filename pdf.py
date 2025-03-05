import pypdf as p
def subString(Str, n):
    substrings = []
    for Len in range(1, n + 1):
        for i in range(n - Len + 1):
            substring = Str[i:i + Len]
            substrings.append(substring)
    return substrings

reader = p.PdfReader('Yashu page1-2_protected.pdf')
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# reader.decrypt('Potti')
# for page in reader.pages:
#     print(page.extract_text())
for password in letters:
    try:
        if reader.is_encrypted:
            reader.decrypt(password)
            page = reader.pages[0:1] 
            print(page.extract_text())
            break
    except p.errors.FileNotDecryptedError as ex:
        print('Try next letter')

