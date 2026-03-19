#--- Modules ---
from rich import print
import subprocess
import time
import getpass
import sys

# --- password ---
password = getpass.getpass("Senha sudo: ")+"\n"

# --- functions ---
def limpar():#limpar
  subprocess.run(
    ["clear"]
  )

# --- instala o proton plus ---
def instalar_proton():
  subprocess.run(
    [
      "sudo",
      "flatpak remote-add",
      "--if-not-exists",
      "flathub",
      "https://flathub.org/repo/flathub.flatpakrepo"
    ]
  )
  subprocess.run(
    [
      "flatpak",
      "install",
      "flathub",
      "com.vysp3r.ProtonPlus"
    ]
  )

# --- instala heroic launcher ---
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

# --- instalar pacotes ---
def install(packages):
  subprocess.run(
            ["sudo", "-S", "dnf", "install", "-y"] + packages,
            input=password,
            text=True
          )

# --- verificar a instalação do rpm ---
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
  while True:
    time.sleep(1)
    limpar()
    #--- Menu do programa ---
    print(r"""[green]
 _____        _ ___           _        _ _
|  ___|__  __| |_ _|_ __  ___| |_ __ _| | |
| |_ / _ \/ _` || || '_ \/ __| __/ _` | | |
|  _|  __/ (_| || || | | \__ \ || (_| | | |
|_|  \___|\ __,_|___|_| |_|___/\__\__,_|_|_|
[/green]""")

    menu = input("""--- Opções do sistema ---
      [ 1 ] Atualizar
      [ 2 ] Instalar Nvidia Drivers
      [ 3 ] Fedora Gaming
      [ 4 ] Ferramentas Hacking (beta)
      [ 0 ] Sair
      => """)

    match menu:
      # --- Saída do programa ---
      case "0":
        limpar()
        print("Até logo...")
        time.sleep(1)
        sys.exit()

      # --- Atualizar o sistema ---
      case "1":
        time.sleep(1)
        limpar()
        update()

      # --- Drivers Nvidia ---
      case "2":
        time.sleep(1)
        limpar()
        driversNvidia()

      # --- Games ---
      case "3":
        time.sleep(1)
        limpar()
        appsGame()

      # --- Ferramentas Hacking ---
      case "4":
        time.sleep(1)
        limpar()
        hacking()

      # --- ERRO OPTION ---
      case _:
        limpar()
        print("Digite um número válido...")
        time.sleep(1)


  # --- OPÇÕES DO MENU ---


# --- CASE 1 ---
def update():
  print("Ola! Atualizando o sistema...")
  time.sleep(1)

  subprocess.run(
    ["sudo", "-S", "dnf", "update", "-y"],
    input=password,
    text=True
  )


# --- CASE 2 ---
def driversNvidia():
  while True:
    limpar()
    menuDriver = input("""--- Drivers Nvidia ---
      [ 1 ] Drivers Recentes
      [ 2 ] Drivers Legacy (Model 600/700)
      [ 3 ] Drivers Legacy (Model 400/500)
      [ 0 ] Voltar ao menu
      => """)

    match menuDriver:
      case "0":
        print("Voltando...")
        time.sleep(1)
        menu()
        break

      case "1":
        driversActuall = [
          "akmod-nvidia",
          "xorg-x11-drv-nvidia-cuda"
        ]

        install(driversActuall)

      case "2":
        driversMedium = [
          "akmod-nvidia-470xx",
          "xorg-x11-drv-nvidia-470xx"
        ]

        install(driversMedium)

      case "3":
        driversOld = [
          "akmod-nvidia-470xx",
          "xorg-x11-drv-nvidia-470xx"
        ]

        install(driversOld)

      case _:
        limpar()
        print("Digite um número válido.")
        time.sleep(1)


# --- CASE 3 ---
def appsGame():
  appsGame = [
  "stristeam",
  "lu",
  "wine",
  "winetricks",
  "gamemode",
  "mangohud",
  "vulkan-tools",
  "piper",
  "openrgb"
  ]

  instalar_proton()
  instalar_heroic()
  install(appsGame)


