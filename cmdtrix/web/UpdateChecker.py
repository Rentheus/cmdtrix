from requests import get as getRequest
from colorama import Fore, Style

def getLastestPackageVersion(package: str) -> str:
    try:
        response = getRequest(f'https://pypi.org/pypi/{package}/json')
        return response.json()['info']['version']
    except:
        return "0"


def newVersionAvailable(currentVersion: str, latestVersion: str) -> bool:
    currentVersion = ''.join(c for c in currentVersion if c.isdigit())
    latestVersion = ''.join(c for c in latestVersion if c.isdigit())
    return int(latestVersion) > int(currentVersion)


def printUpdateInformation(package: str, currentVersion: str):
    latestVersion = getLastestPackageVersion(package)
    if newVersionAvailable(currentVersion, latestVersion):
        print(Fore.YELLOW)
        print(f"A new release of {package} is available: {latestVersion}")
        print("To update, run:")
        print(f"python -m pip install --upgrade {package}")
        print(Style.RESET_ALL)
