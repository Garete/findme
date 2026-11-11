
#!/usr/bin/env python3

import hashlib
import getpass
import sys
import hmac

EXPECTED_HASH = (
    "0f2ea4761275c99c6bd7c98c23177263d582d702e3bbd8dc1177168b98c73aa1"
)

print("================================")
print("        SYSTEM RECOVERY")
print("================================")

try:
    password = getpass.getpass("Enter recovery password: ")

except KeyboardInterrupt:
    print("\n[!] Recovery process cancelled.")
    sys.exit(130)

except EOFError:
    print("\n[!] Input stream closed. Exiting.")
    sys.exit(1)

provided_hash = hashlib.sha256(
    password.encode()
).hexdigest()

if hmac.compare_digest(provided_hash, EXPECTED_HASH):
    print("\n[+] Authentication successful.")
    print("[+] Recovery access granted.")
    print("[+] Proceed to the next stage.")
else:
    print("\n[-] Authentication failed.")
    print("[-] Recovery access denied.")
    sys.exit(1)
