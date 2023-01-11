{ pkgs }: {
  deps = [
    pkgs.python39Packages.pip
    pkgs.python310
    pkgs.lua
    pkgs.php74
  ];
}