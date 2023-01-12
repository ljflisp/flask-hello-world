{ pkgs }: {
  deps = [
    pkgs.sysstat
    pkgs.rsync
    pkgs.tcpdump
    pkgs.iproute2
    pkgs.busybox
    pkgs.mailutils
    pkgs.mcron
    pkgs.vim
    pkgs.wget
    pkgs.systemd
    pkgs.toybox
    pkgs.util-linux.bin
    pkgs.texinfoInteractive
    pkgs.man_db
    pkgs.openssh_with_kerberos
    pkgs.python39Packages.pip
    pkgs.python310
    pkgs.lua
    pkgs.php74
  ];
}