# --- CASE 4 ---
def hacking():
  while True:
    limpar()
    menuFerramentas = input("""--- Ferramentas Hacking ---
      [ 1 ] Softwares (hydra, hashcat ...)
      [ 2 ] Utilitários (nmap, whois ...)
      [ 0 ] Voltar
      => """)
    match menuFerramentas:
      case "0":
        limpar()
        print("Voltando...")
        menu()

      case "1":
        softwares = [
          "nmap", "masscan", "whois",
          "nikto", "sqlmap",
          "john", "hashcat", "hydra",
          "wireshark", "tcpdump", "aircrack-ng",
          "radare2", "binwalk",
        ]

        install(softwares)

      case "2":
        # Ferramentas instaláveis via dnf no Fedora
        ferramentas = [

            # --- Reconhecimento ---
            "nmap",            # scanner de portas e redes
            "masscan",         # scanner de portas ultra-rápido
            "whois",           # consultas WHOIS
            "bind-utils",      # dig, nslookup, host
            "traceroute",      # rastreamento de rotas
            "mtr",             # traceroute interativo em tempo real

            # --- Web ---
            "nikto",           # scanner de vulnerabilidades web
            "sqlmap",          # SQL injection
            "gobuster",        # brute force de diretórios/subdomínios

            # --- Senhas e Hashes ---
            "john",            # John the Ripper - cracking de hashes
            "hashcat",         # cracking com GPU
            "hydra",           # brute force de login em serviços

            # --- Redes e Wireless ---
            "wireshark",       # análise de pacotes (GUI)
            "wireshark-cli",   # tshark - captura de pacotes no terminal
            "aircrack-ng",     # auditoria de redes Wi-Fi
            "tcpdump",         # captura de tráfego via terminal
            "nmap-ncat",       # netcat moderno (ncat)
            "iftop",           # monitor de tráfego por interface
            "nload",           # gráfico de uso de banda em tempo real

            # --- Forense e Reversão ---
            "binwalk",         # análise de firmwares
            "radare2",         # engenharia reversa
            "strace",          # rastreia chamadas de sistema

            # --- Sistema e Rede ---
            "net-tools",       # ifconfig, netstat, route, arp
            "iproute",         # ip, ss
            "iputils",         # ping, tracepath
            "curl",            # transferência de dados via URL
            "wget",            # download de arquivos
            "htop",            # monitor de processos interativo
            "btop",            # monitor visual moderno
            "lsof",            # lista arquivos/portas abertos por processos
            "psmisc",          # killall, pstree, fuser
            "procps-ng",       # ps, top, free
            "util-linux",      # lsblk, blkid, fdisk
            "iotop",           # monitor de I/O de disco
            "dstat",           # estatísticas de sistema em tempo real
            "tor",             # anonimização de tráfego
            "proxychains-ng",  # forçar tráfego por proxies/tor

            # --- Utilitários ---
            "git",             # controle de versão
            "vim",             # editor de texto no terminal
            "neovim",          # vim moderno
            "tmux",            # multiplexador de terminal
            "make",            # automação de build
            "gcc",             # compilador C
            "python3-pip",     # gerenciador de pacotes Python
            "bash-completion", # autocomplete no bash
            "tree",            # exibe estrutura de diretórios
            "ncdu",            # análise de uso de disco interativa
            "ranger",          # gerenciador de arquivos no terminal
            "bat",             # cat com syntax highlight
            "ripgrep",         # busca em arquivos ultra-rápida (rg)
            "fd-find",         # substituto moderno do find
            "jq",              # manipulação de JSON no terminal
            "unzip",           # descompactação de .zip
            "p7zip",           # descompactação de .7z e outros
            "file",            # identifica tipo de arquivo

        ]

        install(ferramentas)

      case _:
        limpar()
        print("Digite um número válido.")
        time.sleep(1)


check_rpmfusion(password)
menu()
