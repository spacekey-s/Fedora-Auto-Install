import subprocess
import time
import getpass

#password
password = getpass.getpass("Senha sudo: ")+"\n"

#functions
def limpar():#limpar
  subprocess.run(
    ["clear"]
  )

#instalar heroic launcher
def instalar_heroic():
  subprocess.run(
    [
      "flatpak",
      "remote-add",
      "--if-not-exists",
      "flathub",
      "https://flathub.org/repo/flathub.flatpakrepo"
    ]
  )

  subprocess.run(
    [
        "flatpak",
        "install",
        "-y",
        "flathub",
        "com.heroicgameslauncher.hgl"
    ]
  )

#instalar pacotes
def install(packages):
  subprocess.run(
            ["sudo", "-S", "dnf", "install", "-y"] + packages,
            input=password,
            text=True
          )

#verificar a instalação do rpm
def check_rpmfusion(password):

    repos = subprocess.run(
        ["dnf", "repolist"],
        capture_output=True,
        text=True
    ).stdout

    if "rpmfusion" in repos:
        print("RPM Fusion já está ativo.")
        return

    print("RPM Fusion não foi encontrado. Instalando...")

    fedora = subprocess.run(
        ["rpm", "-E", "%fedora"],
        capture_output=True,
        text=True
    ).stdout.strip()

    free = f"https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-{fedora}.noarch.rpm"
    nonfree = f"https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-{fedora}.noarch.rpm"

    subprocess.run(
        ["sudo", "-S", "dnf", "install", "-y", free],
        input=password,
        text=True
    )

    subprocess.run(
        ["sudo", "-S", "dnf", "install", "-y", nonfree],
        input=password,
        text=True
    )

def menu():
  #loop
  while True:
    try:
      time.sleep(1)
      limpar()
      #menu
      menu = int(input("""Opções do sistema:
        [ 1 ] Atualizar
        [ 2 ] Instalar Nvidia Drivers
        [ 3 ] Fedora Gaming
        [ 0 ] Sair
        => """))
    except ValueError:
      print("Número inválido!")
      continue

    match menu:
      case 0:
        print("Até logo...")
        time.sleep(1)
        break

      case 1:
        #hola
        print("Ola! Atualizando o sistema...")
        time.sleep(1)

        #process
        subprocess.run(
          ["sudo", "-S", "dnf", "update", "-y"],
          input=password,
          text=True
        )

      case 2:
        time.sleep(1)
        limpar()
        menuDriver = int(input("""
          [ 1 ] Drivers Recentes
          [ 2 ] Drivers Legacy (Model 600/700)
          [ 3 ] Drivers Legacy (Model 400/500)
          [ 0 ] Voltar ao menu
          => """))
        match menuDriver:
          case 0:
            print("Voltando...")
            time.sleep(1)

          case 1:
            driversActuall = [
              "akmod-nvidia",
              "xorg-x11-drv-nvidia-cuda"
            ]

            install(driversActuall)

          case 2:
            driversMedium = [
              "akmod-nvidia-470xx",
              "xorg-x11-drv-nvidia-470xx"
            ]

            install(driversMedium)

          case 3:
            driversOld = [
              "akmod-nvidia-470xx",
              "xorg-x11-drv-nvidia-470xx"
            ]

            install(driversOld)

      case 3:
        appsGame = [
        "steam",
        "lutris",
        "wine",
        "winetricks",
        "gamemode",
        "mangohud",
        "vulkan-tools",
        "piper",
        "openrgb"
        ]

        instalar_heroic()
        install(appsGame)

check_rpmfusion(password)
menu()
