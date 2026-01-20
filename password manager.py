import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def load_vault():
    try:
        with open("vault.txt", "r") as f:
            return f.read().splitlines()

    except FileNotFoundError:
        return []


def save_vault(vault):
    with open("vault.txt", "w") as f:
        f.write("\n".join(vault))

def add_credential(vault):
    service =input("enter service name : ").strip()
    if not service:
        print("No service name entered")
        return
    user_name = input("enter username : ").strip()
    if not user_name:
        print("empty username")
        return
    password = input("enter password : ").strip()
    if not password:
        print("no password has entered")
        return

    hash_pass =hash_password(password)
    vault.append(f"{service}|{user_name}|{hash_pass}")
    save_vault(vault)

def view_services(vault):
    if not vault:
        print("No service found")
        return
    for index , v in enumerate(vault,start=1):
        entry = v.split("|")
        print(f"{index}. {entry[0]}")


def view_credential(vault):

    view_services(vault)
    service_choose =input("enter service number : ").strip()
    if not service_choose:
        print("No service number entered")
        return
    index =int(service_choose) - 1
    if index < 0 or index >= len(vault):
        print("service not found under number")
        return
    check_password = input("enter password : ").strip()
    if not check_password:
        print("no password has entered")
        return
    check_hass_pass =hash_password(check_password)
    entry =vault[index]
    service , username, stored_hash =entry.split("|")

    if check_hass_pass == stored_hash:
        print(f" Username : {username}")
    else:
        print("deny access")

def delete_credential(vault):
    if not vault:
        print("No service found")
        return
    view_services(vault)
    choice= input("enter service number : ").strip()
    if not choice.isdigit():
        print("invalid service number")
        return
    index = int(choice) - 1
    if index < 0 or index >= len(vault):
        print("service not found ")
        return
    confirm=input("confirm delete service (y/n) : ").strip()
    if confirm =="y":
        removed =vault.pop(index)
        save_vault(vault)
        service = removed.split("|")[0]
        print(f" Deleted service :{service}")
    elif confirm =="n":
        print("delete cancelled")
    else:
        print("invalid input")

def search_credential(vault):
    if not vault:
        print("No service found")
        return
    choice =input("enter service to search : ").strip().lower()
    if not choice:
        print("invalid input")
        return
    found = False

    for index ,v in enumerate(vault,start=1):
        service = v.split("|")[0]
        if choice in service.lower():
            print(f"{index}. {service}")
            found =True

    if not found:
        print("no matching service found")

def clear_vault(vault):
    if not vault:
        print("no service found to clear")
        return
    confirm =input("confirm clear (y/n) : ").strip().lower()
    if confirm =="y":
        vault.clear()
        print("vault cleared")
        save_vault(vault)
    elif confirm =="n":
        print("vault clear cancelled")
    else:
        print("invalid input")
def main():
    vault = load_vault()

    while True:
        print("\nPassword Manager")
        print("1. Add credential")
        print("2. View services")
        print("3. View credential")
        print("4. Delete credential")
        print("5. Search credential")
        print("6. Clear vault")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_credential(vault)
        elif choice == "2":
            view_services(vault)
        elif choice == "3":
            view_credential(vault)
        elif choice == "4":
            delete_credential(vault)
        elif choice == "5":
            search_credential(vault)
        elif choice == "6":
            clear_vault(vault)
        elif choice == "0":
            confirm = input("Exit program? (y/n): ").strip().lower()
            if confirm == "y":
                break
        else:
            print("Invalid choice")



main()