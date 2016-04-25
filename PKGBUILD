# Original creator of stylish-dump: https://github.com/spectralsun/stylish-dump
# Fork and PKGBUILD by: spcmd <spcmd@openmailbox.org> (https://github.com/spcmd/stylish-dump)

pkgname=stylish-dump
pkgver=1.0
pkgrel=2
arch=('any')
url='https://github.com/spcmd/stylish-dump'
source=("stylish-dump" "config.py" "database.py" "stylish.py")
sha1sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')
pkgdesc='Dumps stylesheets from stylish extension for easy editing and version control'
depends=('python2-argh' 'python2-pathtools' 'python2-yaml' 'python2-sqlalchemy' 'python2-watchdog')

prepare() {
    # Set the username in the config
    sed -i "s/<user>/$(whoami)/g" config.py

    # Configure stylish-dump for the default Firefox profile
    PROFILE_DIR=$(find $HOME/.mozilla/firefox -type d -name "*.default" -printf "%f\n")
    if [[ -d "$HOME/.mozilla/firefox/$PROFILE_DIR" ]]; then
        # Set the Firefox profile dir name in the config
        sed -i "s/<profile>/$PROFILE_DIR/g" config.py
    fi

    # Set the output dir in the config
    sed -i "s/.css/.stylish-dump/" config.py
    # Create dir for the dumped .css files
    if [[ ! -d $HOME/.stylish-dump ]]; then
        mkdir $HOME/.stylish-dump
    fi
}

package() {
    install -Dm755 "$srcdir"/stylish-dump "$pkgdir"/usr/bin/stylish-dump
    install -Dm644 "$srcdir"/config.py "$pkgdir"/opt/${pkgname}/config.py
    install -Dm644 "$srcdir"/database.py "$pkgdir"/opt/${pkgname}/database.py
    install -Dm644 "$srcdir"/stylish.py "$pkgdir"/opt/${pkgname}/stylish.py
}
